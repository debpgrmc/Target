#PRIMEIRA QUESTÃO:
'''A variável, soma é uma variável de soma acumulada que vai somar os 13 termos da sequência (quantidade definida pela variável K).
Desta forma, a variável SOMA irá retornar o valor da soma da sequência de 1 a 13, ou seja: 1 + 2 + 3+ ... + 13. O que resultará em SOMA = 91'''



#SEGUNDA QUESTÃO: (linguagem Python)
def fibonacci_sequence(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

def verifica_pertence(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

numero = int(input("Digite um número: "))

print("Sequência de Fibonacci até", numero, ":")
fibonacci_sequence(numero)

if verifica_pertence(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")


#TERCEIRA QUESTÃO:
'''a) 9
b) 128
c) 49
d) 100
e) 13
f) '''



#QUARTA QUESTÃO:
'''Acredito que a melhor forma seria ligar um interruptor e esperar o tempo da lâmpada esquentar, dado esse tempo desligar o interruptor e ligar outro. Desta forma temos 3 diferenciais entre as lâmpadas que nos ajudarão a saber qual interruptor ligou cada lâmpada. Teremos:
1- Uma lâmpada quente e apagada, conectada ao primeiro interruptor acionado
2 - Uma lâmpada acesa conectada ao segundo interruptor acionado
3- Uma lâmpada fria e apagada que não foi, em nenhum momento, acionada por seu respectivo interruptor'''



#QUINTA QUESTÃO:
def inverte_string(s):
    inverted = ""
    for char in s:
        inverted = char + inverted
    return inverted


string_original = "Olá, mundo!"
string_invertida = inverte_string(string_original)
print(string_invertida)
