class Usuario:
    def __init__(self, id, usuario, password) -> None:
        self.__id = id
        self.__usuario = usuario
        self.__password = password

    @property
    def id(self):
        return self.__id
    @property
    def usuario(self):
        return self.__usuario
    @property
    def password(self):
        return self.__password
    