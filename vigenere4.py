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
    keyArr = []
    for i in range(0,2):
        flag = True	
        while flag==True:		
            print('Enter key', i, ' (number from 1-%s):' % (MAX_KEY_SIZE))		
            key = int(input())		
            if (key >= 1 and key <= MAX_KEY_SIZE):		
                keyArr.append(key)
                flag = False
    print('keyArr: ', keyArr)             
    return keyArr              		
		
def getTranslatedMessage(mode, message, keyArr):			
    translated = ''		

    i = 0
    for symbol in message:	
        if i>= len(keyArr):
            i = 0
        key = keyArr[i] 
        if mode[0] == 'd':		
            key = -key    
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
    keyArr = getKey()
print('Your translated text is:')
if mode[0] != 'b':				
    print(getTranslatedMessage(mode, message, keyArr))
else:
    with open('5000-words.txt') as file1:
        lines = []
        for line in file1:
            lines.append(line.replace("\n",""))
    for key1 in range(1, MAX_KEY_SIZE + 1):
        for key2 in range(1, MAX_KEY_SIZE + 1):
            keyArrTest = [key1, key2] 
            text1 = getTranslatedMessage('d', message, keyArrTest)
            split1 = text1.split()
        for i1 in split1:
            for l in lines:
                # if i1 == l:
                if i1.lower() == l.lower():
                    print("Word: ", i1, "keys: ", keyArrTest, " message: ", text1) 