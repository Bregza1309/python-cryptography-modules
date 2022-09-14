from functions import string_to_hex,hex_to_string
from functions import hex_to_binary as h_x
from functions import permutate
from functions import shift_left

class GET_DES_ENCRYPTION_KEY:
    def __init__(self,key):
        self.key_hex = string_to_hex(key)
        self.key64 = h_x(self.key_hex)
        self.input_key = [  1,2,3,4,5,6,7,
                            9 ,10, 11, 12, 13, 14, 15,
                            17, 18, 19 ,20 ,21 ,22 ,23 ,
                            25 ,26, 27, 28, 29, 30, 31, 
                            33 ,34, 35, 36 ,37 ,38 ,39 ,
                            41 ,42, 43 ,44 ,45 ,46, 47,
                            49 ,50, 51 ,52 ,53 ,54 ,55 ,
                            57 ,58 ,59, 60, 61, 62 ,63]

        self.PC1 = [57, 49, 41, 33, 25, 17, 9,
                    1 ,58 ,50, 42 ,34 ,26 ,18,
                    10 ,2 ,59, 51, 43, 35, 27,
                    19 ,11 ,3 ,60 ,52 ,44 ,36,
                    63 ,55, 47, 39, 31, 23, 15,
                    7 ,62 ,54 ,46 ,38 ,30 ,22,
                    14 ,6 ,61, 53, 45, 37, 29,
                    21 ,13, 5, 28 ,20 ,12, 4]
        
        self.key56_PC1 = permutate(self.key64,self.PC1,56)
        self.right_bits = self.key56_PC1[28:56]
        self.left_bits = self.key56_PC1[:28]
        

    def get_encryption_round_key(self):
        shift_value = [1, 1, 2, 2 ,2 ,2 ,2 ,2 ,1 ,2 ,2 ,2 ,2 ,2 ,2, 1]
        rk = []
        PC2 = [ 14, 17, 11, 24, 1, 5, 3, 28,
                15 ,6 ,21 ,10 ,23, 19 ,12 ,4,
                26 ,8, 16, 7, 27, 20, 13, 2,
                41 ,52 ,31 ,37, 47, 55 ,30 ,40,
                51 ,45, 33, 48, 44, 49, 39, 56,
                34 ,53 ,46 ,42 ,50 ,36 ,29 ,32]

        # loop to shift right and left bits then permutate
        for b in range(0,16):        
                        
            shifted_string_left = shift_left(self.left_bits,shift_value[b])
            shifted_string_right = shift_left(self.right_bits,shift_value[b])
            key_string = shifted_string_left + shifted_string_right
            round_key = permutate(key_string,PC2,48)
            # record all round keys in an array
            rk.append(round_key)
            self.right_bits = shifted_string_right
            self.left_bits = shifted_string_left


        return rk
    def get_decryption_round_key(self):
        shift_value = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
        rk = []
        PC2 = [ 14, 17, 11, 24, 1, 5, 3, 28,
                15 ,6 ,21 ,10 ,23, 19 ,12 ,4,
                26 ,8, 16, 7, 27, 20, 13, 2,
                41 ,52 ,31 ,37, 47, 55 ,30 ,40,
                51 ,45, 33, 48, 44, 49, 39, 56,
                34 ,53 ,46 ,42 ,50 ,36 ,29 ,32]
        j = 0
        while j < len(shift_value):
            shifted_string_left = shift_left(self.left_bits,shift_value[j])
            shifted_string_right = shift_left(self.right_bits,shift_value[j])
            key_string = shifted_string_left + shifted_string_right
            round_key = permutate(key_string,PC2,48)
            # record all round keys in an array
            rk.append(round_key)
            self.right_bits = shifted_string_right
            self.left_bits = shifted_string_left
            j +=1
      
     
        
        
        return rk[::-1]





   
    





