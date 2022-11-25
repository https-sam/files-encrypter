# files-encrypter

# Getting Started
This project utilizes the cryptography module

To install the modules
```
cd files-encrypter/
pip3 install -r requirements.txt
```


# Key generation
The algorithm uses a base64-encoded 32-byte key to encrypt & decrypt data, which must be kept secret. 
So in order to get started, the key must be generated first.

This command generates a unique key in the current directory
```
python3 main.py keygen
```

# Usage

IMPORTANT!! Make sure you have generated a key, before start encrypting / decrypting.
By default, the program first calls the `activate()` method, which reads the key and initializes the `Crypt` class.

There are different flags that can be passed.

## arguments / flags

- encode
```
python3 main.py encode
```
when `encode` argument is passed, the program will encode all the data in the file(s)


- decode
```
python3 main.py ecode
```
when `decode` argument is passed, the program will decode all the data in the file(s). 
IMPORTANT!! Make sure that you're using the same key that was used for encoding, otherwise, the data will NOT be recovered.
