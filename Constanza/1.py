morseDict = {'.-': 'A',   '-...': 'B',   '-.-.': 'C',
       '-..': 'D',      '.': 'E',   '..-.': 'F',
         '--.': 'G',   '....': 'H',     '..': 'I',  
      '.---': 'J',    '-.-': 'K',   '.-..': 'L',
        '--': 'M',     '-.': 'N',    '---': 'O', 
      '.--.': 'P',   '--.-': 'Q',    '.-.': 'R',
       '...': 'S',      '-': 'T',    '..-': 'U', 
      '...-': 'V',    '.--': 'W',   '-..-': 'X',
      '-.--': 'Y',   '--..': 'Z', '': ' '}
print('Ingresa tu codigo morse', end = '')
morse = input()              
output = []
letter = []
control = -1
errorFlag = True
#print(morse.split(' '))

for i in morse.split(' '):
    control += 1
    letter += [i.split('/')]
    for k in range(len(letter[control])):
        if (letter[control][k] not in morseDict.keys()):
            error = letter[control][k]
            errorFlag = False
            break
        else:
            flag = True
            output += morseDict.get(letter[control][k])
            
if(errorFlag):
    print(''.join(output))
else:
    print('Error sintactico, el simbolo '+error+' no existe.')