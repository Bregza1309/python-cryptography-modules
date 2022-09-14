from AES_ENCRYPTION import AES128_ENCRYPTION
from AES128_DECRYPTION import AES128_DECRYPTION
from bit_encryption_functions import *
from AES_DECRYPTION_FUNCTION import *
from xts_bit_function import * 
class XTS_AES_ENCRYPTION:
    def __init__(self,plaintext,key,tweak_value):
        #padd the plaintext to at least 32 hex

        self.plaintext = string_to_hex(plaintext)
        while len(self.plaintext) < 32:
            self.plaintext = self.plaintext + '0'
        # derive key1 , key2 
        # padd key to 64-bits if necessary
        self.hex_key = string_to_hex(key)
        while len(self.hex_key) < 64:
            self.hex_key = self.hex_key + '0'
        i = 0
        self.keys = []
        while i < len(self.hex_key):
            self.keys.append(self.hex_key[i:i+32])
            i+=32

        
        # derive tweak value
        tweak_value = int(tweak_value)
        # divide plaintext into 128_bit_blocks
        self.plaintext_blocks = []
        b = 0
        while b < len(self.plaintext):
            self.plaintext_blocks.append(self.plaintext[b:b+32])
            b+= 32
        self.tweak_values = []
        for i in range(len(self.plaintext_blocks)):
            y = (2*tweak_value) + 3
            self.tweak_values.append(y)
            tweak_value = y 
        self.cipher = []
        
    def encrypt(self):
        
        temp_tweaks = self.tweak_values
        for i in range(len(self.plaintext_blocks)):

            while len(self.plaintext_blocks[i]) < 32:
                self.plaintext_blocks[i]  = self.plaintext_blocks[i] + '0'
                        
            encrypted_sector = AES128_ENCRYPTION(binary_to_hex(dec_to_binary(temp_tweaks[i])),self.keys[1]).encrypt()
            
            a = gf128_multiplication('02','01')
            for j in range(i):
                                    
                a = gf128_multiplication('02',binary_to_hex(a))
            # multiply by the outcome of AES_ENCRYPTION
            
            mult_value = gf128_multiplication(encrypted_sector,binary_to_hex(a))
            
            # xor plaintext_block with mult_value
            xor_value = binary_to_hex(xor(mult_value,hex_to_binary(self.plaintext_blocks[i])))
            
            # feed xor_value into aes
            scnd_encryption = AES128_ENCRYPTION(xor_value,self.keys[0]).encrypt()
            
            # xor second_encrption  with mult_value to get_cyphertext
            ciphertext = binary_to_hex(xor(hex_to_binary(scnd_encryption),mult_value))

            self.cipher.append(ciphertext)
        
                
               
        res_cypher = ''.join(self.cipher)
        
        return res_cypher

        
class xts_aes_decryption:
    def __init__(self,ciphertext,key,tweak_value) :
        self.ciphertext = ciphertext
        tweak_value = int(tweak_value)
        self.hex_key = string_to_hex(key)
        # padd hex_key to 64 bytes
        while len(self.hex_key) < 64:
            self.hex_key = self.hex_key + '0'
        self.keys = [self.hex_key[:32],self.hex_key[32:34]]
        self.ciphertext_blocks = []
        b = 0
        while b < len(self.ciphertext):
            self.ciphertext_blocks.append(self.ciphertext[b:b+32])
            b+=32
        self.tweak_value = []
        for i in range(len(self.ciphertext_blocks)):
            y = (2*tweak_value) + 3
            
            self.tweak_value.append(y)
            tweak_value = y  
        self.plaintext_blocks = []
    def decrypt(self):
        my_keys = self.keys
        temp_tweak = self.tweak_value
        
        for j in range(len(self.ciphertext_blocks)):
            

            encrypted_sector = AES128_ENCRYPTION(binary_to_hex(dec_to_binary(temp_tweak[j])),my_keys[1]).encrypt()
                
            a = gf128_multiplication('02','01')
            for i in range(j):
                                    
                a = gf128_multiplication('02',binary_to_hex(a))
            
            # multiply by the outcome of AES_ENCRYPTION
            
            mult_value = gf128_multiplication(encrypted_sector,binary_to_hex(a))
            
            # xor plaintext_block with mult_value
            xor_value = binary_to_hex(xor(mult_value,hex_to_binary(self.ciphertext_blocks[j])))
            
            # feed xor_value into aes
            scnd_encryption = AES128_DECRYPTION(xor_value,my_keys[0]).decrypt()
            
            # xor second_encrption  with mult_value to get_cyphertext
            plaintext = binary_to_hex(xor(hex_to_binary(scnd_encryption),mult_value))
            
            self.plaintext_blocks.append(plaintext)

        res_plaintext = ''.join(self.plaintext_blocks)
        return hex_to_string(res_plaintext)
                    


my_xts_aes = XTS_AES_ENCRYPTION('godzilla_my_favourite_car','watch_the_space',400)
my_xts_decryption = xts_aes_decryption('EA6643463BF8BA5CF17B8577D605CE8A6AB90D15E55199837262FAD5E63875E9','watch_the_space',400)
print(my_xts_aes.encrypt())
print(my_xts_decryption.decrypt())