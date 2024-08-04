letters= 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if letter != ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = (index + key) % num_letters
                ciphertext += letters[new_index]
        else:
            ciphertext += ' '
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if letter != ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = (index - key) % num_letters
                plaintext += letters[new_index]
        else:
            plaintext += ' '
    return plaintext

def menu():
    print()
    print('CEASER CIPHER PROGRAM:-')
    print()
    print('1. Encrypt')
    print('2. Decrypt')
    print('3. Quit')
    print()
    choice = input('Enter your choice: ')
    return choice

while True:
    choice = menu()
    
    if choice == '1':
        print('ENCRYPTION MODE SELECTED')
        key = int(input('Enter key (1-26): '))
        if key > 26 or key < 1:
            print('Invalid key')
            continue
        
        text = input('Enter text to encrypt: ').lower()
        ciphertext = encrypt(text, key)
        print('CIPHERTEXT:', ciphertext)
    
    elif choice == '2':
        print('DECRYPTION MODE SELECTED')
        key = int(input('Enter key (1-26): '))
        if key > 26 or key < 1:
            print('Invalid key')
            continue
        
        text = input('Enter text to decrypt: ').lower()
        plaintext = decrypt(text, key)
        print('PLAINTEXT:', plaintext)
    
    elif choice == '3':
        print('Exiting...')
        break
    
    else:
        print('Invalid choice. Please enter a number between 1 and 3.')
