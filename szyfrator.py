alphabet = "abcdefghijklmnopqrstuvwxyz .?!,"
def char_to_index(char):
    for i in range(0,len(alphabet)):
        if char==alphabet[i]:
            return i

def add_key(key, text):
    j =0
    cipher = []
    for i in range(0, len(text)):
        cipher.append((char_to_index(text[i])+char_to_index(key[j]))%len(alphabet))
        j+=1
        if j>=len(key):
            j=0
    return cipher


while True:
    ch = raw_input("(p) Dzialanie na plikach\n(c) Dzialanie w konsoli\n(z) Zakoncz\n")
    if ch=='p':
        plaintext = open('text.txt').read()
        key = "drzwi"
        ciphertext = add_key(key, plaintext)
        file = open('result.txt', 'w')
        for i in range(0, len(ciphertext)):
            file.write(alphabet[ciphertext[i]])
        print("Rezultat zapisany do pliku result.txt")
        file.close()
    elif ch=='c':
        plaintext = raw_input("Podaj tekst do zaszyfrowania")
        key = "drzwi"
        ciphertext = add_key(key, plaintext)
        text=[]
        for i in range(0, len(ciphertext)):
            text.append(alphabet[ciphertext[i]])
        print(''.join(text))
    elif ch=='z':
        break

