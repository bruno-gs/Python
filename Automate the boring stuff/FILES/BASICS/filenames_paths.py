# for a path
print('c:\\spam\\eggs.png')

# you can use the 'r' to exclude the second '\'
print(r'c:\spam\eggs.png')

#you can use the 'join' to make the PATH
print('\\'.join(['folder1', 'folder2','folder3','file.png']))


# using the 'os' library
import os
print(os.path.join('folder1', 'folder2','folder3','file.png'))
os.sep
# Show the path that you are
print(os.getcwd())

##########################################
# to change the path you are: os.chdir(c:\\)

##########################################
# ABSOLUTE FILE PATH: 'c:\\folder1\\folder2\\folder3\\eggs.png'

# RELATIVE FILE PATH: 'eggs.png' -- search on the path you are 
        # you can : 'folder2\\folder3\\eggs.png'

# to know what is the absolute path of a file
    # os.path.abspath('spam.png')

# to know every file and folder in a folder, use: os.listdir('c:\\automatebook')
    # know if is file: os.path.isfile()

# create new folder: os.makedirs('c:\\delicious\\walnut\\waffles')







