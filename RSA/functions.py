from random import choice
from bit_encryption_functions import *

from bit_encryption_functions import hex_to_dec, string_to_hex
def get_whole_number(float):
    whole_num = ''
    i = 0
    while float[i] != '.':
        whole_num = f"{whole_num}{float[i]}"
        i+=1
    return whole_num

def mod(a,b):
    """CALCULATE THE MODULUS OF TWO NUMBERS"""
    modulus = a % b
    return modulus
def string_to_decimal(string):
    
    
    values = []
    for i in string:
        v = ord(i)
        values.append(v)
    i = len(values)-1
    decimal = ''
    
    for b in values:
        v = (b * pow(256,i))
        
        decimal  = decimal + str(v) +  "+" 
        
        i-=1
    return decimal

def hex_padding(hex,length):
    while len(hex) < int(length):
        hex = hex + '0'
    return hex


    





def multiplication_modulo_8(a):
    resedues = []
    for i in range(0,8):
        v = mod((i*a),8)
        resedues.append(v)
    return resedues
    


def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def Eulers_totient(x):
    relatively_prime_nums = []
    for i in range(int(x)):
        if gcd(x,i) == 1:
            relatively_prime_nums.append(i)
    
    eulers_totient_value = len(relatively_prime_nums)
    return eulers_totient_value
def miller_rabin(num):
    # determine k 
    num = int(num)
    c = 1 
    temp = int(num) - 1
    temp_factor = int(get_whole_number(str(temp/2)))

    while True:
        if temp_factor % 2 == 0:
            temp_factor = int(get_whole_number(str(temp_factor/2)))
            c+=1
        else:
            q = temp_factor
            k = c
            break
    for i in range(40):

        nums = list(range(2,num-2))
        
        random_num = choice(nums)
        test_value = (pow(random_num,q) % (int(num)))
        
        if test_value == 1 or test_value == temp:
            return True
        else:   
            while k != (temp):
                
                test_value = (test_value * test_value) % num
                k*=2
                if (test_value == temp):
                    
                    return True
                else:

                    break
    return  False
            

  
   







