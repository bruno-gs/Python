import re

# Use the sub method to replace the name of the agents
nameRegex = re.compile(r'Agent \w+')
# Output: ['Agent Alice', 'Agent Bob']
print(nameRegex.findall('Agent Alice gave the secret documents to Agent Bob'))

# Using the sub method
# Output: REDACTED gave the secret documents to REDACTED
# REDACTED: ​to remove information from a document because you do not want the public to see it
print(nameRegex.sub('REDACTED','Agent Alice gave the secret documents to Agent Bob'))

############# SUB for part of the information
# Using the groups and the sub to analise the information and substitute

# here, the first \w is a group
nameRegex = re.compile(r'Agent (\w)\w*')
# Output: ['A', 'B']      ### Group 1
print(nameRegex.findall('Agent Alice gave the secret documents to Agent Bob'))

# Here the \1 is the first group of the information at the object 'nameRegex'
# Output: Agent A**** gave the secret documents to Agent B****    #### using group one and completed with *
print(nameRegex.sub(r'Agent \1****','Agent Alice gave the secret documents to Agent Bob'))


###########################################################################################
# VERBOSE MODE -- re.VERBOSE
    # this mode is important to documentation
    # you can put some comments to improve others understand
    # You can use this to help you remenber what each parameter means

re.compile(r'''
(\d\d\d-) |         # area code (without parens, with dash)
(\(\d\d\d) )        # -or- area code with parens, with no dash
\d\d\d              # first 3 digits
-                   # second dash
\d\d\d\d            # last 4 digits
\sx\d{2,4}          # extension, like x1234''', re.IGNORECASE | re.DOTALL | re.VERBOSE) # you can use several methods
# Igonore case: maiusculo e minusculo
# dotall -- pega tudo -- pra pegar o pular linha
# verbose para documentação