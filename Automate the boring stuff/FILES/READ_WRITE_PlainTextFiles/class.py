################################################################
# to open a file
helloFile = open(r'C:\Users\ilidio\Documents\Python\Automate the boring stuff\FILES\READ_WRITE_PlainTextFiles\hello.txt')
# read and save the content of the file
content = helloFile.read()
# close the file
helloFile.close()
# print the content of the file, after closed
print(content)

################################################################
helloFile = open(r'C:\Users\ilidio\Documents\Python\Automate the boring stuff\FILES\READ_WRITE_PlainTextFiles\hello.txt')
# each line as a string in a list
# OUTPUT: ['hello world \n', "i'm Bruno\n", "let's learn to code\n"]
print(helloFile.readlines())
helloFile.close()

################################################################
# write a file -- new file and the 'w' argument
helloFile = open(r'C:\Users\ilidio\Documents\Python\Automate the boring stuff\FILES\READ_WRITE_PlainTextFiles\hello2.txt', 'w')

helloFile.write('HELLO!!!!!!!!!!!!!!!!!!!!\nTMJ')
helloFile.close()

# append mode
helloFile = open(r'C:\Users\ilidio\Documents\Python\Automate the boring stuff\FILES\READ_WRITE_PlainTextFiles\hello2.txt', 'a')
helloFile.write('append stage!\ngabigol\nsantos maior do mundo\n')
helloFile.close()

################################################################

