from sha_functions import *

class SHA512:
    def __init__(self,plaintext):
        self.padding_value = sha_padding(plaintext)
        
        self.registers = {'a':'6A09E667F3BCC908',
                          'b':'BB67AE8584CAA73B' ,
                          'c' :'3C6EF372FE94F82B' ,
                          'd' :'A54FF53A5F1D36F1',
                          'e' :'510E527FADE682D1',
                          'f' :'9B05688C2B3E6C1F',
                          'g' :'1F83D9ABFB41BD6B',
                          'h' :'5BE0CD19137E2179'}
        
        self.sha_constants = [['428A2F98D728AE22','3956C25BF348B538','D807AA98A3030242','72BE5D74F27B896F','E49B69C19EF14AD2','2DE92C6F592B0275','983E5152EE66DFAB','C6E00BF33DA88FC2','27B70A8546D22FFC','650A73548BAF63DE','A2BFE8A14CF10364','D192E819D6EF5218','19A4C116B8D2D0C8','391C0CB3C5C95A63','748F82EE5DEFB2FC','90BEFFFA23631E28','CA273ECEEA26619C','06F067AA72176FBA','28DB77F523047D84','4CC5D4BECB3E42B6'],
                              ['7137449123EF65CD','59F111F1B605D019','12835B0145706FBE','80DEB1FE3B1696B1','EFBE4786384F25E3','4A7484AA6EA6E483','A831C66D2DB43210','D5A79147930AA725','2E1B21385C26C926','766A0ABB3C77B2A8','A81A664BBC423001','D69906245565A910','1E376C085141AB53','4ED8AA4AE3418ACB','78A5636F43172F60','A4506CEBDE82BDE9','D186B8C721C0C207','0A637DC5A2C898A6','32CAAB7B40C72493','597F299CFC657E2A'],
                              ['B5C0FBCFEC4D3B2F','923F82A4AF194F9B','243185BE4EE4B28C','9BDC06A725C71235','0FC19DC68B8CD5B5','5CB0A9DCBD41FBD4','B00327C898FB213F','06CA6351E003826F','4D2C6DFC5AC42AED','81C2C92E47EDAEE6','C24B8B70D0F89791','F40E35855771202A','2748774CDF8EEB99','5B9CCA4F7763E373','84C87814A1F0AB72','BEF9A3F7B2C67915','EADA7DD6CDE0EB1E','113F9804BEF90DAE','3C9EBE0A15C9BEBC','5FCB6FAB3AD6FAEC'],
                              ['E9B5DBA58189DBBC','AB1C5ED5DA6D8118','550C7DC3D5FFB4E2','C19BF174CF692694','240CA1CC77AC9C65','76F988DA831153B5','BF597FC7BEEF0EE4','142929670A0E6E70','53380D139D95B3DF','92722C851482353B','C76C51A30654BE30','106AA07032BBD1B8','34B0BCB5E19B48A8','682E6FF3D6B2B8A3','8CC702081A6439EC','C67178F2E372532B','F57D4F7FEE6ED178','1B710B35131C471B','431D67C49C100D4C','6C44198C4A475817']]
        i = 0 
        self.fin_consts = []
        
        while i < len(self.sha_constants[0]):
            b = 0 
            while b < len(self.sha_constants):
                self.fin_consts.append(self.sha_constants[b][i])
                b+=1
            i +=1
            
             
        
            
      
            
                                 
    def hash(self):
        """generate hash value"""
        # partition plaintext blocks into 1024
        l = 0
        plaintext_blocks = []
        
        while l < len(self.padding_value):
            plaintext_blocks.append(self.padding_value[l:l+256])
            l += 256
        
        #set initial values of a,b,c,d,e,f,g,h
        a = self.registers['a']
        b = self.registers['b']
        c = self.registers['c']
        d = self.registers['d']
        e = self.registers['e']
        f = self.registers['f']
        g = self.registers['g']
        h = self.registers['h']
        for block in plaintext_blocks:
            self.final_hash = []
            initial_register = [a,b,c,d,e,f,g,h]
            # loop through the 80 rounds
            
            derived_words = sha_word_processing(block)  
            for m in range(80):
                
                t = addition_mod(h,ch(e,f,g))
                t = addition_mod(t,sum512_1(e))
                t = addition_mod(t,derived_words[m])
                
                t_1 = addition_mod(t,self.fin_consts[m])
                
                
                t_2 = addition_mod(sum512_0(a),maj(a,b,c))
                
                h = g 
                g = f
                f = e 
                
                    
                e = addition_mod(d,t_1)
                
                d = c
                c = b
                b = a
                
                a = addition_mod(t_1,t_2)
            
            fin_values = [a,b,c,d,e,f,g,h]
            
            for k in range(len(fin_values)):
                temp = addition_mod(fin_values[k],initial_register[k])
                self.final_hash.append(temp)
            a = self.final_hash[0]
            b = self.final_hash[1]
            c = self.final_hash[2]
            d = self.final_hash[3]   
            e = self.final_hash[4]
            f = self.final_hash[5]
            g = self.final_hash[6]
            h = self.final_hash[7]
        hash_value = a+b+c+d+e+f+g+h
        return hash_value 
            
         
    



