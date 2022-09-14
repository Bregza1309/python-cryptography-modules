from bit_encryption_functions import *

def MSB(x):
    return x[0]

def cmac_gf128_multiplication(x):
    reduction_v = hex_padding_("78" , 32)
    reduction_v = reduction_v[::-1]
    
    if len(x) < 32 :
        x = hex_padding_(x,32)
    
    
    temp = binary_to_hex(shift_left_bits(hex_to_binary(x),1))
    if MSB(hex_to_binary(x)) == '0':
        return temp
    else:
        result = xor(temp,reduction_v)
        return result
    
        
         
        
    
print(cmac_gf128_multiplication("E"))