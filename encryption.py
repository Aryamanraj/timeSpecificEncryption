import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from flask import Flask, jsonify, request
import requests
from datetime import datetime, timedelta
from timeFromFirstDay import timeFromFirstDay
from findCommonSubstring import find_common_substring
from loadTree import load_tree
from getPasswd import getPassword

# def getPassword(_from_date,_from_hour, _to_date,_to_hour):

#       now = datetime.now()
#       __from = now.replace(day=int(_from_date), hour=int(_from_hour), minute=0, second=0, microsecond=0)
#       __from_seconds_passed = (now - __from).total_seconds()
#       __from_minutes_passed = __from_seconds_passed / 60
#       __from_binOfMinutesPassed = bin(abs(int(__from_minutes_passed)))[2:]


#       __to = now.replace(day=int(_to_date), hour=int(_to_hour), minute=0, second=0, microsecond=0)
#       __to_seconds_passed = (now - __to).total_seconds()
#       __to_minutes_passed = __to_seconds_passed / 60
#       __to_binOfMinutesPassed = bin(abs(int(__to_minutes_passed)))[2:]


#       url = "http://192.168.61.8:5223/input_hash?From="+__from_binOfMinutesPassed+"&To="+__to_binOfMinutesPassed
#       response = requests.get(url)
#       if response.status_code == 200:
#             data = response.json()
#             print(data)
#             return str(data)
#       else:
#             print('Error:', response.status_code)


def encrypt(key, source, encode=True):
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    IV = key[:16]  # generate IV
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size  # calculate needed padding
    source += bytes([padding]) * padding  # Python 2.x: source += chr(padding) * padding
    data = IV + encryptor.encrypt(source)  # store the IV at the beginning and encrypt
    print("data->", base64.b64encode(data).decode("latin-1"))
    return base64.b64encode(data).decode("latin-1") if encode else data

def decrypt(key, source, decode=True):
    if decode:
        source = base64.b64decode(source.encode("latin-1"))
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    IV = key[:16]  # extract the IV from the beginning
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(source[AES.block_size:])  # decrypt
    padding = data[-1]  # pick the padding value from the end; Python 2.x: ord(data[-1])
    if data[-padding:] != bytes([padding]) * padding:  # Python 2.x: chr(padding) * padding
        raise ValueError("Invalid padding...")
    return data[:-padding]  # remove the padding


def listPasswd():
    inputer = timeFromFirstDay()
    listBins = []
    _listPasswd = []

    for i in range(0,len(inputer)):
        listBins.append(inputer[0:i])

    
    for j in range(0, len(listBins)):
        url = "http://192.168.61.8:5223/get_hash?Bin="+listBins[j]
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            _listPasswd.append(data)
        else:
            print('Error:', response.status_code)
    return _listPasswd

    



app = Flask(__name__)


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

@app.route('/encrypting', methods=["GET"])
def encryption():
    import urllib.parse
    

    _from_date = request.args["From_date"]
    _from_hour = request.args["From_hour"]
    _to_date = request.args["To_date"]
    _to_hour = request.args["To_hour"]
    _data = request.args["Data"]
    _passwd = getPassword(_from_date,_from_hour,_to_date,_to_hour)
    passwd = bytes(_passwd, "ascii")
    data = bytes(_data,"ascii")
    my_password = passwd
    my_data = data
    safe_string = urllib.parse.quote_plus(encrypt(my_password, my_data))
    print(safe_string)
    return jsonify("cipher text:", safe_string,"password: ", _passwd)


@app.route('/decrypting', methods=["GET"])
def decryption():
    _cipher = request.args["cipher"]
    _list_of_pwd = listPasswd()
    #_cipher = "d76QNdHHppq6wsvRETIvCqTUawY320YSl+88333TSZA="
    passwd = []
    message = ""
    for j in range(0,len(_list_of_pwd)):
        _passwd = _list_of_pwd[j]
        passwd.append((bytes(str(_passwd), "ascii")))
    for k in range(0, len(passwd)):
        try:
            message = str(decrypt(passwd[k], _cipher).decode())
        except:
            pass
    return jsonify("sucess", message, "listofpasswords", _list_of_pwd)


app.run(host = '0.0.0.0',port = 6117)