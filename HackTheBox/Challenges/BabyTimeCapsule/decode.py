import socket
import json
from decimal import *
from Crypto.Util.number import long_to_bytes
from modint import ChineseRemainderConstructor

TARGET_HOST="localhost";
TARGET_PORT=1337
e=5

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (TARGET_HOST, TARGET_PORT)
sock.connect(server_address)

response = sock.recv(1024)
print(f"{response}")

message="Y"
ciphertexts=[]
modulus=[]

for i in range(e):
    sock.sendall(message.encode())
    response = sock.recv(598)
    print(f"{response}")

    #parse ciphertext from response
    ciphertext = json.loads(response)["time_capsule"]
    #convert hexstring to long
    ciphertext = int(ciphertext,16)
    ciphertexts.append(ciphertext)

    #parse modulus from response
    N = json.loads(response)["pubkey"][0]
    #convert hexstring to long
    N = int(N,16)
    modulus.append(N)

    response = sock.recv(1024)



print(f"{ciphertexts}")
print(f"{modulus}")

#Solve equation using CRT
cr = ChineseRemainderConstructor(modulus)
solve_crt = cr.rem(ciphertexts)

#Take e-th root
#Integer is too large to be converted to normal float
getcontext().prec = 512
result = Decimal(solve_crt) ** (Decimal(1.0) / Decimal(e) )
assert result**e == solve_crt

#Root computation returns float
print(f"{long_to_bytes(int(result)).decode('utf_8')}")
