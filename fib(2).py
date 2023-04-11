#lucaskgf

#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
#IMPORTANTE:
#Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;


num = int(input("Digite um número: "))

num1 = 0
num2 = 1
fib = 0

while fib < num:
    fib = num1 + num2
    num1 = num2
    num2 = fib

if fib == num:
    print(f"{num} pertence à sequência de Fibonacci".format(num))
else:
    print(f"{num} não pertence à sequência de Fibonacci")