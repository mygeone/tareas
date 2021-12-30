class Ventas:
    def __init__(self, id_venta, monto, fecha,id_vendedor) -> None:
        self.__id_venta = id_venta
        self.__monto = monto
        self.__fecha = fecha
        self.__id_vendedor = id_vendedor

    @property
    def id_venta(self)->int:
        return self.__id_venta
    @property
    def monto(self)->int:
        return self.__monto
    @property
    def fecha(self)->str:
        return self.__fecha
    @property
    def id_vendedor(self)->int:
        return self.__id_vendedor