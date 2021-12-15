import os
# this will delete the file -- pass the path if you not in there
os.unlink('bacon.txt')

# to delete an empty folder
os.rmdir(r'c:\delicious')

# to delete a full folder
import shutil
shutil.rmtree(r'c:\delicious')


#### To use a more safe function
import send2trash # need to install
send2trash.send2trash(r'c:\users\al\desktop\Important')
