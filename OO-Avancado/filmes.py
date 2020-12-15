class Programa(object):
    """
    Classe Programa
    """
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

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

    @property
    def likes(self):
        """
        Getter Likes
        """
        return self._likes

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    @property
    def duracao(self):
        """
        Getter Duracao
        """
        return self.__duracao


class Serie(Programa):
    """
    Classe Serie
    """
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas

    @property
    def temporadas(self):
        """
        Getter Temporadas
        """
        return self.__temporadas


if __name__ == "__main__":
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    atlanta = Serie('atlanta', 2018, 2)
    vingadores.dar_likes()
    vingadores.dar_likes()
    vingadores.dar_likes()
    atlanta.dar_likes()
    print(f'{vingadores.nome} - {vingadores.duracao}: {vingadores.likes}')
    print(f'{atlanta.nome} - {atlanta.temporadas}: {atlanta.likes}')