from bit_encryption_functions import *
from AES_DECRYPTION_FUNCTION import *
def gf128_multiplication(x = str(),y  = str()):
    # padd from byte to 128_bits
    x = x[::-1]
    y = y[::-1]
    while len(x) < 32:
         x = x + '0'
         y = y + '0' 
    y = y[::-1]
    x = x[::-1]
    
    reduction = dec_to_binary('135')
    
    reduction = reduction[::-1]
    while len(reduction) < 128:
        reduction = reduction + '0'
    reduction = reduction[::-1]
    
    # divide given hex by 2 to get coeficients of the polynomial
    var_1 = int(hex_to_dec(y))
    
    factor = int(get_whole_number(str(var_1 /2))) 
    mult_factors = []
    temp = hex_to_binary(x)
    
    mult_factors.append(temp)
     
    # for multiple_powers of  of x
    # for odd powers of x
                 
    for i in range(factor):
        
        
        if factor == 1:

            shifted_value = shift_left_bits(temp,1)
            
            if temp[0] == '1':
                value = xor(shifted_value,reduction)
                return xor(value,temp)
            else:
                return xor(shifted_value,temp)
        elif factor > 1:
            
            shifted_value = shift_left_bits(temp,1)
            
            if temp[0] == '1':
                value = xor(shifted_value,reduction)
                temp = value
                mult_factors.append(value)
            else:
                mult_factors.append(shifted_value)
                temp = shifted_value
    
    j = 0
    real_fact = []

    rev_b = reverse_binary(hex_to_binary(y))
    
    h = 0
    bit_positions = []
    while h < len(rev_b):
        if rev_b[h] == '1':
            bit_positions.append(h)
        h+=1

    while j < len(bit_positions):
        
        real_fact.append(mult_factors[bit_positions[j]])
        
        
        j+=1
    
    h = 1

    temp_1 = real_fact[0]
    while h < len(real_fact):
        temp_1 = xor(temp_1,real_fact[h])
        h+=1
    return temp_1
         

