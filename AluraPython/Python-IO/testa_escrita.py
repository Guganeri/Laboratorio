arquivo_contatos = open('contatos-escrita.csv', encoding='latin_1', mode='a')

contato = '11,Carol,carol@carol.com.br\n'

arquivo_contatos.write(contato)
