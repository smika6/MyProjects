#Jacob Hopkins
#7/18/2017
#rot13 encryption
#rot13.py
#Assignment 2
def rot13(plainText):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rot13Alphabet = "nopqrstuvwxyzabcdefghijklm"
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText:
        if(ch==' '):
            cipherText += ' '
        elif(ch in alphabet):
            idx = alphabet.find(ch)
            newLetter = rot13Alphabet[idx]
            cipherText = cipherText + newLetter
        else:
            cipherText += ch
            print('rot13 tried to implement a character not registered')
    return cipherText

#Python v2.7.6
#IDLE v2.7.6
#Windows 10
#No additional libraries
