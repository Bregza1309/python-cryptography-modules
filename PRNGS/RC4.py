from PRNG import *
from functions import * 
from bit_encryption_functions import *
 

class RC4_ENCRYPTION:
    def __init__(self,plaintext,p , q , seed):
        self.plaintext256 = hex_to_binary(string_to_hex(plaintext))
        while len(self.plaintext256) < 2048:
            self.plaintext256 = self.plaintext256 + '0'

        self.key256 = Blum_Blum_Shub_generator(2048,p,q,seed)
    def key_permutation(self):
        # partition key and plaintext into bytes
        key_bytes = []
        
        b = 0
        while b < len(self.key256):
            key_bytes.append(self.key256[b:b+8])
            
            b+=8
        
        # initialization of S
        s = []
        t = []
        for i in range(256):
            s.append(i)  
            t.append( bin_to_dec(key_bytes[i % len(key_bytes)]))

        c = 0
        j = 0
        # initial permutation of S using vector T
        for n in range(256):
            j = (j + s[n] + t[n]) % 256
            a = s[c]
            b = s[j]
            s[c] = b
            s[j] = a
            c+=1
        c = 0
        j = 0
        new_key = []
        # stream geneartion of bits
        while len(new_key) < 256:
            c = (c + 1) % 256
            j = (j + s[c] ) % 256
            
            a = s[c]
            b = s[j]
            s[c] = b
            s[j] = a
             
            k = (s[c] + s[j]) % 256
            
            new_key.append(s[k])
        
        # converting new_key_values from dec to binary then storing it in byte list/array
        bin_Key = []
        for d in range(len(new_key)):
            byte = reverse_binary(dec_to_binary(new_key[d]))
            while len(byte) < 8 : 
                byte = byte + '0'
            byte = reverse_binary(byte)
            bin_Key.append(byte)
        return bin_Key
    def encrypt(self):
        bytes_key = self.key_permutation()
        plaintext_bytes = []
        b = 0
        while b < len(self.plaintext256) :
            plaintext_bytes.append(self.plaintext256[b:b+8])
            b+=8
        
        ciphertext = ''
        c = 0
        while c < len(plaintext_bytes):
            xor_bytes = xor(bytes_key[c],plaintext_bytes[c])
            ciphertext = ciphertext + xor_bytes
            c+=1
        return binary_to_hex(ciphertext) 
class RC4_DECRYPTION:
    def __init__(self, ciphertext, p, q, seed):
         self.ciphertext = hex_to_binary(ciphertext)
         self.PRNG_key = Blum_Blum_Shub_generator(2048,p,q,seed)

    def key_permutation(self):
        # partition key and plaintext into bytes
        key_bytes = []
        
        b = 0
        while b < len(self.PRNG_key):
            key_bytes.append(self.PRNG_key[b:b+8])
            
            b+=8
        
        # initialization of S
        s = []
        t = []
        for i in range(256):
            s.append(i)  
            t.append( bin_to_dec(key_bytes[i % len(key_bytes)]))

        c = 0
        j = 0
        # initial permutation of S using vector T
        for n in range(256):
            j = (j + s[n] + t[n]) % 256
            a = s[c]
            b = s[j]
            s[c] = b
            s[j] = a
            c+=1
        c = 0
        j = 0
        new_key = []
        # stream geneartion of bits
        while len(new_key) < 256:
            c = (c + 1) % 256
            j = (j + s[c] ) % 256
            
            a = s[c]
            b = s[j]
            s[c] = b
            s[j] = a
             
            k = (s[c] + s[j]) % 256
            
            new_key.append(s[k])
        
        # converting new_key_values from dec to binary then storing it in byte list/array
        bin_Key = []
        for d in range(len(new_key)):
            byte = reverse_binary(dec_to_binary(new_key[d]))
            while len(byte) < 8 : 
                byte = byte + '0'
            byte = reverse_binary(byte)
            bin_Key.append(byte)
        return bin_Key
    def decrypt(self):
        cipher_bytes = []
        plaintext_binary = ''
        # get stream key from key_permutation_functions
        key_byte_array = self.key_permutation()
        b = 0
        #partition_ciphertext into bytes and store em in an array!
        while len(cipher_bytes) < 256:
            cipher_bytes.append(self.ciphertext[b:b+8])
            b+=8
        
        b = 0
        # xor ciphertext_bytes_with key_bytes_and return a ciphertext
        while b < len(cipher_bytes):
            xor_value = xor(cipher_bytes[b],key_byte_array[b])
            plaintext_binary =  plaintext_binary + xor_value
            b+=1
        # convert binary to string
        string_plaintext = hex_to_string(binary_to_hex(plaintext_binary))
        return string_plaintext

        
ciphertext = RC4_ENCRYPTION('bregza_the_man_with_a_plan_nobody_can_flexw',911,1303,913).encrypt()
print(ciphertext)
print(RC4_DECRYPTION(ciphertext,911,1303,917).decrypt())