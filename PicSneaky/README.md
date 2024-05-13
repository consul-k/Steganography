## 🏴‍☠️ PicSneaky - a steganography utility

PicSneaky is a console utility that allows you to hide any files inside JPEG images, and then extract them back. Perfect when you need to conceal important information from prying eyes! 👀

### How to use

1. Install dependencies: `pip install treasure-image`
2. Run the PicSneaky.py script
3. Follow the instructions in the interactive menu
4. To hide a file - specify an image (JPEG format) and the file you want to hide
5. To find a file - specify the image to search. By default, the file is called "treasure", but you can set your own name.

### Dependencies
- Python 3.x
- treasure-image library

Install the treasure-image library using pip:
```
pip install treasure-image
```

### Notes
- The size of the hidden file is limited by the size of the "container" image. Very large files may not fit.
- The extracted file will be created in the same folder where the image is located.
- Hide files at your own risk! The author is not responsible for possible data loss.

This project is distributed under the MIT license. See the LICENSE file for more details.
