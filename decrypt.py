from cryptography.fernet import Fernet
import os

def decrypt(fullpath):
  with open('key.key', 'r') as file:
    key=file.read()
    f=Fernet(key)
    with open(fullpath, 'rb') as f2:
      content=f.decrypt(f2.read())
    print(content)
    with open(fullpath, 'wb') as f2:
      f2.write(content)

if __name__ == '__main__':
    path_to_encrypt = '#PATH'

    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt + '/' + item for item in items if item!='readme.txt']
    print(full_path)
    for i in full_path:
      decrypt(i)

with open(path_to_encrypt + '/readmev2.txt', 'w') as file:
    file.write('Data decrypted \n')
    file.write('it was a pleasure')
