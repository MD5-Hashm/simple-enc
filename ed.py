import pyAesCrypt
import sys

encrypt = False
decrypt = False

try:
    if sys.argv[1] in ["-e"]:
        encrypt = True
    elif sys.argv[1] in ["-d"]:
        decrypt = True
    elif sys.argv[1] == "-h":
        print("Usage: e-d.py <arg> <file> <password>")
        print("\t-e\tEncrypt")
        print("\t-d\tDecrypt")
        sys.exit(1)
except:
    print("Usage: e-d.py <arg> <file> <password>")
    print("\t-e\tEncrypt")
    print("\t-d\tDecrypt")
    sys.exit(1)

try:
    inFile = sys.argv[2]
except:
    print("Usage: e-d.py <arg> <file> <password>")
    print("\t-e\tEncrypt")
    print("\t-d\tDecrypt")
    sys.exit(1)

try:
    password = sys.argv[3]
except:
    print("Usage: e-d.py <arg> <file> <password>")
    print("\t-e\tEncrypt")
    print("\t-d\tDecrypt")
    sys.exit(1)

if encrypt == True:
    decrypt = False
elif decrypt == True:
    encrypt = False

if encrypt == True:
    try:
        pyAesCrypt.encryptFile(inFile, inFile + ".aes", password)
        print("Encrypted!")
    except Exception as E:
        print("Error: Could not encrypt file", E)
        sys.exit(1)
elif decrypt == True:
    try:
        pyAesCrypt.decryptFile(inFile, inFile.replace(".aes", ""), password)
        print("Decrypted!")
    except Exception as E:
        print("Error: Could not decrypt file", E)
        sys.exit(1)
else:
    print("error")