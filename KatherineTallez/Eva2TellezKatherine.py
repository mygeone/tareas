class Eva2TellezKatherine:

    class Usuario:
        def __init__(self, tipo, usuario, password):
            self.tipo = tipo
            self.usuario = usuario
            self.password = password

    class Estudiante(Usuario):
        def __init__(self,tipo,usuario,password,carrera, asignatura, notas):
            
            super().__init__(tipo,usuario,password)

            self.carrera = carrera
            self.asignatura = asignatura
            self.notas = notas

        def visualizarNotas(self):
            print(self.notas)

        def revisarSituacion(self):
            try:
                    
                prom = 0
                for i in (self.notas):
                    prom = prom + i

                if( prom/len(self.notas) <= 3):
                    print('Reprobado')
                elif ( prom/len(self.notas) > 3 and  prom/len(self.notas) < 4.9):
                    print('Debe rendir examen')
                else:
                    print('Aprobado')
            except:
                print("El profesor debe ingresar notas primero")


    class Profesor(Usuario):
        def __init__(self,tipo,usuario,password):
            super().__init__(tipo,usuario,password)

        
        def ingresarDatos(self,alumno,notas):
            alumno.notas = notas
            
        
    profesor1 = Profesor('profesor',1,'password1')

    estudiante1 = Estudiante('alumno',1,'1111','Psicologia','Pensamiento I',[])
    estudiante2 = Estudiante('alumno',2,'2222','Informmatica','BDD',[])
    estudiante3 = Estudiante('alumno',3,'3333','Periodismo','Teoria I',[])

    carrera4 = input('Ingrese carreara del cuarto estudiante : ')
    asignatura4 = input('Ingrese asignatura del cuarto estudiante : ')
    carrera5 = input('Ingrese carreara del quinto estudiante : ')
    asignatura5 = input('Ingrese asignatura del quinto estudiante : ')

    estudiante4 = Estudiante('alumno',4,'4444',carrera4,asignatura4,[])
    estudiante5 = Estudiante('alumno',5,'5555',carrera5,asignatura5,[])
    estudiantes = [estudiante1,estudiante2,estudiante3,estudiante4,estudiante5]

    while(True):

        print(" ------------   Menu Principal: Ingrese el tipo de usuario ------------ ")
        print("1. Estudiante")
        print("2. Profesor")
        print("0. Salir")
        opcion = int(input())

        #login alumno
        
        if(opcion == 1):
            while(True):
                idAlumno = int(input("Ingrese ID Alumno : "))
                password = input("Ingrese password : ")

                for i in estudiantes:
                    if (i.usuario == idAlumno and i.password == password):
                        login = True
                        actual = i
                        break
                    else:
                        login = False
                
                if(login):
                    print("Acceso correcto")
                    print('----- Menu Estudiante --------')
                    while(True):
                            print('1. Visualizar Notas')
                            print('2. Revisar estado')
                            print('0. Salir')
                            opcion = int(input())
                            if(opcion == 0):
                                break
                            else:
                                if(opcion == 1):
                                    actual.visualizarNotas()
                                elif (opcion == 2):
                                    
                                    actual.revisarSituacion()
                else:
                    print("Intente nuevamente")
                    break
                
        #login profesor
        elif (opcion == 2):
                idProfesor = int(input("Ingrese ID Profesor: "))
                password = input("Ingrese password : ")
                if(profesor1.usuario == idProfesor and profesor1.password == password):
                    print(" Acceso correcto ")
                    print('----- Menu Profesor --------')
                    while(True):
                        print("Ingrese el numero del estudiante del cual desea ingresar sus notas")
                        print("0. Salir")
                        count = 0
                        for i in estudiantes:
                            count += 1
                            print("Estudiante",count,"- Carrera:",i.carrera," - Asignatura:",i.asignatura)
                        numero = int(input())
                        if(numero == 0):
                            break
                        else:
                            #estudianteObjetivo = estudiantes[numero]
                            print("Ingrese las notas del estudiante")
                            notasObjetivo = [0] * 3
                            for i in range(3):
                                notasObjetivo[i] = int(input())

                            estudiantes[numero-1].notas = notasObjetivo
                            estudiantes[numero-1].revisarSituacion()
                else:
                    print("Ingrese datos nuevamente")
        #salir
        elif (opcion == 0):
            break

Eva2TellezKatherine()