class Vendedores:
    def __init__(self, id_vendedor, nombre, apellidos,email,id_sucursal) -> None:
        self.__id_vendedor = id_vendedor
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__email = email
        self.__id_sucursal = id_sucursal

    @property
    def id_vendedor(self)->int:
        return self.__id_vendedor
    @property
    def nombre(self)->str:
        return self.__nombre
    @property
    def apellidos(self)->str:
        return self.__apellidos
    @property
    def email(self)->str:
        return self.__email
    @property
    def id_sucursal(self)->int:
        return self.__id_sucursal
    