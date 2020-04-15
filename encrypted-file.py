from cryptography.fernet import Fernet
import base64
key = Fernet.generate_key() #use one of the methods to get a key (it0must0be-the same when decrypting)
print(key)
input_file = "config.ini"
outout_file = "config.ini.enc"

with open(input_file, 'rb') as f:
  data = f.read()
  
fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as o:
  o.write(encrypted)
