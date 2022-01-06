class V_totalventasxvendedores:
    def __init__(self, sumMonto, nombre, apellidos) -> None:
        self.__sumMonto = sumMonto
        self.__nombre = nombre
        self.__apellidos = apellidos

    @property
    def sumMonto(self)->int:
        return self.__sumMonto
    @property
    def nombre(self)->str:
        return self.__nombre
    @property
    def apellidos(self)->str:
        return self.__apellidos
