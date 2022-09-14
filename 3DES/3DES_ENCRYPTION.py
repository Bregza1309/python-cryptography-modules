from des import DES_ENCRYPTION
from des_decryption import DES_DECRYPTION
from functions import *

class TRIPLE_DES_ENCRYPTION:
    def __init__(self,plaintext,key_1,key_2,key_3):
        self.plaintext = string_to_hex(plaintext)
        self.keys = [key_1,key_2,key_3]

    def encrypt(self):
        my_keys = self.keys
        # ENCRPTION_DECRYPTION_ENCRYPTION
        for b in range(3):
            
            
            if b == 1:
                temp_cypher = DES_DECRYPTION(self.plaintext,my_keys[b]).decrypt()
                 
            else:
                temp_cypher = DES_ENCRYPTION(self.plaintext,my_keys[b]).encrypt()
                
            self.plaintext = temp_cypher

        return temp_cypher

class TRIPLE_DES_DECRYPTION:
    def __init__(self,ciphetext,key_1,key_2,key_3):
        self.ciphertext = ciphetext
        self.keys = [key_1,key_2,key_3]

    def decrypt(self):
        # REVERSING THE ORIGINAL KEYS LIST
        my_keys = self.keys[::-1]
        # DECRYPTION_ENCRYPTION_DECRYPTION
        for i in range(3):
            if i == 1:
                temp_plain = DES_ENCRYPTION(self.ciphertext,my_keys[i]).encrypt()
            else:
                temp_plain = DES_DECRYPTION(self.ciphertext,my_keys[i]).decrypt()
            self.ciphertext = temp_plain
        return hex_to_string(temp_plain)

                        
my_3des = TRIPLE_DES_ENCRYPTION('chilwel','brendon','tatenda','muchesa')
my_3des_d = TRIPLE_DES_DECRYPTION('397ad0e5faf97928','brendon','tatenda','muchesa')
print(my_3des.encrypt())
print(my_3des_d.decrypt())