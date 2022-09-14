from random import choice
from datetime import datetime
def get_whole_number(float):
    whole_num = ''
    i = 0
    while float[i] != '.':
        whole_num = f"{whole_num}{float[i]}"
        i+=1
    return int(whole_num)
def linear_congruential_generator(x,m,a,c,end_value):
    random_numbers = []
    for i in range(int(end_value)):
        b = (a*x + c) % m
        random_numbers.append(b)
        x = b
    return random_numbers
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def Blum_Blum_Shub_generator( end_value ,p = None , q = None,seed = None  ):
    if (p and q) == None:
        my_nums = []  
        prime_nums = [] 
             
        for i in range(2,pow(2,11)):
            isPrime = True
            for b in range(2,i):
                
                if i % b == 0:
                    isPrime = False
            if isPrime:
                if i % 4 == 3:

                    prime_nums.append((i))             

        p = choice(prime_nums)
        q = choice(prime_nums)
                    
        
        
    
    n = int(p) * int(q)
    
    s_values = []
    
    for b in range(pow(2,10)):
        
        if  gcd(n,b) == 1:
            s_values.append(b)
    
        if seed == None:
            seed = choice(s_values)
        
        
        results = []
        x = pow(seed,2) % n

        for r in range(int(end_value)):
            x = pow(x,2) % n
            results.append(x% 2)
        
        bin_str = ''
        for b in results:
            bin_str = bin_str + str(b)
        return bin_str                

def get_instaneous_date_and_time():
    now = datetime.now()
    current_date_time = now.strftime("%H%M%S%m%d%Y")
    return current_date_time

def hex_padding(hex,length):
    while len(hex) < int(length):
        hex = hex + '0'
    return hex
