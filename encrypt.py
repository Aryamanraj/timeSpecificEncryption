import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from Cryptodome.Cipher import AES
from base64 import b64encode, b64decode



def getPassword(_from, _to):
      import requests
      from datetime import datetime, timedelta
      now = datetime.now()
      __from = now.replace(day=int(_from), hour=0, minute=0, second=0, microsecond=0)
      __from_seconds_passed = (now - __from).total_seconds()
      __from_minutes_passed = __from_seconds_passed / 60
      __from_binOfMinutesPassed = bin(int(__from_minutes_passed))[2:]
      __to = now.replace(day=int(_to), hour=0, minute=0, second=0, microsecond=0)
      __to_seconds_passed = (now - __to).total_seconds()
      __to_minutes_passed = __to_seconds_passed / 60
      __to_binOfMinutesPassed = bin(int(__to_minutes_passed))[2:]
      url = "http://192.168.61.8:5223/input_hash?From="+__from_binOfMinutesPassed+"&To="+__to_binOfMinutesPassed
      response = requests.get(url)
      if response.status_code == 200:
            data = response.json()
            print(data)
            return str(data)
      else:
            print('Error:', response.status_code)



def encrypt(plain_text, _from, _to):
      import chardet
      print(type(getPassword(_from, _to)))
      password = getPassword(_from, _to)
      password_bytes = password.encode('utf-8')

      #################
      salt = 'salt'.encode('utf-8')
      kdf = PBKDF2HMAC(
          algorithm=hashes.SHA512(),
          length=32,
          salt=salt,
          iterations=10000,
          backend=default_backend()
      )
      key = kdf.derive(password_bytes)
      nonce = password_bytes


      cipher = AES.new(key, AES.MODE_GCM)
      ciphertext, tag = cipher.encrypt_and_digest(plain_text.encode())
      ciphertext_b64 = b64encode(ciphertext).decode()
      print(ciphertext_b64)



      # aesgcm = AESGCM(key)
      # cipher_text_bytes = aesgcm.encrypt(
      #     nonce=nonce,
      #     data=plain_text.encode('utf-8'),
      #     associated_data=None
      # )
      # ##################


      # # CONVERSION of raw bytes to BASE64 representation
      # cipher_text = base64.urlsafe_b64encode(cipher_text_bytes)
      # # DECRYPTION
      # print('cipher text: ', type(cipher_text_bytes.decode('windows-1251')))
      # decrypted_cipher_text_bytes = aesgcm.decrypt(
      #     nonce=nonce,
      #     data=base64.urlsafe_b64decode(cipher_text),
      #     associated_data=None
      # )
      # decrypted_cipher_text = decrypted_cipher_text_bytes.decode('utf-8')
      # print(type(decrypted_cipher_text))




def decryptor():
      password = str(23892643)
      password_bytes = password.encode('utf-8')


      #################
      salt = 'salt'.encode('utf-8')
      kdf = PBKDF2HMAC(
          algorithm=hashes.SHA512(),
          length=32,
          salt=salt,
          iterations=10000,
          backend=default_backend()
      )
      key = kdf.derive(password_bytes)
      nonce = password_bytes
      #################
      _text = 'ZSM//byjqjImJW6Naw=='
      ciphertext = b64decode(_text.encode())
      decipher = AES.new(key, AES.MODE_GCM)
      plain_text = decipher.decrypt_and_verify(ciphertext, decipher.digest()).decode()
      print(plain_text)
      # _result = {'encoding': 'windows-1251', 'confidence': 0.3982065233282465, 'language': 'Russian'}
      # _cipher_text_bytes = _text.encode('windows-1251')
      # cipher_text = base64.urlsafe_b64encode(_cipher_text_bytes)
      # decrypted_cipher_text_bytes = aesgcm.decrypt(
      #     nonce=nonce,
      #     data=base64.urlsafe_b64decode(cipher_text),
      #     associated_data=None
      # )
      # decrypted_cipher_text = decrypted_cipher_text_bytes.decode('utf-8')
      # print(decrypted_cipher_text)




# _from = input("From: ")
# _to = input("To: ")
# encrypt('first message', _from, _to)

# passwd = str(input("Enter Password: "))
# cipher_text = input("Enter Cipher Text: ")
print(decryptor())