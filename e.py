import pyAesCrypt
import sys

try:
    inFile = sys.argv[1]
except:
    print("Usage: e.py <file> <password>")
    sys.exit(1)

try:
    password = sys.argv[2]
except:
    print("Usage: e.py <file> <password>")
    sys.exit(1)

try:
    pyAesCrypt.encryptFile(inFile, inFile + ".aes", password)
    print("Encrypted!")
except Exception as E:
    print("Error: Could not encrypt file", E)
    sys.exit(1)