from cryptography.fernet import Fernet
import subprocess
import sys


class Crypt():
  def __init__(self, key=None):
    self.keyName = ""
    self.key = None
  
  def activate(self, keyname):
    try:
      with open(keyname, 'rb') as filekey:
        self.key = filekey.read()
        self.keyName = keyname
    except:
      raise "Invalid filename to the keyfile"


  def keygen(self, keyname):
    key = Fernet.generate_key()
    with open(keyname, 'wb') as filekey:
      filekey.write(key)

  def encode(self, path):
    out = subprocess.check_output(["ls", "-A1", path])
    files = out.decode('UTF-8').split('\n')
    files = [line for line in files if line.strip()]

    for fileName in files:
      # feeding the key
      fernet = Fernet(self.key)
      filePath = "".join([path,fileName])

      with open(filePath, 'rb') as file:
        content = file.read()

      encrypted = fernet.encrypt(content)

      with open(filePath, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


  def decode(self, path):
    if not self.key:
      raise "Activate first . . . . ."
    out = subprocess.check_output(["ls", "-A1", path])
    files = out.decode('UTF-8').split('\n')
    files = [line for line in files if line.strip()]

    for fileName in files:
      # feeding the key
      fernet = Fernet(self.key)
      filePath = "".join([path,fileName])

      with open(filePath, 'rb') as file:
        content = file.read()

      decrypted = fernet.decrypt(content)

      with open(filePath, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)



if __name__ == '__main__':
  if len(sys.argv) < 2:
    raise "Please provide arguments"
  
  cp = Crypt()
  cp.activate("secret.key")

  if sys.argv[1] == "encode":
    cp.encode("./data/") # path to the folder that contains files to be encrypted
  elif sys.argv[1] == "decode":
    cp.decode("./data/") # path to the folder that contains files to be encrypted
  elif sys.argv[1] == "keygen":
    cp.keygen('secret.key')
    