alphabet = "abcdefghijklmnopqrstuvwxyz .?!,"
print(len(alphabet))

def char_to_index(char):
    for i in range(0,len(alphabet)):
        if char == alphabet[i]:
            return i


def decipher(key, cipher_text):
    j = 0
    text = []
    for i in range(0, len(cipher_text)):
        if char_to_index(cipher_text[i])>=char_to_index(key[j]):
            text.append(char_to_index(cipher_text[i])-char_to_index(key[j]))
        else:
            text.append(len(alphabet)-abs(char_to_index(cipher_text[i])-char_to_index(key[j]))%len(alphabet))
        j+=1

        if j>=len(key):
            j=0

    return text

while True:
    ch = input("(p) Dzialanie na plikach\n(c) Dzialanie w konsoli\n(z) Zakoncz\n")
    if ch=='p':
        ct = open('result.txt').read()
        k = open('key.txt').read()
        dec=decipher(k,ct)
        file = open('decipher_result.txt', 'w')
        for i in range(0,len(dec)):
            print(dec[i])
            file.write(alphabet[dec[i]])
        print("Operacja zakonczona")
        file.close()
    elif ch=='c':
        ct=input("Podaj zaszyfrowany tekst")
        k=input("Podaj klucz")
        dec = decipher(k, ct)
        text = []
        for i in range(0, len(dec)):
            text.append(alphabet[dec[i]])
        print(''.join(text))
    elif ch=='z':
        break
