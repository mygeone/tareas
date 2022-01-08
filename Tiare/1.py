def dias_con_restriccion(digitos,ppu):

    res = list()

    digito = int(ppu[5])

    for key in digitos.keys():
        for number in digitos[key]:
            if digito == number:
                res.append(key)

    return res
a
digitos = {
    'lunes' : [6,4,3],
    'martes' : [6,1,3],
    'lunes' : [6,8,3],
    'lunes' : [6,4,1],

}

print(dias_con_restriccion(digitos,"ABCD56"))