from key_exchange import *
from random import choice
from bit_encryption_functions import *
# generaate user global public elements p and a
bregza_global_elements = Global_Public_Elements()

def user_key_generation(public_elements):
    """Generate public key using Global Public Elements"""
    q = public_elements[0]
    a = public_elements[1]
    # randomly choose private key
    domain = list(range(1,q-1))
    x = choice(domain)
    # calculate Ya 
    
    y = pow(a,x) % q
    public_key = [q,a,y,x]
    return public_key

plaintext = 'im the next elon REST IN PEACE PAPER ROUTE FRANK ! ITS DOLPHHHHH!'
def Encryption(plaintext,receiver_public_key):
    """Encrypt Plaintext using Public Key"""
        
    q = receiver_public_key[0]
    a = receiver_public_key[1]
    y = receiver_public_key[2]
    # store ASCII decimal values of each character
    hex_value  = string_to_hex(plaintext)
    bytes = []
    cipher_bytes = []
    b = 0
    while b < len(hex_value):
        bytes.append(hex_value[b:b+2])
        b+=2
    k = choice(list(range(1,q)))
    c_1 = pow(a,k) % q
    for j in bytes:
        
        if len(j) < 2:
            j = j + '0'
            
        Key = pow(y,k) % q
        if gcd(q,Key) == 1:
            m = hex_to_dec(j)
            if m < q:
                
                c_2 = (Key * m) % q
                
                c_2 = str(c_2)
                while len(c_2) < 3:
                    c_2 = '0' + c_2
                cipher_bytes.append(c_2)
                
        else:
            Encryption(plaintext,receiver_public_key)
                    
                                
    
    ciphertext = [c_1,''.join(cipher_bytes)]
    return ciphertext

 
def decryption(ciphertext , Xa,q):
    c_1 = ciphertext[0]
    c_2 = ciphertext[1]
    key = pow(c_1,Xa) % int(q)
    euler_value = Eulers_totient(q)
    k_inverse = pow(key,euler_value-1)
    b = 0
    cipher_bytes = []
    while b < len(c_2):
        cipher_bytes.append(c_2[b:b+3])
        b+= 3
    plaintext = []
    for t in cipher_bytes:
        temp = int(t)
        plain = (temp * k_inverse) % q
        plaintext.append(binary_to_hex(dec_to_binary(plain)))
    string_plain = ''.join(plaintext)
    return string_plain

            
