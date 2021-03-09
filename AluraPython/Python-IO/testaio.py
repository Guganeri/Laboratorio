arquivo = open('contatos-escrita.csv', encoding='latin_1', mode='a+')

print(type(arquivo.buffer))

conteudo = arquivo.buffer.read()
print(conteudo)

arquivo.close()