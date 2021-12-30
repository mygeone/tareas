class Producto:
    def __init__(self, codigo, nombre, precio, stock,categoria) -> None:
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__categoria = categoria

    @property
    def codigo(self)->str:
        return self.__codigo
    @property
    def nombre(self)->str:
        return self.__nombre
    @property
    def precio(self)->int:
        return self.__precio
    @property
    def stock(self)->int:
        return self.__stock
    
    @property
    def categoria(self)->int:
        return self.__categoria