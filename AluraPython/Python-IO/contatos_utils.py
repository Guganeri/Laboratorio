import csv
from contato import Contato


def csv_para_contatos(caminho, encoding='latin_1'):
    contatos = []

    with open(caminho, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            id = linha[0]
            nome = linha[1]
            email = linha[2]

            contato = Contato(id, nome, email)
            contatos.append(contato)

    return contatos