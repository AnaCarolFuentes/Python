#Formatação de strings

nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

#f-strings
mensagem_1 = f'{nome} pesa {peso:.2f} kg'#exibe o peso com 2 casas decimais
mensagem_2 = f'{nome} tem {altura:.2f} metros'
mensagem_3 = f'{nome} tem {imc:.2f} de imc'

print(mensagem_1)
print(mensagem_2)
print(mensagem_3)

#Função format
a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}' #a primeira chave referencia o primeiro parâmetro passado p/ o format
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato) 

print(formato)
