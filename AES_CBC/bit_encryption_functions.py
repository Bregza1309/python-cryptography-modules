def arrange_word(hex):
    hex_arr = word_arr(hex)
    
    word_array = [[],[],[],[]]
    for i in range(len(hex_arr)):
        temp = hex_arr[i][0]
        b = 0
        while b < len(temp):
            word_array[i].append(temp[b:b+2])
            b+=2
    return word_array

def string_to_hex(string):
    bin_string = ''.join(format(b,'08b') for b in bytearray(string,encoding="utf-8"))
    while True:
        if len(bin_string)<64:
            bin_string = bin_string + '0'
        else:
            break
    hex_string = binary_to_hex(bin_string)
    return hex_string

def binary_to_hex(binary):
    hex_key ={'0':'0000',
               '1':'0001',
               '2':'0010',
               '3':'0011',
               '4':'0100',
               '5':'0101',
               '6':'0110',
               '7':'0111',
               '8':'1000',
               '9':'1001',
               'A':'1010',
               'B':'1011',
               'C':'1100',
               'D':'1101',
               'E':'1110',
               'F':'1111', }

    
    bin_list =[]
    hex_list = []
    hex_str = ""
    i = 0
    while i<len(binary):
        bin_list.append(binary[i:i+4])
        i+= 4
    i = 0
    while i < len(bin_list):
        for key,value in hex_key.items():
            if bin_list[i] == value:
                hex_list.append(key)
                hex_str = ''.join(hex_list)
        i+=1
    

    
    return hex_str




def hex_to_binary(hex):
    hex_key ={'0':'0000',
               '1':'0001',
               '2':'0010',
               '3':'0011',
               '4':'0100',
               '5':'0101',
               '6':'0110',
               '7':'0111',
               '8':'1000',
               '9':'1001',
               'A':'1010',
               'B':'1011',
               'C':'1100',
               'D':'1101',
               'E':'1110',
               'F':'1111', }
    bin_list = []
    bin_string = ''
    
    for i in hex:
        for h,b in hex_key.items():
            if i == h :
                bin_list.append(b)
                bin_string = ''.join(bin_list)

    
    return bin_string

def xor(a,b,c= None , d = None):
    xor_list = []
    xor_string = ''
    i = 0
    while i < (len(a) and len(b)):
        if a[i]== b[i]:
            
            xor_list.append('0')
        else:
            xor_list.append('1')
        xor_string  = ''.join(xor_list)
        i += 1
    if c :
        string = ''
        i = 0
        while i < (len(c) and len(xor_string)):
            if c[i]== xor_string[i]:
                
                string = string + '0'
            else:
                xor_list.append('1')
                string = string + '1'
            i += 1
    if d :
        xor_string = ''
        i = 0
        while i < (len(a) and len(b)):
            if d[i]== string[i]:
                
                xor_string = xor_string + '0'
            else:
                xor_string = xor_string + '1'
           
            i += 1
    return xor_string



def permutate(k,table,n):
    
    per_string = ''
    for i in range(0,n):
        per_string = per_string + k[table[i] -1]
    permuted_string = per_string
    return permuted_string
    

def shift_left(k,n):
    s = ''
    for i in range(n):
        for b in range(1,len(k)):
            s = s + k[b]
        s = s + k[0]    
        k = s
        s = ''
    return k

def hex_to_dec(hex):
    bin = hex_to_binary(hex)
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


def reverse_binary(bin):
    bin_string = str(bin)
    i = len(bin_string)-1
    reversed_bin = ''
    while i >= 0:
        reversed_bin = reversed_bin + bin_string[i]
        i-=1
    return reversed_bin

def dec_to_binary(dec):
    my_dec = int(dec)
    binary = ''

    while my_dec > 0 :
        remainder = my_dec % 2
        
        binary = binary +  str(remainder)
        my_dec = my_dec/2
        string_dec = str(my_dec)
        i = 0
        new_dec = ''
        while string_dec[i] != '.':
            new_dec = new_dec + string_dec[i]
            i+= 1
        my_dec = int(new_dec)
    while len(binary) % 8 !=0:
        binary = binary + '0'
    return reverse_binary(binary)
        





#s_box substitution
def s_box_sub(hex):
    
    
    s_box = [['63', '7C', '77' ,'7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'],
             ['CA', '82', 'C9', '7D', 'FA' ,'59', '47', 'F0' ,'AD' ,'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'],
             ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71' ,'D8' ,'31', '15'],
             ['04', 'C7' ,'23', 'C3', '18' ,'96', '05', '9A' ,'07' ,'12', '80', 'E2', 'EB', '27', 'B2', '75'],
             ['09' ,'83', '2C' ,'1A', '1B', '6E', '5A', 'A0' ,'52', '3B', 'D6', 'B3', '29', 'E3', '2F' ,'84'],
             ['53', 'D1', '00', 'ED', '20', 'FC' ,'B1' ,'5B', '6A', 'CB' ,'BE' ,'39' ,'4A', '4C' ,'58', 'CF'],
             ['D0', 'EF' ,'AA' ,'FB', '43', '4D' ,'33', '85', '45', 'F9' ,'02', '7F' ,'50' ,'3C' ,'9F', 'A8'],
             ['51', 'A3', '40', '8F', '92', '9D' ,'38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'],
             ['CD' ,'0C' ,'13', 'EC', '5F' ,'97', '44' ,'17' ,'C4' ,'A7', '7E', '3D' ,'64', '5D', '19', '73'],
             ['60', '81', '4F' ,'DC' ,'22', '2A' ,'90' ,'88', '46' ,'EE' ,'B8' ,'14', 'DE' ,'5E' ,'0B', 'DB'],
             ['E0', '32' ,'3A' ,'0A' ,'49', '06' ,'24' ,'5C' ,'C2' ,'D3' ,'AC', '62', '91', '95', 'E4', '79'],
             ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A' ,'AE', '08'],
             ['BA', '78' ,'25' ,'2E' ,'1C' ,'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'],
             ['70', '3E', 'B5', '66' ,'48', '03', 'F6', '0E', '61', '35', '57' ,'B9', '86', 'C1', '1D', '9E'],
             ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55' ,'28', 'DF'],
             ['8C', 'A1' ,'89', '0D', 'BF', 'E6' ,'42' ,'68', '41', '99' ,'2D' ,'0F' ,'B0', '54', 'BB', '16']]
    k = 0
    sub_string = ''
    while k < len(hex):
        temp = hex[k:k+2]
        
        row = int(hex_to_dec(temp[0]))
        column = int(hex_to_dec(temp[1]))
        s_box_value = s_box[row][column]
        sub_string = sub_string + s_box_value
        k += 2
    return sub_string

def word_arr (word):
    word_array = [[],[],[],[]]
    i = 0
    b = 0
    while b < len(word):
        word_array[i].append(word[b:b+8])
        i+=1
        b+=8
    return word_array

def shift_left(k,n):
    s = ''
    k_byte = []
    g = 0
    while g < len(k):
        k_byte.append(k[g:g+2])
        g+=2
    for i in range(n):
        for b in range(1,len(k_byte)):
            s = s + k_byte[b]
        s = s +  str(k_byte[0])   
        k = s
        s = ''
    return k
def shift_rows(hex):
    hex_arr = word_arr(hex)
    i = 0
    b = 0
    shifted_row = ''
    s_row_string = ''
    shift_schedule = [0,1,2,3]
    while i < len(hex_arr):
        temp = hex_arr[i]
        if shift_schedule[i] == 1:
            shift_value = shift_left(temp[0],shift_schedule[i]) 
            
            s_row_string = s_row_string + shift_value
        elif shift_schedule[i] == 2:
            shift_value = shift_left(temp[0],shift_schedule[i]) 
            temp[0] = shift_value
            shift_value = shift_left(temp[0],shift_schedule[i]) 
            s_row_string = s_row_string + shift_value
        elif shift_schedule[i] == 3:
            shift_value = shift_left(temp[0],shift_schedule[i]) 
            temp[0] = shift_value
            shift_value = shift_left(temp[0],shift_schedule[i]) 
            temp[0] = shift_value
            shift_value = shift_left(temp[0],shift_schedule[i]) 
            s_row_string = s_row_string + shift_value
        else:
            s_row_string = s_row_string + str(temp[0])
        i+=1
        
    return s_row_string

def bits_multiplication(a,b):
    # convert to binary
    binary = hex_to_binary(a)
    #shift left
    if b == '02':

        shifted_bin = shift_left_bits(binary,1)
        value = ''
        if binary[0] == '1':
            value = xor(shifted_bin,'00011011')
            return value
        else:
            return shifted_bin
    elif b == '03':
        # multiply by 02 and xor with original bits
        shifted_bin = shift_left_bits(binary,1)
        value = ''
        if binary[0] == '1':
            value = xor(shifted_bin,'00011011')
            
        else:
            value =  shifted_bin
        x = xor(value,binary)
        return x





def mix_columns(hex):
    hex_arr = word_arr(hex)
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
                
                results[z].append( binary_to_hex(xor(bits_multiplication(res_arr[0][b],'02'),bits_multiplication(res_arr[1][b],'03'),hex_to_binary(res_arr[2][b]),hex_to_binary(res_arr[3][b]))))
                
            elif z == 1 :
                results[z].append( binary_to_hex(xor(hex_to_binary(res_arr[0][b]),bits_multiplication(res_arr[1][b],'02'),bits_multiplication(res_arr[2][b],'03'),hex_to_binary(res_arr[3][b]))))
                
            elif z == 2:
                results[z].append( binary_to_hex(xor(hex_to_binary(res_arr[0][b]),hex_to_binary(res_arr[1][b]),bits_multiplication(res_arr[2][b],'02'),bits_multiplication(res_arr[3][b],'03'))))    
                
            elif z == 3:
                results[z].append( binary_to_hex(xor(bits_multiplication(res_arr[0][b],'03'),hex_to_binary(res_arr[1][b]),hex_to_binary(res_arr[2][b]),bits_multiplication(res_arr[3][b],'02'))))
                
            z+=1
        b+=1
    b = 0
    final_value = ''
    while b < len(results):
        final_value = final_value + ''.join(results[b])
        b+=1

    return final_value
                
        

def shift_left_bits(k,n):
    s = ''
    for i in range(n):
        for b in range(1,len(k)):
            s = s + k[b]
        s = s + '0'    
        k = s
        s = ''
    return k
def w_arr_to_string(w_arr):
    res_string = ''
    for i in w_arr:
        temp = i
        res_string = res_string + ''.join(temp)
    return res_string

def correct_array(hex):
    hex_arr = arrange_word(hex)
    

    i = 0
    
    
    new_arr = [[],[],[],[]]
    while i < len(hex_arr):
        j = 0
        temp = ''
        while j < len(hex_arr[i]):

            temp = temp + hex_arr[j][i]
            new_arr[i].append(temp)
            temp = ''
            
            j+=1
        
        i+=1
    return new_arr
def creverse_array(hex):
    hex_arr = arrange_word(hex)
    

    i = 0
    
    
    new_arr = [[],[],[],[]]
    while i < len(hex_arr):
        j = 0
        temp = ''
        while j < len(hex_arr[i]):

            temp = temp + hex_arr[j][i]
            new_arr[i].append(temp)
            temp = ''
            
            j+=1
        
        i+=1
    return w_arr_to_string(new_arr)
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
        string_bytes.append(binary_value[b:b+8])
        b += 8
    b = 0
    while b < len(string_bytes):
        str_value = str_value + chr(bin_to_dec(string_bytes[b]))
        b +=1
    return str_value


