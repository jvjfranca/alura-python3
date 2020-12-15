class Programa(object):
    """
    Classe Programa
    """
    _likes = 0
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano

    @property
    def nome(self):
        """
        Getter Nome
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Setter Nome
        """
        self._nome = nome.title()

    @property
    def ano(self):
        """
        Getter Ano
        """
        return self._ano

    @ano.setter
    def funcname(self, ano):
        """
        Setter Ano
        """
        self._ano = ano

    def dar_likes(self):
        """
        Incrementa Likes
        """
        self._likes += 1

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao


class Serie(Programa):
    """
    Classe Serie
    """
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas



if __name__ == "__main__":
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    print(vingadores.nome)
    atlanta = Serie('atlanta', 2018, 2)
    print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}')