from bit_key_encryption_functions import *

class AES_KEY:
    def __init__(self,key):
        self.key = string_to_hex(key)

    def key_expansion(self):
        while len(self.key) < 32:
            self.key = self.key + '0'
        
        b = 0
        c = 0
        round_keys = []
        
        round_constants = ['01', '02', '04', '08', '10', '20', '40', '80', '1B', '36']
        word_array = arrange_word(self.key)
        
        
        while b < 11:
            c= 0
            # shift words left:
            shifted_values = shift_words(w_arr_to_string(word_array))
            
            if b ==0:
                round_keys.append(w_arr_to_string(word_array))
                
            else:
                # substitute each word into s_box
                s_box_values = []
                for i in range(len(shifted_values)):
                    s_box_values .append(word_s_box_sub(shifted_values[i]))
                
                # padding round_constant
                
                p_con = round_constants[b-1] +'000000' 
                 
                # add round constant to word and remove the last word
                
                while c < len(s_box_values):
                    temp_word = ''
                    if c == 3:
                        
                        value = binary_to_hex(xor(hex_to_binary(s_box_values[c]),hex_to_binary(p_con))) 
                        temp_word = temp_word + value
                        
                    c+=1
                
                

                
                # get words from xor 
                
                
                round_word_arr = get_key_words(temp_word,word_array)
                round_key = ''.join(round_word_arr)
                round_keys.append(round_key)
                word_array = arrange_word(round_key)
                
            
            b+=1
        return round_keys
                

               


             
        
        




