from bit_encryption_functions import *
from AES_KEY import AES_KEY

# class aes for ecryption
class AES128_ENCRYPTION:
    """ENCRYPT TEXT USING AES """
    def __init__(self,plaintext,key):
        self.hex_plain = string_to_hex(plaintext)
        # retreive all round keys from key_expansion function
        self.keys = AES_KEY(key).key_expansion()

    def encrypt(self):
        """ENCRYPTS 128 bits plaintext using given key """
        # assign retreived keys in array my_keys
        my_keys = self.keys

        # padd plaintext to 128 bits if needed
        while len(self.hex_plain) < 32:
            self.hex_plain = self.hex_plain + '0'
        # loop through 10 rounds
        for i in range(11):
            if i == 0:
                
                 # xor state bits with round 0 key
                xor_value = binary_to_hex(xor(hex_to_binary(self.hex_plain),hex_to_binary(my_keys[i])))
                self.hex_plain = xor_value
                
            elif i == 10:
                 # substitute into the s_box

                s_box_value = s_box_sub(self.hex_plain)
                # re arrange into colunmns
                
                s_box_value = w_arr_to_string(correct_array(s_box_value))
                
                #shift_rows 
                shift_rows_value = shift_rows(s_box_value)
                # xor with round key
                round_cypher = binary_to_hex(xor(hex_to_binary(shift_rows_value),hex_to_binary(w_arr_to_string(correct_array(my_keys[i])))))
                
                self.hex_plain = w_arr_to_string(correct_array(round_cypher)) 
                return self.hex_plain
                
            else:
                
                # substitute into the s_box

                s_box_value = s_box_sub(self.hex_plain)
                # re arrange into colunmns
                
                s_box_value = w_arr_to_string(correct_array(s_box_value))
                
                #shift_rows 
                shift_rows_value = shift_rows(s_box_value)
                
                
                # mix columns
                mix_columns_value = mix_columns(shift_rows_value)
                
                # add round key 
                round_cypher = binary_to_hex(xor(hex_to_binary(mix_columns_value),hex_to_binary(w_arr_to_string(correct_array(my_keys[i])))))
                
                # ASSIGN NEW ROUND CYPHETEXT
                self.hex_plain = w_arr_to_string(correct_array(round_cypher)) 
                

                





   
my_aes = AES128_ENCRYPTION('bregza','muchesa') 
 
print(my_aes.encrypt())
