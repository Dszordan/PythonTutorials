# Caesar Cipher

MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message or brute force?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d brute b force'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

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
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

def bruteForce(message):
    for i in range(26):
        for l in message:
            num = ord(l)
            num += i
            if l.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif l.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
                
            print(chr(num), end='')
        print()

mode = getMode()
message = getMessage()
if mode[0] == 'b':
    bruteForce(message)
else:
    key = getKey()
    print('Your translated text is:')
    print(getTranslatedMessage(mode, message, key))


