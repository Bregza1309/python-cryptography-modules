from bit_encryption_functions import *

def shift_right(k,n):
    s = ''
    k_byte = []
    g = 0
    while g < len(k):
        k_byte.append(k[g:g+2])
        g+=2
    s = ''
    for i in range(n):
        s = s +  str(k_byte[-1])
        for b in range(0,len(k_byte)-1):
            s = s + k_byte[b]
           
        k = s
        s = ''
    return k
def shift_rows_inverse(hex):
    hex_arr = correct_array(hex)
    
    i = 0
    b = 0
    shifted_row = ''
    s_row_string = ''
    # shift rows inverse function
    shift_schedule = [0,1,2,3]
    while i < len(hex_arr):
        temp = ''.join(hex_arr[i])
        
        if shift_schedule[i] == 1:
            #shift once
            shift_value = shift_right(temp,shift_schedule[i]) 
            
            s_row_string = s_row_string + shift_value
            
        elif shift_schedule[i] == 2:
            #shift two times
            shift_value = shift_right(temp,shift_schedule[i]) 
            temp = shift_value
            shift_value = shift_right(temp,shift_schedule[i]) 
            s_row_string = s_row_string + shift_value
        elif shift_schedule[i] == 3:
            # shift three times
            shift_value = shift_right(temp,shift_schedule[i]) 
            temp = shift_value
            shift_value = shift_right(temp,shift_schedule[i]) 
            temp = shift_value
            shift_value = shift_right(temp,shift_schedule[i]) 
            s_row_string = s_row_string + shift_value
        else:
            s_row_string = s_row_string + str(temp)
        i+=1
        
    return w_arr_to_string(correct_array(s_row_string))
def s_box_inverse_substitution(hex):
    inverse_s_box = [['52', '09', '6A', 'D5', '30', '36', 'A5', '38' ,'BF' ,'40', 'A3', '9E' ,'81', 'F3', 'D7', 'FB'],
                     ['7C', 'E3', '39', '82', '9B', '2F', 'FF', '87', '34', '8E', '43', '44' ,'C4', 'DE', 'E9', 'CB'],
                     ['54', '7B', '94', '32', 'A6', 'C2', '23', '3D', 'EE', '4C', '95', '0B' ,'42' ,'FA' ,'C3', '4E'],
                     ['08', '2E', 'A1', '66', '28', 'D9', '24' ,'B2', '76', '5B', 'A2', '49', '6D', '8B', 'D1', '25'],
                     ['72', 'F8', 'F6', '64', '86', '68' ,'98', '16', 'D4', 'A4', '5C', 'CC', '5D', '65', 'B6' ,'92'],
                     ['6C', '70', '48', '50' ,'FD ','ED', 'B9', 'DA', '5E', '15' ,'46', '57', 'A7' ,'8D', '9D', '84'],
                     ['90', 'D8', 'AB', '00', '8C' ,'BC', 'D3' ,'0A', 'F7', 'E4', '58', '05', 'B8', 'B3', '45', '06'],
                     ['D0', '2C' ,'1E' ,'8F' ,'CA', '3F', '0F' ,'02', 'C1' ,'AF', 'BD', '03', '01', '13' ,'8A', '6B'],
                     ['3A', '91' ,'11', '41' ,'4F', '67', 'DC', 'EA', '97' ,'F2', 'CF', 'CE' ,'F0', 'B4', 'E6' ,'73'],
                     ['96' ,'AC', '74', '22', 'E7', 'AD', '35' ,'85' ,'E2', 'F9', '37', 'E8', '1C' ,'75', 'DF', '6E'],
                     ['47', 'F1', '1A', '71', '1D', '29', 'C5', '89', '6F', 'B7', '62', '0E', 'AA', '18', 'BE', '1B'],
                     ['FC', '56', '3E', '4B', 'C6' ,'D2', '79', '20', '9A', 'DB', 'C0', 'FE', '78', 'CD', '5A', 'F4'],
                     ['1F', 'DD' ,'A8', '33','88' ,'07', 'C7',  '31' ,'B1', '12', '10', '59', '27' ,'80', 'EC', '5F'],
                     ['60' ,'51', '7F', 'A9', '19' ,'B5', '4A', '0D' ,'2D', 'E5', '7A', '9F', '93', 'C9' ,'9C', 'EF'],
                     ['A0', 'E0', '3B', '4D', 'AE', '2A', 'F5', 'B0', 'C8', 'EB', 'BB', '3C', '83', '53', '99', '61'],
                     ['17', '2B', '04', '7E', 'BA' ,'77','D6' ,'26', 'E1', '69', '14', '63', '55', '21', '0C', '7D']]
    b = 0
    res_string = ''
    while b < len(hex):
        temp = hex[b:b+2]
        
        row = int(hex_to_dec(temp[0]))
        column = int(hex_to_dec(temp[1]))
        s_value = inverse_s_box[row][column]
        
       
        res_string = res_string + s_value
        b+=2
    return res_string
def get_whole_number(float):
    whole_num = ''
    i = 0
    while float[i] != '.':
        whole_num = f"{whole_num}{float[i]}"
        i+=1
    return whole_num

        
    
def hex_multiplication(a,b):
    # divide given hex by 2
    var_1 = int(hex_to_dec(b))
    factor = int(get_whole_number(str(var_1 /2))) 
    mult_factors = []
    temp = hex_to_binary(a)
    mult_factors.append(temp)
    poly_value = var_1 % 8 
    # for multiple_powers of  of x
    # for odd powers of x
                 
    for i in range(factor):
        
        
        if factor == 1:

            shifted_value = shift_left_bits(temp,1)
            
            if temp[0] == '1':
                value = xor(shifted_value,'00011011')
                return xor(value,temp)
            else:
                return xor(shifted_value,temp)
        elif factor > 1:
            
            shifted_value = shift_left_bits(temp,1)
            
            if temp[0] == '1':
                value = xor(shifted_value,'00011011')
                temp = value
                mult_factors.append(value)
            else:
                mult_factors.append(shifted_value)
                temp = shifted_value
    
    j = 0
    real_fact = []
    
    
    
    
    
    rev_b = reverse_binary(hex_to_binary(b))
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
    

    
def mix_columns_inverse(hex):
    hex_arr = word_arr(w_arr_to_string(correct_array(hex)))
    res_arr = [[],[],[],[]]
    
   # arrange hex into an array
    for i  in range(0,len(hex_arr)):
        temp = hex_arr[i][0]
        b = 0
        while b < len(temp):
            res_arr[i].append(temp[b:b+2])
            b+=2
    
    results = [[],[],[],[]]
    b = 0
    
    while b < 4:
        z = 0
        while z < 4:
                   
            if z == 0:
                
                results[z].append( binary_to_hex(xor(hex_multiplication(res_arr[0][b],'0E'),hex_multiplication(res_arr[1][b],'0B'),hex_multiplication(res_arr[2][b],'0D'),hex_multiplication(res_arr[3][b],'09'))))
                
            elif z == 1 :
                results[z].append( binary_to_hex(xor(hex_multiplication(res_arr[0][b],'09'),hex_multiplication(res_arr[1][b],'0E'),hex_multiplication(res_arr[2][b],'0B'),hex_multiplication(res_arr[3][b],'0D'))))
                
            elif z == 2:
                results[z].append( binary_to_hex(xor(hex_multiplication(res_arr[0][b],'0D'),hex_multiplication(res_arr[1][b],'09'),hex_multiplication(res_arr[2][b],'0E'),hex_multiplication(res_arr[3][b],'0B'))))
                
            elif z == 3:
                results[z].append( binary_to_hex(xor(hex_multiplication(res_arr[0][b],'0B'),hex_multiplication(res_arr[1][b],'0D'),hex_multiplication(res_arr[2][b],'09'),hex_multiplication(res_arr[3][b],'0E'))))
                
            z+=1
        b+=1
    b = 0
    final_value = ''
    while b < len(results):
        final_value = final_value + ''.join(results[b])
        b+=1

    return w_arr_to_string(correct_array(final_value))
def bin_to_dec(bin):
    reversed_string = reverse_binary(bin)
    i = 0
    value = 0
    for b in range(0,len(reversed_string)):
        i = 2**b
        if reversed_string[b] == '1':
            
            
            value += i
        else:
            value += 0
    return value

def hex_to_string(hex):
    binary_value = hex_to_binary(hex)
    string_bytes = []
    str_value = ''
    b = 0

    while b < len(binary_value):
        string_bytes.append(binary_value[b:b+7])
        b += 7
    b = 0
    while b < len(string_bytes):
        str_value = str_value + chr(bin_to_dec(string_bytes[b]))
        b +=1
    return str_value




                
            
