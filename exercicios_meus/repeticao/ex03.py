acumultiva = 0
#aqui está uma variável acumulativa

cont = 0
#aqui está uma variável para contar

for c in range(1, 501, 2):
    if c % 3 == 0:
        acumultiva = acumultiva + c
        cont = cont + 1
print(f'A soma dos {cont} valores solicitados é {acumultiva}')