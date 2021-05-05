import markdown
import os
import shutil

articles=[]

filepath = os.path.dirname(os.path.realpath('__file__'))




def prepare():
    filepath = os.path.dirname(os.path.realpath('__file__'))
    filepath = os.path.join(filepath, 'src' , 'public')
    print(filepath)
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
    


prepare()



filepathbefore = os.path.join(filepath, 'src' , 'articles', 'test.md')

filepathafter= os.path.join(filepath, 'src' , 'public', 'test.html')

print(filepath)

with open (filepathbefore, 'r' ) as f:
    text = f.read()
    f.close
    html = markdown.markdown(text)
    f.close

with open (filepathafter, 'w') as f:
    f.write(html)
    f.close()
