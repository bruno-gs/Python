#           ## o programa tratar possiveis erros ou problemas
#           # continuando sem interromper o processso

#           def div42by(divideBy):
#               try:
#                   return 42 / divideBy

#               # Aqui colocamos um retorno de print, caso caia na situação
#               # de divisão por 0
#               # retornará None
#               # podemos também deixar sem especificar
#               # dai qq erro dará essa mensagem
#               # except ZeroDivisionError:
#               except:
#                   print('Error: You tried to divide by zero.')

#           print(div42by(2))
#           print(div42by(12))
#           # O programa para de executar aqui, por n haver div por 0
#           print(div42by(0))
#           # portanto, essa linha nunca será executada
#           print(div42by(1))

#           # então vamos resolver com um try, except


print('How many cats do you have?')
# como aqui pode ser digitados qq valores, por ex 'six' ou 'seven'
# teremos um erro na hora de passar esse valor para inteiro
# então colocaremos um try / except
numCats = input()

try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    else:
        print('That is not that many cats.')

except ValueError:
    print('You did not enter a number.')