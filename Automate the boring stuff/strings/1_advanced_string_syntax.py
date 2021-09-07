'''
 -- usar aspas para usar as simples em outro lugar
"That is Alice's cat."

-- usar barra invertida para não precisar das aspas simples
'Say hi to Bob\'s mother.'

TABELA DE UTILIZAÇÕES: 
    \'  -- aspas simples
    \"  -- aspas duplas
    \t  -- tabulação
    \n  -- pular linha
    \\  -- usar a barra invertida msm

    print('Hello there!\nHow are you?\nI\'m fine.')

    pode usar também r'' -- dai aparecerá tudo q estiver nas aspas
'''

'''
RECAP

Strings are enclosed by a pair of single quotes 
    or double quotes (as long as the same kind are used).

Escape characters let you put quotes 
    and other characters that are hard to type inside strings.

Raw strings (which have the r prefix before the first quote) will literally 
    print any backslashes in the string and ignore escape characters.

Multiline strings begin and end with three quotes, and can span multiple lines.

Indexes, slices, and the "in" and "not in" operators all work with strings.
'''