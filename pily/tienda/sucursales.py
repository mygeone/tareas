class Sucursales:
    def __init__(self, id_sucursal, nombre, direccion,telefono,email,id_comuna) -> None:
        self.__id_sucursal = id_sucursal
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        self.__id_comuna = id_comuna

    @property
    def id_sucursal(self)->int:
        return self.__id_sucursal
    @property
    def nombre(self)->str:
        return self.__nombre
    @property
    def direccion(self)->str:
        return self.__direccion
    @property
    def telefono(self)->int:
        return self.__telefono
    @property
    def email(self)->str:
        return self.__email
    @property
    def id_comuna(self)->int:
        return self.__id_comuna
    