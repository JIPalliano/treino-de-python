dados = [1,6,2,3,6,4,5,6,7,8]

def algoritimo(dados):
    tam = len(dados)
    for v in range(0, tam, 1):
        flag = 0
        for i in range(0, tam - 1, 1):
            if dados[i] > dados[i + 1]:
                aux = dados[i]
                dados[i] = dados[i+1]
                dados[i+1] = aux
                flag = 1
        if flag == 0:
            return dados

print(algoritimo(dados))
x = dados

for i in range(0, x, 1):
    print(i)


