#Jacob Hopkins
#7/18/2017
#rotates alphabet n and encrypts data using scale
#rotN
#Assignment 2

def rotateAlphabet(shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet =""
    for ch in alphabet:
        newIdx = ord(ch) + shift
        if newIdx > ord('z'):
                newIdx -= 26
        newLetter = chr(newIdx)
        shifted_alphabet += newLetter
    return shifted_alphabet
        

def rotNEncrypt(plainText, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newAlphabet = rotateAlphabet(shift)
    cipherText = ""
    for ch in plainText:
        if(ch==' '):
            cipherText += ' '
        elif(ch in alphabet):
            idx = alphabet.find(ch)
            newLetter = newAlphabet[idx]
            cipherText = cipherText + newLetter
        else:
            cipherText += ch
            print('rot13 tried to implement a character not registered')
    return cipherText

def rotNDecrypt(plainText, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newAlphabet = rotateAlphabet(26-shift)
    cipherText = ""
    for ch in plainText:
        if(ch==' '):
            cipherText += ' '
        elif(ch in alphabet):
            idx = alphabet.find(ch)
            newLetter = newAlphabet[idx]
            cipherText = cipherText + newLetter
        else:
            cipherText += ch
            print('rot13 tried to implement a character not registered')
    return cipherText

#Python v2.7.6
#IDLE v2.7.6
#Windows 10
#No additional libraries
