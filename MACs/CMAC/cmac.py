
from bit_encryption_functions  import *
from AES_ENCRYPTION import AES128_ENCRYPTION
from AES_DECRYPTION_FUNCTION import *
from cmac_functions import *

class CMAC:
    def __init__(self,plaintext,key):
        self.hex_plain = plaintext
        self.hex_key = key
    def derive_keys(self):
        keys = []
        initial_vector = '0'
        initial_vector = hex_padding_(initial_vector,32)
        
        while len(self.hex_key) < 32:
            self.hex_key = self.hex_key + '0'
        l = AES128_ENCRYPTION(initial_vector,self.hex_key).encrypt()
        
        k1 = cmac_gf128_multiplication(l)
        keys.append(k1)
        k2 = cmac_gf128_multiplication(k1)
        keys.append(k2)
        
        return keys
    def _get_cmac_(self):
        cipher_blocks = []
        initial_vector = hex_padding_('0',32)
        cipher_blocks.append(initial_vector)
        
        #divede plaintext into 128 bits / 32 hex_values blocks
        
        i = 0
        blocks = []
        
        while i < len(self.hex_plain):
            blocks.append(self.hex_plain[i:i+32])
            i+=32
        # get keys
        keys = self.derive_keys()
        
        
        for b in range(len(blocks)):
            temp_plain = blocks[b]
            if len(temp_plain) < 32:
                temp_plain = hex_padding_right(temp_plain,32)
            
                
            if b == len(blocks)-1:
                
                if len(blocks[-1]) == 32:
                    
                    xor_value = xor(temp_plain,cipher_blocks[b])
                    xor_value = xor(xor_value, keys[0])
                    
                    
                else:
                    xor_value = xor(temp_plain,cipher_blocks[b])
                    xor_value = xor(xor_value,keys[1])
                    
                    
            else:
                
                xor_value = xor(temp_plain,cipher_blocks[b])
                
            
            
            round_value = AES128_ENCRYPTION(xor_value,self.hex_key).encrypt()
            cipher_blocks.append(round_value)
        
        return round_value
        
my_cmac = CMAC('6BC1BEE22E409F96E93D7E117393172AAE2D8A571E03AC9C9EB76FAC45AF8E5130C81C46A35CE411E5FBC1191A0A52EFF69F2445DF4F9B17AD2B417BE66C3710','2B7E151628AED2A6ABF7158809CF4F3C') 
 
 

print(my_cmac._get_cmac_())



