from usuario_dao import UsuarioDao
from usuario import Usuario
from os import system
system('cls')

usuario = UsuarioDao()

#Verificar existencia de tabla
opc = usuario.validarExistenciaTabla()
if opc==1:
    print(usuario.eliminarTablaUsuario())
    print()
    print(usuario.crearTablaUsuario())
    print()
else:
    print(usuario.crearTablaUsuario())
    print()

#Crear productos
u1 = Usuario('1', 'psalas', '123')
u2 = Usuario('2', 'mtorres', '123')
u3 = Usuario('3', 'aaraneda', '123')
u4 = Usuario('4', 'jlopez', '123')
u5 = Usuario('5', 'kduran', '123')

print(usuario.insertarUsuario(u1))
print()
print(usuario.insertarUsuario(u2))
print()
print(usuario.insertarUsuario(u3))
print()
print(usuario.insertarUsuario(u4))
print()
print(usuario.insertarUsuario(u5))
print()

#Buscar usuario
id=int(input('Indique un ID de usuario a buscar: '))
u = usuario.buscarUsuario(id)

if u!=None:
    print()
    print('Los datos del usuario son Usuario: ',u.usuario,' Password: ',u.password)
    print()
else:
    print('Usuario no encontrado')
    print()

#Eliminar usuario
id=int(input('Indique un ID de usuario a eliminar: '))
print()
print(usuario.eliminarUsuario(id))
print()

#Editar un usuario
id=int(input('Indique un ID de usuario a editar: '))
u = usuario.buscarUsuario(id)

if u!=None:
    print('Los datos del usuario son Usuario: ',u.usuario,' password: ',u.password)
    nuevousuario=input('Indique un nombre de usuario: ')
    password=input('Indique el nuevo password: ')
    print(usuario.actualizarUsuario(id,nuevousuario,password))
    print()
else:
    print('Usuario no encontrado')    

#Mostrar los usuarios
usuario.obtenerUsuarios()
print()