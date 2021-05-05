import markdown
import os
import shutil


def prepare():
    """
    Cleans the workspace
    and deletes everything in ./src/public
    """
    filepath = os.path.dirname(os.path.realpath('__file__')) #getting the current path
    filepath = os.path.join(filepath, 'src' , 'public') #appending the workspace for python
    print("Running in: " + filepath)
    if os.path.exists(filepath): #if exists files are getting reqursivly removed
        shutil.rmtree(filepath)
    else:
        print("No files to cleanup.")

    try: #trying to make a new directory
        os.mkdir(filepath)
    except OSError:
        print ("Creation of the directory %s failed" % filepath)
    else:
        print ("Successfully created the directory %s " % filepath)
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
    for result in results:
        newpath = result.replace("articles", "public")
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

        with open (oldfile, 'r' ) as f:
            text = f.read()
            f.close
            html = markdown.markdown(text)
            f.close

        with open (newfile, 'w') as f:
            f.write(html)
            f.close()


    
    
phrase(oldfiles,newfiles)



exit(0)