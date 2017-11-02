#################################################
#                                               #
# Based on Al Sweigart's Python Vigenere Cipher #
#                                               #
#################################################

# Requires stepic and image libraries for stegenography

import random, os, Image, stepic, time, string

LETTERS = string.printable

while True:

    def main():

        print ' '
		
        myMessage = raw_input('>>:Enter Message (Blank For Decrypting): ')
        
        myMode = raw_input('>>:Mode(Lock, Unlock): ')
	
        if myMode == 'Lock': # set to 'Lock' or 'Unlock'

            rnd = random.SystemRandom()
            myKey = ''.join((rnd.choice(LETTERS) for i in range(len(myMessage)))) # Generates random key of same length as message to be encrypted

            pic = raw_input('>>:Enter Image Name: ') # Name of image file to hide encryption key
            im1 = Image.open(pic)
            im2 = stepic.encode(im1, myKey)
            im2.save('Lock.png','PNG')
            
            print '>>:Key Completed.'
            print '>>:File Locked.'
            print '>>:Press Ctrl + C to Quit.\n'
            print '=' * 60
            print ' '
            time.sleep(3)
            os.system('clear')

            translated = encryptMessage(myKey, myMessage)
            file = open("Encrypted.txt", "w")
            file.write(translated)
            file.close()

            if os.path.isfile('Decrypted.txt'):
                os.remove('Decrypted.txt')
            
        elif myMode == 'Unlock':
            
            file = open("Encrypted.txt") # Reads from 'Encrypted.txt' to begin decryption
            myMessage = file.read()

            im0 = Image.open('Lock.png')
            s = stepic.decode(im0)
            myKey = s.decode()
            
            translated = decryptMessage(myKey, myMessage)
            print '>>:Decrypted Message Saved'
            print '>>:Press Ctrl + C to Quit.\n'
            print '=' * 60
            print ' '
            time.sleep(3)
            os.system('clear')

            file = open("Decrypted.txt", "w")
            file.write(translated)
            file.close()

            os.remove("Encrypted.txt") # Deletes encrypted.txt file after decryption

    def encryptMessage(key, message):
        return translateMessage(key, message, 'Lock')


    def decryptMessage(key, message):
        return translateMessage(key, message, 'Unlock')


    def translateMessage(key, message, mode):
        translated = [] # stores the encrypted/decrypted message string

        keyIndex = 0

        for symbol in message: # loop through each character in message
            num = LETTERS.find(symbol)
            if mode == 'Lock':
                num += LETTERS.find(key[keyIndex]) # add if encrypting
            elif mode == 'Unlock':
                num -= LETTERS.find(key[keyIndex]) # subtract if decrypting

            num %= len(LETTERS) # handle the potential wrap-around

            # add the encrypted/decrypted symbol to the end of translated.
            symbol = translated.append(LETTERS[num])

            keyIndex += 1 # move to the next letter in the key
            if keyIndex == len(key):
                keyIndex = 0

        return ''.join(translated)

    if __name__ == '__main__':
        main()
