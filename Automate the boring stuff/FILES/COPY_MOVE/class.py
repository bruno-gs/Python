import shutil
# here are the example, but the folder 'Automate...' contain Space, and I get a error
# You can change the name of the new file - complete the path with the name and extension of the file you want
shutil.copy(r'C:\Users\ilidio\Documents\Python\Automate the boring stuff\FILES\READ_WRITE_PlainTextFiles\hello2.txt', r'C:\Users\ilidio\Documents\Python\Automate the boring stuff\FILES\COPY_MOVE')

# copy an entire folder -- make a backup for the folder
shutil.copytree('c:\\delicious','c:\\delicious_backup')

# to move a file to a location
shutil.move('c:\\spam.txt', 'c:\\delicious\\walnut')

# to rename, use the move, but change the name of the file
shutil.move('c:\\delicious\\walnut\\spam.txt', 'c:\\delicious\\walnut\\spam2.txt')
