from cryptography.fernet import Fernet
import subprocess
import argparse

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

  def encode(self, path, isDir):
    if not self.key:
      raise "Activate first . . . . ."

    files = []
    if isDir:
      out = subprocess.check_output(["ls", "-A1", path])
      files.extend(out.decode('UTF-8').split('\n'))
      files = [line for line in files if line.strip()]
    else:
      files.append(path)

    for fileName in files:
      # feeding the key
      fernet = Fernet(self.key)
      filePath = "".join([path,fileName]) if isDir else f"./{path}"

      with open(filePath, 'rb') as file:
        content = file.read()

      encrypted = fernet.encrypt(content)

      with open(filePath, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


  def decode(self, path, isDir):
    if not self.key:
      raise "Activate first . . . . ."

    files = []
    if isDir:
      out = subprocess.check_output(["ls", "-A1", path])
      files.extend(out.decode('UTF-8').split('\n'))
      files = [line for line in files if line.strip()]
    else:
      files.append(path)

    for fileName in files:
      # feeding the key
      fernet = Fernet(self.key)
      filePath = "".join([path,fileName]) if isDir else f"./{path}"

      with open(filePath, 'rb') as file:
        content = file.read()

      decrypted = fernet.decrypt(content)

      with open(filePath, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)



if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  parser.add_argument("-a", "--action", help="Action to perform (encode / decode / keygen)")
  parser.add_argument("-f", "--file", help="file to be processed")
  parser.add_argument("-d", "--directory", help="directory to be processed")
  args = parser.parse_args()

  # checking args
  if args.file and args.directory:
    raise "Target must be either a file or a directory, but both are specified."
  elif not args.file and not args.directory and args.action != "keygen":
    raise "Target must be specified."
  
  cp = Crypt()
  cp.activate("secret.key")

  path = args.file or args.directory
  isDir = args.directory != None

  if args.action == "encode":
    cp.encode(path, isDir)
  elif args.action == "decode":
    cp.decode(path, isDir)
  elif args.action == "keygen":
    cp.keygen('secret.key')
    