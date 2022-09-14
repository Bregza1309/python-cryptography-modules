from AES_DECRYPTION_FUNCTION import *
from bit_encryption_functions import * 
from AES_KEY import AES_KEY

class AES128_DECRYPTION:
    """DECRYPTS CYPHERTEXT USING GIVEN KEY"""
    def __init__(self,cyphertext,key):
        self.hex_cypher = cyphertext
        self.hex_blocks = []
        b = 0
        while b < len(self.hex_cypher):
           
            self.hex_blocks.append(self.hex_cypher[b:b+32])
            b += 32
        self.keys = AES_KEY(key).key_expansion()
        self.plaintext = ''

    def decrypt(self):
        my_keys = self.keys[::-1]
        initial_vector = 'C5CB2E7F58400000'
        
        # padd initialization vector
        while len(initial_vector) < 32:
            initial_vector = initial_vector + '0'
        
        for cyphertext in self.hex_blocks:
                       
            temp_cypher = cyphertext
            # loop through the 10 rounds
            for i in range(11):
                # no mix columns in first round
                if i == 0:

                    # xor last_key and cyphertex
                    xor_value = binary_to_hex(xor(hex_to_binary(temp_cypher),hex_to_binary(my_keys[i])))

                    # shift_rows
                    shift_rows_value = shift_rows_inverse(xor_value)

                    # substitute in inverse_s_box
                    s_box_value = s_box_inverse_substitution(shift_rows_value)

                    # renew hex_cypher for new round
                    
                    temp_cypher = s_box_value 
                elif i == 10:
                    # xor last_key and cyphertex
                    xor_value = binary_to_hex(xor(hex_to_binary(temp_cypher),hex_to_binary(my_keys[i])))
                    # renew hex_cypher for new round
                    
                    temp_cypher = xor_value 
                else:
                    # xor last_key and cyphertex
                    xor_value = binary_to_hex(xor(hex_to_binary(temp_cypher),hex_to_binary(my_keys[i])))
                    # renew hex_cypher for new round

                    # inverse mix_columns
                    mix_columns_value = mix_columns_inverse(xor_value)
                    
                    # shift_rows
                    shift_rows_value = shift_rows_inverse(mix_columns_value)

                    # substitute in inverse_s_box
                    s_box_value = s_box_inverse_substitution(shift_rows_value)

                    # renew hex_cypher for new round
                
                    temp_cypher = s_box_value 
            # xor with INITIALISATION VECTOR 
            plaintext = binary_to_hex(xor(hex_to_binary(initial_vector),hex_to_binary(temp_cypher)))
            initial_vector = cyphertext 
             
            self.plaintext = self.plaintext + plaintext

        pre_plaintext = hex_to_string(self.plaintext)
        final_plaintext = ''
        b = 0
        while pre_plaintext[b] !='@':
            final_plaintext = final_plaintext + pre_plaintext[b]
            b+=1
        return final_plaintext
my_decryption = AES128_DECRYPTION('C62BEA1F1B7F701FB3F51B197BEC08ACE2A620919E1D0C971CD787929B02BBBA88DB8B1D95BAF768C60EDD77C5429EC0','muchesa')
print(my_decryption.decrypt())