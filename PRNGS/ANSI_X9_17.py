from PRNG import *
from TRIPLE_DES_ENCRYPTION import TRIPLE_DES_ENCRYPTION,TRIPLE_DES_DECRYPTION
from bit_encryption_functions import * 


class ANSI_X9_17:
    def __init__(self,initial_seed,key_1,key_2,key_3,loop_value):
        self.loop_value = int(loop_value)
        self.initial_seed = string_to_hex(initial_seed)
        # padd self.initial_seed to 16 hex_values
        self.initial_seed = hex_padding(self.initial_seed,16)
        self.current_DT = ''
        

        # initialize DES KEYS
        self.key_1 = string_to_hex(key_1)
        self.key_2 = string_to_hex(key_2)
        self.key_3 = string_to_hex(key_3)

        #padd the keys to 16 hex_values if needed
        self.key_1 = hex_padding(self.key_1 , 16)
        self.key_2 = hex_padding(self.key_2,16)
        self.key_3 = hex_padding(self.key_3 , 16)

        self.generated_random_hex = ''
        self.test = []

    def get_current_time(self):
        current_DT = get_instaneous_date_and_time()
        # convert datetime to hex_values and pad to 64bits
        current_DT = binary_to_hex(dec_to_binary(current_DT))
        # padd the hex_value to 16 hex_values 
        current_DT = hex_padding(current_DT,16)
        return current_DT

    def encrypt(self):
        for b in range(self.loop_value):
            
            current_dt = self.get_current_time()
            # encrypt date_time using triple_des
            cipher_DT = TRIPLE_DES_ENCRYPTION(current_dt,self.key_1,self.key_2,self.key_3).encrypt()
            
            # ADD ENCRYPTED_DT WITH INITIAL_VECTOR
            v_DT = binary_to_hex(xor(hex_to_binary(cipher_DT),hex_to_binary(self.initial_seed)))
           
            # encrypt vdt using triple_des
            self.generated_random_hex = TRIPLE_DES_ENCRYPTION(v_DT,self.key_1,self.key_2,self.key_3).encrypt()
            
            # xor generated_random_hex with encrypted date_and_time
            xor_value = binary_to_hex(xor(hex_to_binary(self.generated_random_hex),hex_to_binary(cipher_DT)))
            
            # encrypt xor_value using triple_des

            self.initial_seed = TRIPLE_DES_ENCRYPTION(xor_value,self.key_1,self.key_2,self.key_3).encrypt()
            

            
        return self.generated_random_hex
            

my_ansi = ANSI_X9_17('BREGZA','coin','heads','tails',5)
print(my_ansi.encrypt())     
        
        