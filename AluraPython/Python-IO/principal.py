try:
    with open('contatos.csv', encoding='latin_1', mode='r') as arquivo_contatos:
    #conteudo = arquivo_contatos.readline()
        for linha in arquivo_contatos:
            print(linha, end='')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')
finally:
    arquivo_contatos.close()