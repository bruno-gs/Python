# for loop -- loop com loops certos para acontecer
# vendo o range -- inicia em 0

print('My name is')
for i in range(5):
    print(f'Jimmy Five Times {i}')

#soma de 0 a 100
total = 0
for num in range(101):
    total += num
print(total)

# WHile é equivalente
print('My name is')
i = 0
while i<5:
# for i in range(5):
    print(f'Jimmy Five Times {i}')
    i +=1

#range(10) == range (0,10) == range(inicio, fim [sem incluir])

#range(0,10,2) ou range(5,-1,-1) -- Quais as somas ou subtrações que deseja

#break and continue podem ser usados