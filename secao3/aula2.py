#funcao print

#argumentos não nomeados
print(12, 34) 
print(12, 34) #por padrao, o separador é um espaço
#imprime os argumentos e, no python, a funcao print pula linha automaticamente
#argumentos nomeados. Eu mudo o separador 
print (12, 34, sep='-') 
print (27, 90, sep="/")

#argumento end
# \r\n -> CRLF (quebra de linha)
#end -> final do print
print (27, 90, end="\n") #nada muda
print (27, 90, end="##") #não quebra a linha, apenas coloca algum caractere

