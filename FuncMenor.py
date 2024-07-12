#lista = [2,4,5,10,20]
#def encontra_menor(lista):
    #minimo = lista[0]
    #for i in lista:
        #if i < minimo:
            #minimo = i
        #return minimo


#menor = encontra_menor(lista)

#print('O menor item da lista é: [{}]'.format(menor))

def ehPar(n):
    r = n % 2 == 0
    return r
def soma_pares(lista):
    soma = 0
    for i in lista:
        if ehPar(i):
            soma += i


    return soma


lista= [2,4,5,10,20,6,8]
soma = soma_pares(lista)

print('A soma é [{}]'.format(soma))
