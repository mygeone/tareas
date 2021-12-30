from os import path

def transaccion(cuenta,tipo,monto,fecha):

    if(tipo == 'DP'):
        if(path.exists('movimientos.csv')):
            movimientos = open('movimientos.csv','a')
            newLine = fecha+';'+cuenta+';'+str(monto)+';'+tipo+'\n'
            movimientos.write(newLine)
            movimientos.close()
            print('Movimiento DP registrado')
            return True
        else:
            print('Archivo no existe') 

    if(tipo == 'GA' or tipo == 'GC'):
        if(path.exists('cuentas.txt')):
            cuentas = open('cuentas.txt')
            lines = cuentas.readlines()
            for line in lines:
                datos = line.split(':')
                #verificamos si la cuenta es activa
                if(datos[1] == cuenta and int(datos[2].rstrip()) == 0):
                    print('Cuenta no activa')
                    return False
                elif(datos[1] == cuenta and int(datos[2].rstrip()) == 1):               
                    if(tipo == 'GC'):
                        movimientos = open('movimientos.csv','a')
                        newLine = fecha+';'+cuenta+';'+str(monto)+';'+tipo+'\n'
                        movimientos.write(newLine)
                        print('Movimiento GC registrado')
                        movimientos.close()
                    if(tipo == 'GA'):
                        #verificamos monto menor a 200.000 en transaccion
                        if monto>200000:
                            print('Movimiento GA no registrado: Monto excede maximo por transaccion de 200.000')
                            return False
                        #verificamos monto acumulada
                        else:
                            movimientos = open('movimientos.csv')
                            rows = movimientos.readlines()
                            montoAcumulado = 0
                            for linea in rows:
                                datos = linea.split(';')
                                if(datos[0] == fecha and datos[1] == cuenta):
                                    montoAcumulado += int(datos[2])
                            movimientos.close()
                            if(montoAcumulado + monto > 200000):
                                print('Movimiento GA no registrado: Monto excede maximo acumulado de 200.000 por dia')
                                return False
                            else:
                                movimientos = open('movimientos.csv','a')
                                newLine = fecha+';'+cuenta+';'+str(monto)+';'+tipo+'\n'
                                movimientos.write(newLine)
                                movimientos.close()
                                print('Movimiento GA registrado')
        else:
            print('Archivo no existe') 

def saldos(rut):
    if(path.exists('cuentas.txt')):
        cuentas = open('cuentas.txt')
        lines = cuentas.readlines()
        
        #guardamos las cuentas asociadas al rut
        saldos = {}
        for line in lines:
            datos = line.split(':')
            if(datos[0] == rut):
                saldos[datos[1]] = 0
        cuentas.close()
        #actualizamos saldos
        movimientos = open('movimientos.csv')
        rows = movimientos.readlines()
        for numCuenta in saldos.keys():
            saldoAcumulado = 0
            for linea in rows:
                datos = linea.split(';')
                if(datos[1] == numCuenta):
                    if(datos[3].rstrip() == 'GA' or datos[3].rstrip() == 'GC'):
                        saldoAcumulado -= int(datos[2])
                    elif(datos[3].rstrip() == 'DP'):
                        saldoAcumulado += int(datos[2])
            saldos[numCuenta] = saldoAcumulado
        movimientos.close()
        return saldos    
    else:
        print('Archivo no encontrado!')

def cartola(cuenta,fecha1,fecha2):
    #guardamos la fecha menor y mayor
    fecha1 = fecha1.split('-')
    fecha2 = fecha2.split('-')
    f1 = (int(fecha1[1]),int(fecha1[0]))
    f2 = (int(fecha2[1]),int(fecha2[0]))
    if(f1>f2):
        mayor = f1
        menor = f2
    else:
        mayor = f2
        menor = f1
    
    
    if(path.exists('cuentas.txt')):
        movs = open('movimientos.csv')
        lines = movs.readlines()

        nuevoRegistro = open(cuenta+'.txt','w')
        id = 0
        saldoAcumulado = 0

        for line in lines:
            id += 1
            datos = line.split(';')
            if(cuenta == datos[1]):
                saldoAcumulado += int(datos[2])
                tempf3 = datos[0].split('-')
                fechaTransaccion =  (int(tempf3[1]),int(tempf3[0]))
                if ( mayor > fechaTransaccion > menor):
                    escribir = str(id)+' '+datos[0]+' '+datos[2]+' '+datos[3].rstrip()+'\n'
                    print(escribir)
                    nuevoRegistro.write(escribir)
        nuevoRegistro.close()
        movs.close()
        return saldoAcumulado

#transaccion('1234-5678-8765-4321','DP',20000,'01-01-2020')
#print(cartola('1234-5678-8765-4321', '01-01-2020', '30-01-2020'))
#print(saldos('12367266K'))