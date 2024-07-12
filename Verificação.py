# try:
#     x = int(input("Qual o numero?"))
# except ValueError:
#     print("Entre com o número válido.")

#while True:
   # try:
       # x = int(input("Qual o numero? "))
       # break
    #except #ValueError:
        #print("Digite um numero valido.")

def dividir(x, y):
    try:
        resultado = x / y
        print("A resposta é:", resultado)
    except ZeroDivisionError:
        print("Divisão por zero")

# Solicita os números do usuário
x = int(input("Primeiro número? "))
y = int(input("Segundo número? "))

# Chama a função dividir com os números fornecidos
dividir(x, y)


