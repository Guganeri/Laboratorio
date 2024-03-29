import contatos_utils

try:
    #contatos = contatos_utils.csv_para_contatos('contatos-escrita.csv')
    #contatos_utils.contatos_para_pickle(contatos, 'contatos.pickle')
    #contatos_utils.contatos_para_json(contatos, 'contatos.json')

    contatos = contatos_utils.json_para_contatos('contatos.json')

    for contato in contatos: 
        print(f'{contato.id} - {contato.nome} - {contato.email}')

except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')