from Crypto.Util.number import long_to_bytes
from base64 import b64encode

message = b"Our counter agencies have intercepted your messages and a lot "
message += b"of your agent's identities have been exposed. In a matter of "
message += b"days all of them will be captured"

# load ciphertext
f = open("out.txt", "r")
_ = f.readline()
enc_message = f.readline()
enc_flag = f.readline()

# transform hex string to byte array
enc_message = bytes.fromhex(enc_message)
enc_flag = bytes.fromhex(enc_flag)

# XOR
result = b""
for b1, b2, b3 in zip(enc_flag,enc_message, message):
    print(type(b1))
    result += bytes([b1 ^ b2 ^ b3])


print(f"{result}")