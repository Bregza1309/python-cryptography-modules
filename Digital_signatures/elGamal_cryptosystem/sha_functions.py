from bit_encryption_functions import *

def sha_padding(string):
    hex_string = string_to_hex(string)
    
    bin_string = hex_to_binary(hex_string)
    # padd to a length congruent to 896(mod 1024)
    b = len(bin_string)
    
    while True:
        
        b+=1    
        if b % 1024 == 896 :
            
            break
            
           
        
            
        
    pad_string_length = b - len(bin_string) -1
    
    bin_string = bin_string + '1'
    b = 0
    while b < pad_string_length:
        bin_string = bin_string + '0'
        b+=1
    res_hex = binary_to_hex(bin_string)
    # pad length to the message block
    block_length = len(hex_string) * 4
    hex_length = binary_to_hex(dec_to_binary(block_length))
    #padd hex_to 128 bits
    while len(hex_length) < 32:
        hex_length = '0' + hex_length
    # message block
    msg_block = res_hex + hex_length
    return msg_block

def ROTR(n,x):
    n = int(n)
    bin_x = hex_to_binary(x)
    
    for i in range(n):
        temp = bin_x[-1] + bin_x[:-1]
        
        bin_x = temp
    
    temp_hex = binary_to_hex(temp)
    return temp_hex
def SHR(n,x):
    n = int(n)
    bin_x = hex_to_binary(x)
    
    for i in range(n):
        temp = '0' + bin_x[:-1] 
        
        bin_x = temp 
    
    temp_hex = binary_to_hex(temp)
    return temp_hex

def sigma_sum512_0(x):
    j = ROTR(1,x)
    p = ROTR(8,x)
    n = SHR(7,x)
    
    t_param = xor(j,p)
    t_param = xor(t_param,n)
    return t_param
def sigma_sum512_1(x):
    a = ROTR(19,x)
    k = ROTR(61,x)
    
    c = SHR(6,x)
    
    f_param = xor(a,k)
    f_param = xor(f_param,c)
    return f_param
def sha_word_processing(block):
    words = []
    b = 0
    while b < len(block):
        words.append(block[b:b+16])
        b += 16
    b = 16
    
    while b < 80:
        
        
        
        
        
        
        res_word = addition_mod(sigma_sum512_1(words[b-2]),words[b-16])
        res_word = addition_mod(res_word,words[b-7])
        res_word = addition_mod(res_word,sigma_sum512_0(words[b-15]))
        
        words.append(res_word)
        b+=1
    return words

def hex_and(x,y):
    x_bin = hex_to_binary(x)
    y_bin = hex_to_binary(y)
    and_value = ''
    b = 0
    while b < len(x_bin):
        if x_bin[b]  == '1':
            if y_bin[b] == '1':
                
                and_value = and_value + '1'
            else:
                and_value = and_value + '0'
        else:
            and_value = and_value + '0'
        b+=1
    and_hex = binary_to_hex(and_value)
    return and_hex

def hex_not(x):
    x_bin = hex_to_binary(x)
    not_value = ''
    for b in x_bin:
        if b == '1':
            not_value = not_value + '0'
        else:
            not_value = not_value + '1'
    hex_not_value = binary_to_hex(not_value)
    return hex_not_value

        
def maj(a,b,c):
    # (a and b ) + (a and c) + (b and c)
    x = hex_and(a,b)
    z = hex_and(a,c)
    k = hex_and(c,b)
    
    y = xor(x,z)
    y = xor(y,k)
    return y

def ch(e,f,g):
    x = hex_and(e,f)
    
    not_e = hex_not(e)
    
    k = hex_and(not_e,g)
    
    y = xor(x,k)
    return y
def sum512_0(x):
    f = ROTR(28,x)
    k = ROTR(34,x)
    h = ROTR(39,x)
    y = xor(f,k)
    y = xor(y,h)
    return y 

def sum512_1(x):
    f = ROTR(14,x)
    k = ROTR(18,x)
    h= ROTR(41,x)
    y = xor(f,k)
    y = xor(y,h)
    return y 

def addition_mod(x,y):
    x = hex_to_binary(x)
    y = hex_to_binary(y)
    x = reverse_binary(x)
    y = reverse_binary(y)
    carry = 0
    results = ''
    for b in range(len(x)):
        if x[b] == '0' and y[b] == '0':
            if carry == 0:
                
                results = results + '0'
            else:
                results = results + '1'
                carry = 0
        elif x[b] == '1' and y[b] == '0':
            if carry == 0:
                
                results = results + '1'
            else:
                results = results + '0'
                carry = 1
        elif x[b] == '0' and y[b] == '1':
            if carry == 0:
                
                results = results + '1'
            else:
                results = results + '0'
                carry = 1
        elif x[b] == '1' and y[b] == '1':
            if carry == 0:
                
                results = results + '0'
                carry = 1
            else:
                results = results + '1'
                carry = 1
    
    if carry == 1:
        results = results + '1'
        
        temp_bin = reverse_binary(results)
        reduced_value = temp_bin[1:]
        
        return binary_to_hex(reduced_value)
    else:
        
        return binary_to_hex(reverse_binary(results))
       
    


  