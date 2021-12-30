import copy
from funciones import modificar_producto

class Bodega:
    def __init__(self, cantidad, comuna, calle, numero, jefe):
        self.categorias = ["Bebidas","Carnes" ,"Cecinas" ,"Fideos", "Harinas", "Arroz"]
        self.cantidad = cantidad
        self.comuna = comuna
        self.calle = calle
        self.numero = numero
        self.jefe = jefe
        self.listaProductos = []
        self.listaIngresados = []
        self.listaSalidos = []

    def informe_bodega(self):
        print("Cantidad de productos:", self.cantidad)
        print("Cantidad de productos ingresador:", len(self.listaIngresados))
        print("Cantidad de productos salidos:", len(self.listaSalidos))

    def informe_ventas(self):
        print("Productos Ingresado:")
        for categoria in self.categorias:
            total = 0
            print("Categoria:",categoria)
            for producto in self.listaIngresados:
                if producto.categoria == categoria:
                    total += (producto.precio * producto.cantidad)
            print("Total de ", total)

        print("\nProductos salidas:")
        for categoria in self.categorias:
            total = 0
            print("Categoria:", categoria)
            for producto in self.listaSalidos:
                if producto.categoria == categoria:
                    total += (producto.precio * producto.cantidad)
            print("Total de ", total)



class Empleado:
    def __init__(self, nombre, rut, FechaNac, usuario, contraseña):
        self.run = nombre
        self.nombre = rut
        self.fechanac = FechaNac
        self.usuario = usuario
        self.contraseña = contraseña


class Administrador(Empleado):
    def __init__(self, nombre, rut, fechaNac, usuario, contraseña):
        Empleado.__init__(self, nombre, rut, fechaNac, usuario, contraseña)
        self.perfil = 'Administrador'

    def ingresar_producto(self, bodega):
        se_encuentra = False
        print("tipo de dato ingresado incorrecto\n")
        codebarra = input("Ingrese codigo de barras: ")
        codebarra = int(codebarra)
        for producto in bodega.listaProductos:
                print("Producto ya existente\n")
                cantidad = input("Ingrese cantidad del producto agregar: ")
                while( not cantidad.isdigit() or int(cantidad) < 1):
                    print("tipo de dato ingresado incorrecto\n")
                    cantidad = input("Ingrese cantidad del producto agregar: ")
                cantidad = int(cantidad)
                producto.cantidad += cantidad
                print("Cantidad aumentada\n")

                for product in bodega.listaIngresados:
                        product.cantidad += cantidad
                        break
                se_encuentra = True
                break
        if( not se_encuentra):
            print("Producto Nuevo \n")
            nombre = input("Ingrese nombre del producto: ")
            categoria = input("Ingrese categoria del producto (fideos-galletas-jabon-arroz-carne-papas): ").capitalize()
            while( categoria not in bodega.categorias):
                print("Categoría Incorrecta \n")
                categoria = input("Ingrese categoria del producto (fideos-galletas-jabon-arroz-carne-papas): ").capitalize()
                marca = input("Ingrese marca del producto: ")
                precio = input("Ingrese precio del producto: ")
                print("tipo de dato ingresado incorrecto o menor a 100\n")
                precio = input("Ingrese precio del producto: ")
                precio = int(precio)
                cantidad = input("Ingrese cantidad del producto: ")
                print("tipo de dato ingresado incorrecto\n")
                cantidad = input("Ingrese cantidad del producto: ")
            cantidad = int(cantidad)
            producto_nuevo = Producto(codebarra, nombre, categoria, marca, precio, cantidad)
            bodega.listaProductos.append(producto_nuevo)
            prod_nuevo = copy.copy(producto_nuevo)
            bodega.cantidad += 1
            bodega.listaIngresados.append(prod_nuevo)
            print("Producto agregado \n")

    def sacar_producto(self,bodega):
        salida = True
        salida2 = True
        se_encuentra = False
        codebarra = input("Ingrese codigo de barras: ")
        while (not codebarra.isdigit() or len(codebarra) < 1):
            print("tipo de dato ingresado incorrecto\n")
            codebarra = input("Ingrese codigo de barras: ")
        codebarra = int(codebarra)
        for producto in bodega.listaProductos:
            if producto.codebarra == codebarra:
                print("Producto encontrado\n")
                cantidad = input("Ingrese cantidad a vender: ")
                while (not cantidad.isdigit() or int(cantidad) < 1 or int(cantidad) > producto.cantidad):
                    print("tipo de dato ingresado incorrecto o  cantidad superior máximo o menor a 0\n")
                    cantidad = input("Ingrese cantidad a vender: ")
                cantidad = int(cantidad)
                if( cantidad < producto.cantidad):
                    salida = False
                    for product in bodega.listaSalidos:
                        if product.codebarra == codebarra:
                            product.cantidad += cantidad
                            producto.cantidad -= cantidad
                            salida = True
                            
                else:
                    salida2 = False
                    for product in bodega.listaSalidos:
                        if product.codebarra == codebarra:
                            bodega.listaProductos.remove(producto)
                            product.cantidad += producto.cantidad
                            bodega.cantidad -= 1
                            salida2 = True
                           
                if (not salida):
                    producto_salida = copy.copy(producto)
                    producto.cantidad -= cantidad
                    producto_salida.cantidad = cantidad
                    bodega.listaSalidos.append(producto_salida)
                if (not salida2):
                    bodega.listaProductos.remove(producto)
                    bodega.listaSalidos.append(producto)
                    bodega.cantidad -= 1
                se_encuentra = True
               
        if (not se_encuentra):
            print("No se encuentra producto\n")

    def eliminar_producto(self, bodega):
        se_encuentra = False
        codebarra = input("Ingrese codigo de barras: ")
        while (not codebarra.isdigit() or len(codebarra) < 1):
            print("tipo de dato ingresado incorrecto\n")
            codebarra = input("Ingrese codigo de barras: ")
        codebarra = int(codebarra)
        for producto in bodega.listaProductos:
            if producto.codebarra == codebarra:
                print("Producto encontrado\n")
                bodega.listaProductos.remove(producto)
                bodega.cantidad -= 1
                salida = False
                for product in bodega.listaSalidos:
                    if product.codebarra == codebarra:
                        product.cantidad += producto.cantidad
                        salida = True
                       
                if (not salida):
                    bodega.listaSalidos.append(producto)
                se_encuentra = True
               
        if (not se_encuentra):
            print("No se encuentra producto\n")

    def modificar_producto(self, bodega):
        se_encuentra = False
        codebarra = input("Ingrese codigo de barras: ")
        while (not codebarra.isdigit() or len(codebarra) < 1):
            print("tipo de dato ingresado incorrecto\n")
            codebarra = input("Ingrese codigo de barras: ")
        codebarra = int(codebarra)
        for producto in bodega.listaProductos:
            if producto.codebarra == codebarra:
                print("Producto enontrado\n")
                propiedades = ["codebarra","nombre","categoria","marca","precio"]
                propiedad = input("Que desea modificar (codebarra, nombre, categoria, marca, precio): ").lower()
                while( propiedad not in propiedades):
                    print("Propiedad incorrecta \n")
                    propiedad = input("Que desea modificar (codebarra, nombre, categoria, marca, precio): ").lower()
                modificar_producto(propiedad,producto,bodega)
                se_encuentra = True
                print("Producto modificado \n")
               
        if (not se_encuentra):
            print("No se encuentra producto\n")

class Funcionario(Empleado):
    def __init__(self, nombre, rut, fechanac, usuario, contraseña):
        Empleado.__init__(self, nombre, rut, fechanac, usuario, contraseña)
        self.perfil = 'Funcionario'

    def ingresar_producto(self, bodega):
        se_encuentra = False
        codebarra = input("Ingrese codigo de barras: ")
        while (not codebarra.isdigit() or len(codebarra) < 1):
            print("tipo de dato ingresado incorrecto\n")
            codebarra = input("Ingrese codigo de barras: ")
        codebarra = int(codebarra)
        for producto in bodega.listaProductos:
            if producto.codebarra == codebarra:
                print("Producto ya existente\n")
                cantidad = input("Ingrese cantidad del producto agregar: ")
                while (not cantidad.isdigit() or int(cantidad) < 1 or int(cantidad) > producto.cantidad):
                    print("tipo de dato ingresado incorrecto o  cantidad superior máximo o menor a 0\n")
                    cantidad = input("Ingrese cantidad del producto agregar: ")
                cantidad = int(cantidad)
                producto.cantidad += cantidad
                print("Cantidad aumentada\n")
                se_encuentra = True
        if (not se_encuentra):
            print("Producto no encontrado, avisar administrador \n")


class Producto:
    def __init__(self, codebarra, nombre, categoria, marca, precio, cantidad):
        self.codebarra = codebarra
        self.nombre = nombre
        self.categoria = categoria
        self.marca = marca
        self.precio = precio
        self.cantidad = cantidad


class Usuarios:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self,empleado):
        if empleado not in self.empleados:
            self.empleados.append(empleado)
        else:
            print("Empleado ya se encuentra registrado\n")

    def eliminar_empleado(self,empleado):
        if empleado in self.empleados:
            self.empleados.append(empleado)
        else:
            print("Empleado no se encuentra registrado\n")

    def login(self, user, password):
        for empleado in self.empleados:
            if empleado.usuario == user and empleado.contrasena == password:
                print("Acceso concedido\n")
                return True
        print("Usuario o Contraseña incorrecto\ņ")
        return False

    def buscar_usuario(self, user, password):
        for empleado in self.empleados:
            if empleado.usuario == user and empleado.contrasena == password:
                return empleado