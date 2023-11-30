

![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=daitohck&theme=dark&show_icons=true)
Encryption and Decryption Scripts using Fernet

These Python scripts provide a simple implementation of file encryption and decryption using the Fernet symmetric key encryption algorithm from the cryptography library.
Encryption Script (encrypt.py)

This script encrypts files in a specified directory using Fernet encryption.


Prerequisites

Ensure that you have the cryptography library installed:


    pip install cryptography


Usage

Open the encrypt.py file.

Locate the following line and replace #PATH with the absolute path to the directory containing the files you want to encrypt:

python

path_to_encrypt = '#PATH'

Save the file.

Run the script:

    python encrypt.py


Follow the prompts to complete the encryption process.

The script will generate a key (key.key), encrypt all files in the specified directory, and create a readme.txt file with instructions.

Note: Make sure to run the encrypt.py script before attempting to decrypt with decrypt.py.

Feel free to contact me for further assistance or if you encounter any issues.
