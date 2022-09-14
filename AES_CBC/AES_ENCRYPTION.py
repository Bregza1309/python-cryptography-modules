from AES_DECRYPTION_FUNCTION import get_whole_number
from bit_encryption_functions import *
from AES_KEY import AES_KEY

# class aes for ecryption
class AES128_ENCRYPTION:
    """ENCRYPT TEXT USING AES """
    def __init__(self,plaintext,key):

        self.hex_plain = string_to_hex(plaintext + ' ')
        self.hex_blocks = []
        if len(self.hex_plain) >= 32:
             
             b = 0
             while True:
                if b > len(self.hex_plain):
                    break
                else:

                    self.hex_blocks.append(self.hex_plain[b:b+32])
                b+=32
        else:
            self.hex_blocks.append(self.hex_plain)
        self.ciphertext = ''
        # retreive all round keys from key_expansion function
        self.keys = AES_KEY(key).key_expansion()

    def encrypt(self):
        """ENCRYPTS 128 bits plaintext using given key """
        # assign retreived keys in array my_keys
        my_keys = self.keys
        initial_vector = 'C5CB2E7F58400000'
        for plaintext in self.hex_blocks:
            temp_plaintext = plaintext
            # padd plaintext to 128 bits if needed
            while (len(temp_plaintext) < 32):
                temp_plaintext = temp_plaintext + '0'

            # padd initialization_vector
            while len(initial_vector) < 32:
                initial_vector = initial_vector + '0'
            # xor plaintext with initialization vector
            temp_plaintext = binary_to_hex(xor(hex_to_binary(temp_plaintext) ,hex_to_binary(initial_vector)))
            
            # loop through 10 rounds
            for i in range(11):
                if i == 0:
                    
                    # xor state bits with round 0 key
                    xor_value = binary_to_hex(xor(hex_to_binary(temp_plaintext),hex_to_binary(my_keys[i])))
                    temp_plaintext = xor_value
                    
                elif i == 10:
                    # substitute into the s_box

                    s_box_value = s_box_sub(temp_plaintext)
                    # re arrange into colunmns
                    
                    s_box_value = w_arr_to_string(correct_array(s_box_value))
                    
                    #shift_rows 
                    shift_rows_value = shift_rows(s_box_value)
                    # xor with round key
                    round_cypher = binary_to_hex(xor(hex_to_binary(shift_rows_value),hex_to_binary(w_arr_to_string(correct_array(my_keys[i])))))
                    
                    temp_plaintext = w_arr_to_string(correct_array(round_cypher)) 
                    self.ciphertext = self.ciphertext + temp_plaintext
                    initial_vector = temp_plaintext
                     
                else:
                    
                    # substitute into the s_box

                    s_box_value = s_box_sub(temp_plaintext)
                    # re arrange into colunmns
                    
                    s_box_value = w_arr_to_string(correct_array(s_box_value))
                    
                    #shift_rows 
                    shift_rows_value = shift_rows(s_box_value)
                    
                    
                    # mix columns
                    mix_columns_value = mix_columns(shift_rows_value)
                    
                    # add round key 
                    round_cypher = binary_to_hex(xor(hex_to_binary(mix_columns_value),hex_to_binary(w_arr_to_string(correct_array(my_keys[i])))))
                    
                    # ASSIGN NEW ROUND CYPHETEXT
                    temp_plaintext = w_arr_to_string(correct_array(round_cypher)) 
                    
        return self.ciphertext
                                
    
my_aes = AES128_ENCRYPTION('trust_is_a_virtue_you_either_got_it_or_you_dont','muchesa') 
 
print(my_aes.encrypt())
