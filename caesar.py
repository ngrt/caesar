en = 'abcdefghijklmnopqrstuvwxyz'
ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def reset():
    res = str(input("Do you want to start again? y/n\n"))
    if res == "y":
        print('Restarting...')
        main()
    else:
        print()

print('Welcome to Caesar Cipher decrypter.')

def main():
    key = int(input('\nTo start type your "Key"\n'))
    lng = input('Now choose language of your text for proper working (ru/en)\n')
    if lng == 'en':
        alphabet = en
    if lng == 'ru':
        alphabet = ru
    
    text = str(input('Now type your text\n'))
    cipher = ""
    for char in text:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            new_index = (index - key) % len(alphabet)
            new_char = alphabet[new_index]
            if char.isupper():
                new_char = new_char.upper()
            cipher += new_char
        else:
            cipher += char
    print('\nDecrypted text:\n', cipher)
    reset()
main()