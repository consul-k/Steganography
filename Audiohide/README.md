# Audiohide

Audiohide is an audio steganography tool written in Python. It allows you to embed text messages into WAV audio files and extract them back.

## Features

- Embed text messages into WAV audio files
- Extract hidden messages from WAV audio files
- Simple command-line interface for easy usage

## Usage

1. Run the `audiohide.py` script
2. Choose an action from the menu:
   - Enter `1` to embed a message into an audio file
   - Enter `2` to extract a message from an audio file
   - Enter `0` to exit
3. Follow the prompts to enter the audio file name, message, and output file name (when embedding)

## Requirements

- Python 3.x
- `wave` library

## Supported Formats

- WAV (uncompressed PCM)

## Limitations

- The maximum length of the message that can be hidden depends on the size of the audio file. As a rule of thumb, you can embed approximately 1 character per 8 bytes of audio data. For example, a 1 MB WAV file can hold a message of around 131,072 characters.

This project is distributed under the MIT license. See the LICENSE file for details.
