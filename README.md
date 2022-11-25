# Files-encrypter

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
python3 main.py -a keygen
```

# Usage / Flags

IMPORTANT!! Make sure you have generated a key, before start encrypting / decrypting.
By default, the program first calls the `activate()` method, which reads the key and initializes the `Crypt` class.


Different flags can be passed to perform different operations.

### -a (--action)
the `-a` flag can be either:
- encode
- decode
- keygen

Note that only one of them can be passed.

### -f (--file) OR -d (--directory) followed by file / directory name
example 
```
-f ./data.txt
-d ./data/
```

## Examples of valid arguments
1) Encode all the files in `./data/` directory
```
python3 main.py -a encode -d ./data/
```
2) Encode the file named `./data.txt`
```
python3 main.py -a encode -f ./data.txt
```

3) Decode the file named `./data.txt`
```
python3 main.py -a decode -d ./data.txt
```




IMPORTANT Make sure that you're using the same key that was used to encode when decoding, otherwise, the data will NOT be recovered.
