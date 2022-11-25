# files-encrypter

# Getting Started
This project utilizes the cryptography module

To install the modules
```
cd files-encrypter/
pip3 install -r requirements.txt
```


# Key generation
The algorithm uses a base64-encoded 32-byte key to encode & decode data, which must be kept secret. 
So in order to get started, the key must be generated first.

This command generates a unique key in the current directory
```
python3 main.py keygen
```
