# simple-enc
Simple python program to encrypt files with AES-256 encryption

# Setup
First install "pyAesCrypt" using pip.
Thats it!
Optionally you can add an alias such as: 

alias ed="python3 ~/Python/ed.py"

# Usage
Usage: e-d.py <arg> <file> <password>      
  -e      Encrypt   |   -d      Decrypt
  
# Example
  
python3 ~/Python/ed.py -e important.txt "great password"
  
or if you have an alias
  
ed -e important.txt "great password"
  
its the same for decription except replace "-e" with "-d"
  
python3 ~/Python/ed.py -d important.txt.aes "great password"
  
or if you have an alias
  
ed -d important.txt.aes "great password"
