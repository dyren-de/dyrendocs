import markdown 
import os
import shutil

import re 

def prepare():
    """
    Cleans the workspace
    and deletes everything in ./docs
    """
    filepath = os.path.dirname(os.path.realpath('__file__')) #getting the current path
    filepath = os.path.join(filepath, 'docs') #appending the workspace for python
    print("Running in: " + filepath)
    if os.path.exists(filepath): #if exists files are getting reqursivly removed
        try:
            shutil.rmtree(filepath)
        except Exception:
            print("Error")
            exit(1)

    else:
        print("No files to cleanup.")


    #copy files that have to be in the webroot dir
    filepath = os.path.dirname(os.path.realpath('__file__'))
    tmppathfrom = os.path.join(filepath, 'src' , 'include', 'root')
    tmppathto = os.path.join(filepath,'docs')
    shutil.copytree(tmppathfrom, tmppathto)
    try: 
        shutil.copytree(tmppathfrom, tmppathto)
    except OSError:
        print ("Webroot- Creation of the directory %s failed" % filepath)
    else:
        print ("Webroot-  Successfully created the directory %s " % filepath)

    filepath = os.path.dirname(os.path.realpath('__file__'))
    tmppathfrom = os.path.join(filepath, 'src' , 'include', 'assets')
    tmppathto = os.path.join(filepath,'docs', 'assets')

    try: #trying to make a new directory
        shutil.copytree(tmppathfrom, tmppathto)
    except OSError:
        print ("Creation of the directory %s failed" % filepath)
    else:
        print ("Successfully created the directory %s " % filepath)


    filepath = os.path.dirname(os.path.realpath('__file__'))
    filepath= os.path.join(filepath, 'src' , 'include')

    
    tmppath = os.path.join(filepath, 'head.html')
    with open (tmppath, 'r') as f:
        global head
        head = f.read()
        f.close

    tmppath = os.path.join(filepath, 'footer.html')
    with open (tmppath, 'r' , encoding="utf8") as f:
        global footer
        footer = f.read()
        f.close
prepare()


def scanfiles():
    """
    Scanning wich files need to be processed.
    """

    filepath = os.path.dirname(os.path.realpath('__file__'))
    filepath= os.path.join(filepath, 'src' , 'articles')
    results = [os.path.join(dp, f) for dp, dn, filenames in os.walk(filepath) for f in filenames if os.path.splitext(f)[1] == '.md']

    oldfiles= results


    newfiles = []
    realnewpath = os.path.dirname(os.path.realpath('__file__'))
    realnewpath = os.path.join('src','articles')
    for result in results:
        newpath = result.replace(realnewpath, "docs")
        newpath = os.path.splitext(newpath)[0]
        newpath = newpath + ".html"
        newfiles.append(newpath)

    return oldfiles,newfiles

oldfiles,newfiles = scanfiles()

articles = scanfiles()


def phrase(oldfiles,newfiles):

    for oldfile,newfile in zip(oldfiles,newfiles):
        print("Phrasing: " + oldfile + " to " + newfile)

        filepath= os.path.dirname(newfile)
        if not os.path.exists(filepath):
            os.makedirs(filepath)

        with open(oldfile, 'r', encoding="utf8") as f:
            text = f.read()
            f.close
            md = markdown.markdown(text, extensions=['toc','meta'])
            html = str(head) + str(md) + str(footer)

        with open(newfile, 'w', encoding='utf-8-sig') as f:
            f.write(html)
            f.close()

def minifycss():
    """
    Used to minify css
    """
    pathtocss = os.path.dirname(os.path.realpath('__file__'))
    pathtocss = os.path.join(pathtocss, 'docs', 'assets' , 'css', 'style.css')
    print(pathtocss)
    with open(pathtocss, 'r', encoding='utf-8') as f:
        css= f.read()
        f.close()

    # remove comments - break some hacks
    css = re.sub( r'\s*/\*\s*\*/', "$$IE6$$", css ) # preserve IE<6 comment hack
    css = re.sub( r'/\*[\s\S]*?\*/', "", css )
    css = css.replace( "$$IE6$$", '/**/' ) # preserve IE<6 comment hack

    # remove quotes from url() 
    css = re.sub( r'url\((["\'])([^)]*)\1\)', r'url(\2)', css )

    # remove spaces
    css = re.sub( r'\s+', ' ', css )

    # shorten colors
    css = re.sub( r'#([0-9a-f])\1([0-9a-f])\2([0-9a-f])\3(\s|;)', r'#\1\2\3\4', css )

    # remove unnecessary zeros
    css = re.sub( r':\s*0(\.\d+([cm]m|e[mx]|in|p[ctx]))\s*;', r':\1;', css )

    for rule in re.findall( r'([^{]+){([^}]*)}', css ):

        # we don't need spaces around operators
        selectors = [re.sub( r'(?<=[\[\(>+=])\s+|\s+(?=[=~^$*|>+\]\)])', r'', selector.strip() ) for selector in rule[0].split( ',' )]

        # order is important, but we still want to discard repetitions
        properties = {}
        porder = []
        for prop in re.findall( '(.*?):(.*?)(;|$)', rule[1] ):
            key = prop[0].strip().lower()
            if key not in porder: porder.append( key )
            properties[ key ] = prop[1].strip()

        # output rule if it contains any declarations
        if properties:
            #print("%s{%s}" % ( ','.join( selectors ), ''.join(['%s:%s;' % (key, properties[key]) for key in porder])[:-1] ))
            pass

    with open(pathtocss, 'w', encoding='utf-8-sig') as f:
        f.write(css)
        f.close()
    


    
    
phrase(oldfiles,newfiles)

minifycss()

exit(0)