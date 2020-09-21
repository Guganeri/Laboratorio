arquivo_contatos = open('contatos-escrita.csv', encoding='latin_1', mode='a')

contatos = ['11,Carol,carol@carol.com.br\n',
           '12,Ana,ana@ana.com.br\n',
           '13,AnaOliveira,ana@ana.com.br\n',
           '14,Anaclaudia,ana@ana.com.br\n',
           '15,Felipe,felipa@felipe.com.br\n']

for contato in contatos:
    arquivo_contatos.write(contato)
arquivo_contatos.flush()

input('Pressione <Enter> para encerrrar o programa')
