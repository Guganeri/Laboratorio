arquivo = open('contatos-escrita.csv', encoding='latin_1', mode='a+')

print(type(arquivo.buffer))

contato = bytes('15, Veronica, veronica@veronica.com.br', 'latin_1')
arquivo.buffer.write(contato)


arquivo.close()