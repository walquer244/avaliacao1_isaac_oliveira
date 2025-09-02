#Questão 1 (Fácil) – Verificação de Número Par ou Ímpar
numero = int(input("Digite um numero: "))
if numero % 2 == 0: 
    print(f"O {numero} é par")
else:
    print(f"O {numero} é impar")
if numero < 0:
    print("Este numero é negativo") 
elif numero > 0 :
    print("Este numero é positivo")   
else: 
    print("Você digitou o numero 0")