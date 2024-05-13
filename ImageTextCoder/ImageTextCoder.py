import base64
import os

def encode_image(image_path, output_path):
    try:
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
    except FileNotFoundError:
        print(f"File {image_path} not found.")
        return

    image_data_base64 = base64.b64encode(image_data)

    with open(output_path, 'wb') as binary_file:
        binary_file.write(image_data_base64)

    print(f"Image {image_path} encoded to {output_path}")

def decode_image(txt_path, output_path):
    try:
        with open(txt_path, 'rb') as txt_file:
            image_data_base64 = txt_file.read()
    except FileNotFoundError:
        print(f"File {txt_path} not found.")
        return

    image_data = base64.b64decode(image_data_base64, validate=False)

    with open(output_path, 'wb') as image_file:
        image_file.write(image_data)

    print(f"File {txt_path} decoded to image {output_path}")

def main():
    while True:
        print("\nChoose an action:")
        print("1. Encode image to text")
        print("2. Decode text to image")
        print("3. Exit")

        choice = input("Enter the action number (1-3): ")

        if choice == '1':
            image_path = input("Enter the path to the image: ")
            output_path = input("Enter the name of the output text file: ")
            encode_image(image_path, output_path)
        elif choice == '2':
            txt_path = input("Enter the path to the text file: ")
            output_path = input("Enter the name of the output image: ")
            decode_image(txt_path, output_path)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

# Run the main program
if __name__ == "__main__":
    main()


# Example usage
#encode_image("image.png", "encoded.txt")
#decode_image("encoded.txt", "decoded_image.png")
