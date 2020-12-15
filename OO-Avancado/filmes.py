
class Filme(object):
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        """
        Retorna quantidade de likes
        """
        return self.__likes

    def dar_likes(self):
        """
        Incrimenta likes
        """
        self.__likes += 1

    @property
    def nome(self):
        """
        Getter Nome
        """
        return self.__nome

    @nome.setter
    def nome(self, nome):
        """
        Setter Nome
        """
        self.__nome = nome


class Serie(object):
    """
    Classe Serie
    """
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        """
        Getter Likes
        """
        return self.__likes
    
    @property
    def nome(self):
        return self.__nome

    def dar_likes(self):
        """
        Likes Setter
        """
        self.__likes += 1

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

if __name__ == "__main__":
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    print(vingadores.nome)
    atlanta = Serie('atlanta', 2018, 2)
    print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}')