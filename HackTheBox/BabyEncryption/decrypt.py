# load ciphertext
f = open("msg.enc", "r")
ciphertext = f.read()
# print(ciphertext)

# transform ciphertex back to byte array
byte_arr = bytes.fromhex(ciphertext)
# print(byte_arr)

solution = ""

#iterate over the encrypted bytes one by one
for byte in byte_arr:
    for c in range(0,255):
        #find the original character that matches the equation
        if ((123*c + 18) % 256 == byte):
            solution += chr(c)
            break

print(solution)



