arquivo_contatos = open('contatos.csv', encoding='latin_1')

#conteudo = arquivo_contatos.readline()

for linha in arquivo_contatos:
    print(linha, end='')
