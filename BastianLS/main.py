'''
Utilizadas para calcular la division
'''
def gcd(n, m):
    d =  min (n,    m)
    while   n %  d  !=   0  or  m  %  d  !=   0:
        d =  d  -  1
    return d
    
def reduce (num, den):
    if num == 0:
        return  (0,   1)
    elif num<0:
        g =  gcd(abs(num),      den)
        return  (num    //  g,   den   //  g)
    elif den<0:
        g =  gcd(num,      abs(den))
        return  (num    //  g,   den   //  g)
    else:
        g =  gcd(num,      den)
        return  (num    //  g,   den   //  g)


def solveFrac(frac): #12/5
    indexOfOperator = frac.find('/')
    num1 = frac[:indexOfOperator]
    num2 = frac[indexOfOperator+1:]
    return reduce(int(num1),int(num2))

    
'''
Toma una operacion de la forma (a/b x c/d) y la reduce

str => str

'(12/5 x 6/4)' =>  '18/5' 

'''
def solvePharMult(term):
    eqTemp = term.replace('(','')
    eqDef = eqTemp.replace(')','')
    splitted = eqDef.split(' x ')
    terms = 0
    num1str = solveFrac(splitted[terms])
    num2str = solveFrac(splitted[terms+1])
    f1 = num1str[0]*num2str[0]
    f2 = num1str[1]*num2str[1]
    result =  reduce(f1,f2)
    return str(result[0])+'/'+str(result[1])

'''
Toma una operacion de la forma (a/b - c/d) y la reduce

str => str

'(12/5 - 6/4)' =>  '9/10' 

'''
def solvePharSust(term):
    eqTemp = term.replace('(','')
    eqDef = eqTemp.replace(')','')
    splitted = eqDef.split(' - ')
    terms = 0
    num1str = solveFrac(splitted[terms])
    num2str = solveFrac(splitted[terms+1])
    f1 = abs(num1str[0]*num2str[1] - num1str[1]*num2str[0])
    f2 = abs(num1str[1]*num2str[1])
    result = reduce(f1,f2)
    return str(result[0]*-1)+'/'+str(result[1])

'''
Toma una operacion de la forma (a/b + c/d) y la reduce

str => str

'(12/5 x 6/4)' =>  '39/10' 

'''
def solvePharAdd(term):
    eqTemp = term.replace('(','')
    eqDef = eqTemp.replace(')','')
    splitted = eqDef.split(' + ')
    terms = 0
    num1str = solveFrac(splitted[terms])
    num2str = solveFrac(splitted[terms+1])
    f1 = (num1str[0]*num2str[1] + num1str[1]*num2str[0])
    f2 = (num1str[1]*num2str[1])
    result =  reduce(f1,f2)
    return str(result[0])+'/'+str(result[1])

'''
Toma una operacion de la forma (a/b : c/d) y la reduce

str => str

'(12/5 x 6/4)' =>  '8/5' 

'''
def solvePharDiv(term):
    eqTemp = term.replace('(','')
    eqDef = eqTemp.replace(')','')
    splitted = eqDef.split(' : ')
    terms = 0
    num1str = solveFrac(splitted[terms])
    num2str = solveFrac(splitted[terms+1])
    print(num1str,num2str)
    f1 = num1str[0]*num2str[1]
    f2 = num1str[1]*num2str[0]
    result =  reduce(f1,f2)
    return str(result[0])+'/'+str(result[1])

'''
Retorna una lista con los indices dado un element
'''
    def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)



eq = ' (5/6 + -4/8) x (9/5 ? (12/5 x 6/4))'


parentesisIndexOpen = indices(eq,'(')
parentesisIndexClose = indices(eq,')')

size = len(parentesisIndexOpen)
#3

#print(eq[parentesisIndexOpen[2]:parentesisIndexClose[2]])
#(12/5 x 6/4)

#print(solvePharMult(eq[parentesisIndexOpen[2]:parentesisIndexClose[2]]))
#18/5

while(size != 0):
    size -= 1
    print(size)
    print(eq[ parentesisIndexOpen[size]:parentesisIndexClose[size]])

print("hay ",len(indices(eq,'(')),'indices')
