class Categoria:
    def __init__(self, id, nombre_c, descripcion) -> None:
        self.__id = id
        self.__nombre_c = nombre_c
        self.__descripcion = descripcion

    @property
    def id(self)->int:
        return self.__id
    @property
    def nombre_c(self)->str:
        return self.__nombre_c
    @property
    def descripcion(self)->str:
        return self.__descripcion