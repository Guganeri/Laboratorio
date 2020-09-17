class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano        
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes} Like(s)'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} - {self.likes} Like(s)'
        

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} Temporada(s) - {self.likes} Like(s)'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas


    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas
        
    def __len__(self):
        return len(self._programas)   




vingadores = Filme("vingadores - guerra Infinita", "2018", "03 horas")
vingadores.dar_like()

avatar = Filme("Avatar - A lenda de Ang", "2010", "03 horas")
avatar.dar_like()
avatar.dar_like()
avatar.dar_like()
avatar.dar_like()
avatar.dar_like()
#print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
#       f'- Duracao: {vingadores.duracao} - Likes: {vingadores.likes}')

atlanta = Serie("atlanta", "2018", "02")
atlanta.dar_like()
atlanta.dar_like()

dark = Serie("Dark", "2019", "03")
dark.dar_like()
dark.dar_like()
dark.dar_like()
dark.dar_like()
dark.dar_like()
#print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
#       f'- Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')


filmes_e_series = [vingadores, atlanta, dark, avatar]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana: 
    print(programa)

#print(f'Tá ou não tá? {avatar in playlist_fim_de_semana}')