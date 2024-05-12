StegoPy is a steganography tool for hiding text messages within images. The program allows both embedding text into an image (encryption mode) and extracting previously hidden text (decryption mode).

The application supports a wide range of image formats, including PNG, JPEG, GIF, BMP, and others, thanks to the Pillow library (see Pillow documentation for a full list of supported formats).

StegoPy requires Python 3 and the Stepic and Pillow (PIL) libraries to run. You can install them using the following commands:
```
pip install stepic
pip install pillow
```

All the necessary dependencies are listed in the requirements.txt file. To install them, simply run:

```
pip install -r requirements.txt
```

To use StegoPy, download the StegoPy.py file and run it:
```
python StegoPy.py
```
Then follow the on-screen instructions.

When launched, the program will prompt you to select a mode: encryption (enc), decryption (dec), or exit.
In encryption mode, enter the text to hide and the path to the image. The result will be saved to the stegano.png file.
In decryption mode, just specify the path to the image with hidden text. The program will display the hidden message on the screen.

The size of the text that can be hidden in an image depends on the size of the image itself. For best results, it is recommended to use sufficiently large, high-resolution images.

This project is distributed under the MIT License. See the LICENSE file for more details.
