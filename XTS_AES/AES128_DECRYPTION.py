from AES_DECRYPTION_FUNCTION import *
from bit_encryption_functions import * 
from AES_KEY import AES_KEY

class AES128_DECRYPTION:
    """DECRYPTS CYPHERTEXT USING GIVEN KEY"""
    def __init__(self,cyphertext,key):
        self.hex_cypher = cyphertext
        self.keys = AES_KEY(key).key_expansion()

    def decrypt(self):
        my_keys = self.keys[::-1]
        
        # loop through the 10 rounds
        for i in range(11):
            # no mix columns in first round
            if i == 0:

                # xor last_key and cyphertex
                xor_value = binary_to_hex(xor(hex_to_binary(self.hex_cypher),hex_to_binary(my_keys[i])))

                # shift_rows
                shift_rows_value = shift_rows_inverse(xor_value)

                # substitute in inverse_s_box
                s_box_value = s_box_inverse_substitution(shift_rows_value)

                # renew hex_cypher for new round
                
                self.hex_cypher = s_box_value 
            elif i == 10:
                # xor last_key and cyphertex
                xor_value = binary_to_hex(xor(hex_to_binary(self.hex_cypher),hex_to_binary(my_keys[i])))
                 # renew hex_cypher for new round
                
                self.hex_cypher = xor_value 
            else:
                 # xor last_key and cyphertex
                xor_value = binary_to_hex(xor(hex_to_binary(self.hex_cypher),hex_to_binary(my_keys[i])))
                 # renew hex_cypher for new round

                # inverse mix_columns
                mix_columns_value = mix_columns_inverse(xor_value)
                
                # shift_rows
                shift_rows_value = shift_rows_inverse(mix_columns_value)

                # substitute in inverse_s_box
                s_box_value = s_box_inverse_substitution(shift_rows_value)

                # renew hex_cypher for new round
               
                self.hex_cypher = s_box_value 
        # return cyphertext           
        return self.hex_cypher
