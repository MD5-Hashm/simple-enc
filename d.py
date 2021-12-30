import pyAesCrypt
import sys

try:
    inFile = sys.argv[1]
except:
    print("Usage: d.py <file> <password>")
    sys.exit(1)

try:
    password = sys.argv[2]
except:
    print("Usage: d.py <file> <password>")
    sys.exit(1)

try:
    pyAesCrypt.decryptFile(inFile, inFile.replace(".aes", ""), password)
    print("Decrypted!")
except Exception as E:
    print("Error: Could not decrypt file", E)
    sys.exit(1)