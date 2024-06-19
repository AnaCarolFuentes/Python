# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(1 + 1) #ele reconhece dois ints e soma os valores
print("a" + "b") #polimorfismo, nesse caso, ele concatena as strings

#-----------------------

print('1', type('1'))
print(int('1'), type(int('1')))
print(int('1') + 1)
print(str('1') + str('2')) #exibe 12
print(bool('')) #uma string vazia é false, qualquer outro valor é True
