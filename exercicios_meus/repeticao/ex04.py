num = int(input('Digite o número para ver sua tabuada: '))

for c in range(1, 11):
    resultado = num * c
    print(f'{num} x {c} = {resultado}')