# Caesar Cipher	2	 
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'		
MAX_KEY_SIZE = len(SYMBOLS)		
			
def getMode():		
    while True:		
        print('Encrypt, decrypt a message or break the cipher?')		
        mode = input().lower()		
        if mode in ['encrypt', 'e', 'decrypt', 'd', 'break', 'b']:		
            return mode		
        else:		
            print('Enter either "encrypt", or "e" or, "decrypt" or, "d", or "break", or "b".')		
		
def getMessage():		
    print('Enter your message:')		
    return input()		
		
def getKey():		
    key = 0		
    while True:		
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))		
        key = int(input())		
        if (key >= 1 and key <= MAX_KEY_SIZE):		
            return key		
		
def getTranslatedMessage(mode, message, key):		
    if mode[0] == 'd':		
        key = -key		
    translated = ''		
		
    for symbol in message:		
        symbolIndex = SYMBOLS.find(symbol)	
        # print("symbol =", symbol, "  index =", symbolIndex, "  key =", key)	
        if symbolIndex == -1: # Symbol not found in SYMBOLS.		
        # Just add this symbol without any change.		
            translated += symbol		
        else:		
            # Encrypt or decrypt		
            symbolIndex += key		
	
            if symbolIndex >= len(SYMBOLS):		
                symbolIndex -= len(SYMBOLS)		
            elif symbolIndex < 0:		
                symbolIndex += len(SYMBOLS)		

            translated += SYMBOLS[symbolIndex]		
    return translated		
		
mode = getMode()		
message = getMessage()
if mode != 'b':		
    key = getKey()
print('Your translated text is:')
if mode[0] != 'b':				
    print(getTranslatedMessage(mode, message, key))
else:
    with open('5000-words.txt') as file1:
        lines = []
        for line in file1:
            lines.append(line.replace("\n",""))

    # print(lines)
    # if a translated word with trial key is in the dictionary, print this line
    for key in range(1, MAX_KEY_SIZE + 1):
        text1 = getTranslatedMessage('d', message, key)
        split1 = text1.split()
        for i1 in split1:
            for l in lines:
                # if i1 == l:
                if i1.lower() == l.lower():
                    print("Word: ", i1, "key: ", key, " message: ", text1) 


           