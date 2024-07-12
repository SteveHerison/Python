array = [20, 10, 2, 30, 12, 13, 15, 22]

total = 0
array_num = []

for num in array:
    if num % 2 == 0:
        array_num.append(num)
        total += num

#print(array_num)
#print(total)


lista = [ 10, 2, 5, 7, 6, 3]

soma =0

for num in lista:
    if num % 2 == 0:
        soma = soma+num

print(f'A soma de todos os elementos par da lista é: {soma}')

