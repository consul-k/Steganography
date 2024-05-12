import stepic
from PIL import Image

def encrypt(text, img_path):
    img = Image.open(img_path)
    img_stegano = stepic.encode(img, text.encode('utf-8'))
    img_stegano.save('stegano.png')

def decrypt(img_path):
    img = Image.open(img_path)
    decoded = stepic.decode(img)
    return decoded

# Main part
print('=' * 30)
print('   STEGANO-TOOL 3000   ')
print('=' * 30)

try:
    while True:
        mode = input('Enter mode (enc / dec / exit): ')
        if mode == 'exit':
            print('Exiting...')
            break
        elif mode == 'enc':
            print('-' * 30)
            text = input('Enter text to hide: ')
            img_path = input('Image to use: ')
            encrypt(text, img_path)
            print('-' * 30)
            print('Saved to stegano.png')
        elif mode == 'dec':
            print('-' * 30)
            img_path = input('Image to decipher: ')
            text = decrypt(img_path)
            print('-' * 30)
            print(f'Decoded text: {text}')
        else:
            print('Invalid mode! Please try again.')

        print('=' * 30)

except KeyboardInterrupt:
    print('Interrupted! Exiting...')
