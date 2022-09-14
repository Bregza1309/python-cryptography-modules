from functions import binary_to_hex
from functions import hex_to_binary as h_b
from functions import permutate
from des_key  import GET_DES_ENCRYPTION_KEY
from functions import xor
from functions import s_box_substitution as s_b
from functions import string_to_hex,hex_to_string


class DES_ENCRYPTION:
    def __init__(self,plain_text,key):
        # initialize des variables
        self.hex = string_to_hex(plain_text)   
        self.plaintext = h_b(self.hex)          
        self.initial_permutation = [58, 50, 42, 34, 26, 18, 10, 2,
                                    60 ,52 ,44 ,36, 28 ,20 ,12 ,4,
                                    62 ,54, 46, 38, 30, 22, 14, 6,
                                    64 ,56 ,48 ,40 ,32 ,24 ,16 ,8,
                                    57 ,49, 41, 33, 25, 17, 9, 1,
                                    59 ,51 ,43 ,35 ,27 ,19 ,11 ,3,
                                    61 ,53 ,45 ,37 ,29 ,21 ,13 ,5,
                                    63 ,55, 47, 39, 31, 23, 15, 7]

        self.inverse_initial_permutation =  [40, 8, 48, 16, 56 ,24, 64, 32,
                                            39 ,7 ,47 ,15 ,55 ,23 ,63 ,31,
                                            38 ,6 ,46, 14, 54, 22, 62, 30,
                                            37, 5, 45 ,13 ,53 ,21 ,61 ,29,
                                            36, 4, 44, 12, 52, 20, 60, 28,
                                            35 ,3 ,43 ,11 ,51 ,19 ,59 ,27,
                                            34 ,2 ,42, 10, 50, 18, 58, 26,
                                            33 ,1 ,41 ,9 ,49 ,17 ,57 ,25
                                            ]
        self.expansion_permutation_table = [32,1,2,3,4,5,
                                            4,5,6,7,8,9,
                                            8,9,10,11,12,13,
                                            12,13,14,15,16,17,
                                            16,17,18,19,20,21,
                                            20,21,22,23,24,25,
                                            24,25,26,27,28,29,
                                            28,29,30,31,32,1]
        self.init_string = permutate(self.plaintext,self.initial_permutation,len(self.plaintext)) 
        self.right_bits = self.init_string[32:64]
        self.left_bits = self.init_string[:32]
        self.keys =  GET_DES_ENCRYPTION_KEY(key).get_encryption_round_key()
        
        
    
    def encrypt(self): 
        #16 rounds encryption
        for b in range(0,16):
                expanded_bits =  permutate(self.right_bits,self.expansion_permutation_table,48)
                
                round_keys = self.keys
                key_1 = round_keys[b] 
                value = xor(expanded_bits,key_1)

                
                bin_arr = []
                c = 0 
                while c < len(value):
                        bin_arr.append(value[c:c+6])
                        c += 6

                s_box_string = s_b(bin_arr)

                
                #final permutation table
                permutation_table =     [16, 7, 20, 21, 29, 12, 28, 17,
                                        1 ,15 ,23 ,26 ,5 ,18, 31 ,10,
                                        2 ,8 ,24 ,14, 32, 27, 3 ,9,
                                        19 ,13 ,30 ,6 ,22 ,11, 4 ,25]
                # permutate and record value
                perm_bits = permutate(s_box_string,permutation_table,len(s_box_string))
                # get final permutation string
                
                # xor left bits and final_permutation_bits to get cypher text
                right_ciphertext = xor(self.left_bits,perm_bits)
                self.left_bits = self.right_bits
                print(f"L{b+1} : {self.left_bits}")
                print(f"R{b+1} : {right_ciphertext} \n")
                self.right_bits = right_ciphertext
        # inverse permutation table
        inverse_perm = [40 ,8, 48, 16, 56, 24, 64, 32,
                        39 ,7, 47 ,15 ,55 ,23 ,63 ,31,
                        38 ,6 ,46, 14, 54, 22, 62, 30,
                        37, 5, 45, 13, 53, 21, 61 ,29,
                        36, 4 ,44, 12, 52, 20, 60, 28,
                        35 ,3 ,43 ,11 ,51 ,19 ,59 ,27,
                        34 ,2 ,42, 10, 50, 18, 58, 26,
                        33 ,1, 41, 9 ,49 ,17 ,57 ,25]
        round16_ciphertext = self.right_bits + self.left_bits
        ciphertext = permutate(round16_ciphertext,inverse_perm,len(round16_ciphertext))                               
        print(f"CIPHERTEXT : {binary_to_hex(ciphertext)}")
        return binary_to_hex(ciphertext)
            

my_des = DES_ENCRYPTION('TateND@','muchesa')


print(my_des.encrypt())

