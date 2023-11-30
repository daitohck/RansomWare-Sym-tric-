Encryption and Decryption Scripts using Fernet

These Python scripts provide a simple implementation of file encryption and decryption using the Fernet symmetric key encryption algorithm from the cryptography library.
Encryption Script (encrypt.py)

This script encrypts files in a specified directory using Fernet encryption.


Prerequisites

Ensure that you have the cryptography library installed:

bash

pip install cryptography


Usage

    Open the encrypt.py file.

    Locate the following line and replace #PATH with the absolute path to the directory containing the files you want to encrypt:

    python

path_to_encrypt = '#PATH'

Save the file.

Run the script:

bash

    python encrypt.py

    Follow the prompts to complete the encryption process.

    The script will generate a key (key.key), encrypt all files in the specified directory, and create a readme.txt file with instructions.

Decryption Script (decrypt.py)

This script decrypts files previously encrypted by the encrypt.py script.
Prerequisites

Ensure that you have the cryptography library installed:

bash

pip install cryptography

Usage

    Open the decrypt.py file.

    Locate the following line and replace #PATH with the absolute path to the directory containing the encrypted files:

    python

path_to_encrypt = '#PATH'

Save the file.

Run the script:

bash

    python decrypt.py

    Follow the prompts to complete the decryption process.

    The script will read the key from key.key and decrypt all files in the specified directory. It will create a readmev2.txt file with decryption completion information.

Note: Make sure to run the encrypt.py script before attempting to decrypt with decrypt.py.

Feel free to contact me for further assistance or if you encounter any issues.
