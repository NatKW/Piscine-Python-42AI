import sys
               
Morse_Dico = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
     
if len(sys.argv) < 2:
    sys.exit()

Msg = [arg.upper() for arg in sys.argv[1:]]
Morse_msg = []

try:
    for arg in Msg:
        Morse_msg.append(" ".join([Morse_Dico[letter] for letter in arg]))
    Morse_msg = " / ".join(Morse_msg)
    print(Morse_msg)
except KeyError:
    print('ERROR')
    exit()