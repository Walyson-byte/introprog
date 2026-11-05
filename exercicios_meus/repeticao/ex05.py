cont = 0
acu = 0

for c in range(1,7):
    num = int(input(f'Digite o número {c}: '))
    if num % 2 == 0:
        cont += 1
        acu += num
print(f'Você informou {cont} números PARES e a soma foi {acu}')