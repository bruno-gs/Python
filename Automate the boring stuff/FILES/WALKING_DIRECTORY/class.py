import os
# to walk in a folder and its subfolders and files
for folderName, subfolders, filenames in os.walk(r'C:\Users\ilidio\Documents\CCP130_DESENV_ALG'):
    print(f'The folder is {folderName}')
    print(f'The subfolders in {folderName} are: {subfolders}')
    print(f'The filenames in {folderName} are: {filenames}')
    print()
    
    for subfolder in subfolders:
        if 'fish' in subfolder:
            #os.rmdir(subfolder)

    for file in filenames:
        if file.endswith('.py'):
            #shutil.copy(os.join(folderName,file), os.join(folderName,file + '.backup'))   

# One of the outputs
'''
The folder is C:\Users\ilidio\Documents\CCP130_DESENV_ALG\AULA14-12NOV
The subfolders in C:\Users\ilidio\Documents\CCP130_DESENV_ALG\AULA14-12NOV are: ['LAB']
The filenames in C:\Users\ilidio\Documents\CCP130_DESENV_ALG\AULA14-12NOV are: ['calculo.c', 'calculo.h', 'main.c']
'''

