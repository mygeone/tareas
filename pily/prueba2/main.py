from clases import (
    Bodega,
    Administrador,
    Funcionario,
    Producto,
    Usuarios
)
from funciones import  *
# DATOS INCIALES
bodega_centra = Bodega(0,"Puq","Henrique Abello",11,"joana")
gestorUsuarios = Usuarios()
admin1 = Administrador("2073445243-5","jana","22-05-2001","j", "j")
fun1 = Funcionario("18906791-2","Flavia","25-12-1998","f", "f")
gestorUsuarios.agregar_empleado(admin1)
gestorUsuarios.agregar_empleado(fun1)
p1 = Producto(1234,"leche","cereal","líder",3500,7)
p2 = Producto(1235,"chocolate","arroz","nestle",1000,8)
p3 = Producto(1236,"néctar","agua","bebida",750,2)
bodega_centra.cantidad = 3
bodega_centra.listaProductos = [p1,p2,p3]

#PRUEBA
salir = False
while(not salir):
    usuario, contrasena = solicitar_datos()
    if(gestorUsuarios.login(usuario,contrasena)):
        empleado = gestorUsuarios.buscar_usuario(usuario,contrasena)
        if empleado.perfil == 'Administrador':
            salir_admin = False
            while(not salir_admin):
                opcion = menu_item_admin()
                if opcion == 7:
                    salir_admin = True
                elif opcion == 6:
                    bodega_centra.informe_ventas()
                elif opcion == 5:
                    bodega_centra.informe_bodega()
                elif opcion == 4:
                    empleado.eliminar_producto(bodega_centra)
                elif opcion == 3:
                    empleado.modificar_producto(bodega_centra)
                elif opcion == 2:
                    empleado.sacar_producto(bodega_centra)
                elif opcion == 1:
                    empleado.ingresar_producto(bodega_centra)
                else:
                    print("Opción no valida\n")
        else:
            salir_fun = False
            while(not salir_fun):
                opcion = menu_item_fun()
                if opcion == 2:
                    salir_fun = True
                elif opcion == 1:
                    empleado.ingresar_producto(bodega_centra)
                else:
                    print("Opción no valida\n")

    else:
        opc = input("Desea volver a intentar?  1.-Sí 2.-No: ")
        while( opc != "1" and opc != "2"):
            print("Opción incorrecta\n")
            opc = input("Desea salir?  1.-Sí 2.-No: ")
        if opc == "2":
            salir = True
