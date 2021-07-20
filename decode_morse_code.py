
def decode_bits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bits = bits.replace('11','1').replace('00','0')
    return bits.replace('111', '-').replace('0000000','\t').replace('000', ' ').replace('1', '.').replace('0', '')

def decode_morse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    print("line 8",morseCode)

    morseCode = morseCode.split(' ')
    print("line 12 ",morseCode)
    result= []
    for i in morseCode:
        if "\t" in i:
            #index = i.index('\t')
            i = i.split("\t")
            for m in i:
                if(i.index(m))
                result.append(MORSE_CODE[i[m]])
            result.append("\t")
            
            for n in i:
                
            print("line 13",result)
            
            continue
       
        result.append(MORSE_CODE[i])
        print("line 11",i,MORSE_CODE[i],result)

    return "".join(map(str,result))
#11001100110011 >>> uh,j/hdwqH 

ugbj