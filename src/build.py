import markdown
import os
import shutil


filepath = os.path.dirname(os.path.realpath('__file__'))


def prepare():
    filepath = os.path.dirname(os.path.realpath('__file__'))
    filepath = os.path.join(filepath, 'src' , 'public')
    print("Running in: " + filepath)
    if os.path.exists(filepath):
        shutil.rmtree(filepath)
    else:
        print("No files to cleanup.")

    try:
        os.mkdir(filepath)
    except OSError:
        print ("Creation of the directory %s failed" % filepath)
    else:
        print ("Successfully created the directory %s " % filepath)
    
def scanfiles():
    filepath = os.path.dirname(os.path.realpath('__file__'))
    filepath = os.path.join(filepath, 'src' , 'articles')
    files = []
    for (dirpath, dirnames, filenames) in os.walk(filepath):
        files.extend(filenames)
        break
    return files


prepare()

articles = scanfiles()
print("Files to phrase: " + str(articles))



def phrase(articles):
    filepath = os.path.dirname(os.path.realpath('__file__'))

    for article in articles:
        print("Phrasing " + article)
        article = os.path.splitext(article)[0]

        print(article)



        filenamebefore = article + '.md'
        filepathbefore = os.path.join(filepath, 'src' , 'articles', filenamebefore)
        
        filenameafter = article + '.html'
        filepathafter= os.path.join(filepath, 'src' , 'public', filenameafter)


        print("Using filepath: " + filepath)

        with open (filepathbefore, 'r' ) as f:
            text = f.read()
            f.close
            html = markdown.markdown(text)
            f.close

        with open (filepathafter, 'w') as f:
            f.write(html)
            f.close()

phrase(articles)