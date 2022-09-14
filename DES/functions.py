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
               'a':'1010',
               'b':'1011',
               'c':'1100',
               'd':'1101',
               'e':'1110',
               'f':'1111', }

    
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
               'a':'1010',
               'b':'1011',
               'c':'1100',
               'd':'1101',
               'e':'1110',
               'f':'1111', }
    bin_list = []
    bin_string = ''
    
    for i in hex:
        for h,b in hex_key.items():
            if i == h :
                bin_list.append(b)
                bin_string = ''.join(bin_list)

    
    return bin_string

def xor(a,b):
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
    if len(reverse_binary(binary)) < 4:
        if len(reverse_binary(binary))< 3:
            if len(reverse_binary(binary)) <2 :
                if len(reverse_binary(binary)) <1:
                    return  '0000'+reverse_binary(str(binary))
                return  '000'+reverse_binary(str(binary))
            return  '00'+reverse_binary(str(binary))
        return  '0'+reverse_binary(str(binary))
    else:
        return  reverse_binary(str(binary))


def s_box_substitution(bits6arr):

        s_boxes = [ [ [4 ,4, 13, 1, 2, 15, 11, 8 ,3 ,10, 6, 12, 5, 9 ,0 ,7],
                        [0 ,15 ,7 ,4 ,14, 2 ,13, 1 ,10, 6 ,12 ,11, 9, 5 ,3, 8],
                        [4, 1, 14, 8 ,13 ,6 ,2, 11, 15, 12, 9, 7 ,3 ,10, 5 ,0],
                       [ 15 ,12 ,8 ,2 ,4 ,9 ,1 ,7 ,5 ,11, 3 ,14 ,10 ,0 ,6 ,13]],

                            [[15, 1, 8, 14 ,6 ,11, 3, 4, 9, 7 ,2 ,13, 12 ,0, 5, 10],
                            [3 ,13 ,4 ,7 ,15 ,2 ,8 ,14 ,12, 0 ,1 ,10, 6, 9 ,11 ,5],
                            [0 ,14, 7 ,11, 10, 4 ,13, 1 ,5 ,8 ,12, 6, 9, 3, 2, 15],
                            [13 ,8 ,10, 1, 3, 15 ,4 ,2 ,11 ,6 ,7 ,12 ,0 ,5 ,14 ,9]
                            ],
                    
                            [[10, 0 ,9 ,14, 6 ,3 ,15, 5 ,1 ,13 ,12, 7, 11, 4, 2, 8],
                            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                            [13, 6 ,4 ,9 ,8 ,15, 3, 0 ,11 ,1 ,2, 12, 5, 10 ,14, 7],
                            [1, 10 ,13, 0, 6, 9, 8, 7, 4 ,15, 14, 3 ,11, 5, 2, 12]
                           ],
                            
                           [ [7 ,13 ,14 ,3 ,0 ,6 ,9 ,10, 1, 2, 8, 5, 11, 12, 4, 15],
                           [ 13, 8, 11, 5, 6 ,15 ,0 ,3 ,4 ,7 ,2 ,12, 1 ,10, 14, 9],
                            [10 ,6 ,9 ,0 ,12, 11, 7 ,13, 15, 1, 3 ,14, 5 ,2 ,8 ,4],
                            [3 ,15, 0 ,6 ,10 ,1, 13, 8, 9, 4, 5, 11 ,12, 7, 2 ,14]
                           ],

                            [[2 ,12, 4 ,1 ,7 ,10 ,11, 6 ,8 ,5 ,3 ,15 ,13 ,0 ,14 ,9],
                            [14, 11, 2 ,12, 4, 7 ,13, 1 ,5 ,0 ,15, 10, 3, 9 ,8 ,6],
                            [4 ,2, 1 ,11 ,10 ,13, 7 ,8 ,15 ,9 ,12 ,5, 6 ,3 ,0 ,14],
                            [11 ,8, 12, 7 ,1 ,14 ,2 ,13, 6, 15, 0, 9, 10, 4 ,5 ,3]
                           ],

                            [ [12 ,1 ,10 ,15 ,9 ,2 ,6 ,8 ,0 ,13, 3 ,4 ,14 ,7 ,5 ,11],
                            [10, 15 ,4 ,2 ,7 ,12 ,9 ,5 ,6 ,1, 13 ,14, 0, 11, 3 ,8],
                            [9 ,14 ,15 ,5 ,2 ,8 ,12, 3, 7, 0 ,4 ,10, 1 ,13 ,11 ,6],
                            [4 ,3 ,2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6 ,0 ,8 ,13]
                           ],

                            [[ 4, 11 ,2 ,14 ,15, 0, 8 ,13 ,3 ,12, 9, 7, 5 ,10 ,6, 1],
                            [13, 0, 11, 7 ,4 ,9, 1 ,10, 14, 3, 5, 12, 2 ,15, 8, 6],
                            [1, 4 ,11 ,13 ,12 ,3 ,7 ,14, 10, 15, 6, 8, 0 ,5 ,9, 2],
                            [6 ,11, 13, 8, 1, 4, 10 ,7, 9 ,5 ,0 ,15, 14, 2 ,3, 12]
                            ],

                            [[13, 2 ,8 ,4 ,6 ,15 ,11 ,1 ,10, 9, 3 ,14 ,5, 0 ,12 ,7],
                            [1, 15, 13, 8, 10, 3 ,7 ,4 ,12, 5 ,6 ,11, 0, 14, 9, 2],
                            [7 ,11 ,4 ,1 ,9 ,12 ,14 ,2 ,0 ,6, 10 ,13 ,15 ,3, 5 ,8],
                            [2 ,1, 14, 7, 4 ,10, 8 ,13, 15 ,12, 9 ,0, 3, 5, 6, 11]]
        ]

        s_box_str = ''
        for b in range(0,len(s_boxes)):
            row = int(bin_to_dec(bits6arr[b][0] + bits6arr[b][5]))
            column = int(bin_to_dec(bits6arr[b][1]+bits6arr[b][2]+bits6arr[b][3]+bits6arr[b][4]))
            s_box_str = s_box_str + dec_to_binary(str(s_boxes[b][row][column]))
        return s_box_str   

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

print(string_to_hex('bregza'))
print(hex_to_string("c5cb2e7f58400000"))
