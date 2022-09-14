
from bit_encryption_functions import *
from functions import *


def key_generation():
      
    prime_nums = [] 
            
    for i in range(200,1000):
        isPrime = True
        for b in range(2,i):
            
            if i % b == 0:
                isPrime = False
        if isPrime:
            if i % 4 == 3:

                prime_nums.append((i))             

    p = choice(prime_nums)
    q = choice(prime_nums)
    
    n = p * q
    euler_totient_value = Eulers_totient(n)
    domain = list(range(1,euler_totient_value -1))
    while True :
        b = choice(domain)
        if gcd(euler_totient_value,b) ==1:
            
            e = b
            break
    
    
    for k in range(0,euler_totient_value):
        if ( k * e) % euler_totient_value == 1:
            
                
            d = k
            
    
    return [n,e,d] 
bregza_keys = key_generation()
bregza_public_key = [bregza_keys[1],bregza_keys[0]]
bregza_private_key = [bregza_keys[2],bregza_keys[0]]
print(bregza_public_key)
print(bregza_private_key)


class RSA_ENCRYPTION:
    def __init__(self,plaintext,public_key):
        self.hex_plaintext = string_to_hex(plaintext)
        
        self.hex_bytes = []
        
        i = 0
        while i < len(self.hex_plaintext):
            self.hex_bytes.append(self.hex_plaintext[i:i+2])
            i+=2
        
        self.public_key = public_key
        
    def encrypt(self):
        
        ciphertext = []
        # encrypt_byte_by_byte
        for x in self.hex_bytes:
            
            if len(x) < 2:
                x= hex_padding(x,2)
            decimal_value = hex_to_dec(x)
            
            
            mod_temp = pow(int(decimal_value),self.public_key[0]) % self.public_key[1]
            
            ciphertext.append( mod_temp)
        print(ciphertext)
        cipher = ''
        for b in ciphertext:
            temp = str(b)
            while len(temp) < 6:
                temp = '0' + temp
            cipher = cipher + temp
                  
        
        return cipher
ciphetext = RSA_ENCRYPTION('the big bang theory set in the deep parts of detroit',bregza_public_key)
print(ciphetext.hex_plaintext)
class RSA_DECRYPTION:
    def __init__(self,ciphertext,private_key):
        self.dec_array  = []
        i = 0
        while i < len(ciphertext):
            self.dec_array.append(ciphertext[i:i+6])
            i+=6
        
        self.private_key = private_key
        
    def decrypt(self):
        
        plaintext = ''
        b = 0 
        cipher_list = []
        for i in self.dec_array:
        
            temp = int(i)
          
            mod_temp = pow(temp,self.private_key[0]) % self.private_key[1]
            temp_block = str(mod_temp)
            cipher_list.append(temp_block)
            plaintext = plaintext + binary_to_hex(dec_to_binary(temp_block))
        return hex_to_string(plaintext)

decrypt = RSA_DECRYPTION(ciphetext.encrypt(),bregza_private_key).decrypt()
print(decrypt)




     