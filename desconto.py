# Solicitar a quantidade de produtos comprados e o valor total dos produtos
x = int(input('Quantos produtos foram comprados? '))
y = float(input('Qual o valor total dos produtos? '))

Desconto0 = 0.00
Desconto10 = 0.10
Desconto20 = 0.20


# Calcular o desconto com base na quantidade de produtos
if  x <= 10:
    desconto_Final = y * Desconto0
elif x <= 20:
    desconto_Final = y * Desconto10
else:
    desconto_Final = y * Desconto20

# Calcular o valor final após o desconto
valor_final = y - desconto_Final

# Exibir o valor do desconto e o valor final
print(f'O desconto da compra é: R${desconto_Final:.2f}')
print(f'O valor final após o desconto é: R${valor_final:.2f}')