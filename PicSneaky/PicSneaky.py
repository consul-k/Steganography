import os
import imghdr
from treasure_image import PIRATE, EXPLORER

def main():
    print(r''' _____   _         _____                      _
|  __ \ (_)       / ____|                    | |
| |__) | _   ___ | (___   _ __    ___   __ _ | | __ _   _
|  ___/ | | / __| \___ \ | '_ \  / _ \ / _` || |/ /| | | |
| |     | || (__  ____) || | | ||  __/| (_| ||   < | |_| |
|_|     |_| \___||_____/ |_| |_| \___| \__,_||_|\_\ \__, |
                                                     __/ |
                                                    |___/
''')
    while True:
        print("What do you want to do?")
        print("1. Hide a file in an image")
        print("2. Find a hidden file in an image")
        print("3. Exit")

        choice = input("Enter 1, 2 or 3: ")

        if choice == "1":
            pic = input('IMAGE TO HIDE IN: ')
            file = input('FILE TO HIDE: ')
            if os.path.exists(pic) and os.path.exists(file):
                if imghdr.what(pic) == 'jpeg':
                    PIRATE.hide_file_treasure(image=pic, treasure=file)
                else:
                    print("Error: the picture must be in .jpg format!")
            else:
                print("Error: The specified file does not exist!")
        elif choice == "2":
            pic = input('IMAGE TO SEARCH: ')
            if os.path.exists(pic):
                name = input('FILE NAME (default is "treasure"): ') or "treasure"
                f = input('FILE FORMAT (default is "text"): ') or "text"
                EXPLORER.seek_file_treasure(image=pic, treasure_name=name, treasure_format=f)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
