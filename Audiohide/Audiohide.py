import wave
import struct

def embed_message(audio_file, message, output_file):
    # Open the WAV file and get parameters
    with wave.open(audio_file, 'rb') as wav:
        params = wav.getparams()
        audio_data = wav.readframes(wav.getnframes())

    # Add end-of-message marker
    message += '\x00\x00\x00'

    # Convert the message to bits
    message_bits = ''.join(format(ord(i), '08b') for i in message)

    # Embed message bits into audio data
    sample_width = params.sampwidth
    num_channels = params.nchannels
    embedded_data = bytearray(audio_data)
    for i, bit in enumerate(message_bits):
        byte_index = i * sample_width * num_channels
        embedded_data[byte_index] = (embedded_data[byte_index] & 254) | int(bit)

    # Save the modified WAV file
    with wave.open(output_file, 'wb') as wav:
        wav.setparams(params)
        wav.writeframes(embedded_data)

def extract_message(stego_file):
    # Open the stego WAV file and get parameters
    with wave.open(stego_file, 'rb') as wav:
        params = wav.getparams()
        audio_data = wav.readframes(wav.getnframes())

    # Calculate the number of embedded bits
    sample_width = params.sampwidth
    num_channels = params.nchannels
    max_message_bits = len(audio_data) // (sample_width * num_channels) * 8

    # Extract message bits from audio data
    extracted_bits = [str((audio_data[i * sample_width * num_channels] & 1)) for i in range(max_message_bits // 8)]
    message_bits = ''.join(extracted_bits)

    # Extract characters until the end-of-message marker
    message_chars = []
    for i in range(0, len(message_bits), 8):
        char = chr(int(message_bits[i:i+8], 2))
        if char == '\x00' and ''.join(message_chars[-2:]) == '\x00\x00':
            break
        message_chars.append(char)
    message = ''.join(message_chars)

    return message.rstrip('\x00')


# Dictionary with functions
menu_functions = {
    '1': embed_message,
    '2': extract_message
}

while True:
    print("\nMenu:")
    print("1. Embed message into audio file")
    print("2. Extract message from audio file")
    print("0. Exit")

    choice = input("Choose an action: ")

    if choice == '0':
        print("Goodbye!")
        break
    elif choice in menu_functions:
        if choice == '1':
            audio_file = input("Enter the name of the audio file: ")
            message = input("Enter the message to embed: ")
            output_file = input("Enter the name of the output file (default 'output.wav'): ")
            if not output_file:
                output_file = 'output.wav'
            menu_functions[choice](audio_file, message, output_file)
            print("Message successfully embedded into the audio file!")
        else:
            stego_file = input("Enter the name of the stego audio file: ")
            extracted_message = menu_functions[choice](stego_file)
            print("Extracted message:", extracted_message)
    else:
        print("Invalid choice. Please try again.")
