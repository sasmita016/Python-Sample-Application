from cryptography.fernet import Fernet
import base64

key = use the one genearted from encrypted. file 

input_file = "config.ini.enc"

with open(input_file, 'rb') as f:
  data = f.read()
  
fernet = Fernet(key)
decrypted = fernet.decrypt(data)

decrypted_split = decrypted.rstrip()
decrypted_decode = decrypted_split.decode()

print("Decoded value",decrypted_decode)

cut_decrypted = decrypted_decode.split('|')
A K V client id = cut_decrypted[2]
A K V tenant id = cut_decrypted[1]
A K V secret = cut_decrypted[3]
A K V vault url = cut_decrypted[0]

