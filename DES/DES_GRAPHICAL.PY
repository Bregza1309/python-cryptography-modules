from des import DES_ENCRYPTION
from des_decryption import DES_DECRYPTION
from tkinter import *
from tkinter import messagebox as msgbox

# INITIALISE WINDOW

root = Tk()
root.configure(bg='white smoke')
root.geometry('450x400')
root.title('DATA_ENCRYPTION_STANDARD')

# add labels
plaintext = Label(root,text= 'PLAINTEXT',bg= 'blue',font='aerial 10')
plaintext.place(x = 30 , y=100)
key = Label(root,text= 'KEY',bg= 'blue',font='aerial 10')
key.place(x = 30 , y=150)
title = Label(root,text='DES_ENCRYPTION',bg='orange',font='aerial 15 bold')
title.place(x =100,y = 40)
c_label = Label(root,text='CIPHER_HEX_VALUE :',font='aerial 10')
c_label.place(x =30,y = 300)
# add entry_fields

plain_txt = Entry(root,width='20')
plain_txt.place(x =250,y =100)

key = Entry(root,width='20')
key.place(x =250,y =150)
cypher_txt = Entry(root,width='20')
cypher_txt.place(x = 250 , y = 300)


# encrypt function

def encrypt():
    plaintext = plain_txt.get()
    key_txt = key.get()
    if plaintext != '':
        if key_txt !='':
            cipher_txt = DES_ENCRYPTION(plaintext,key_txt).encrypt()
            cypher_txt.insert(10,cipher_txt)
        else:
            msgbox.showerror('DES_ENCRYPTION_ERROR','ENTER 8 ASCII CHARACTERS_KEY OR LESS TO ENCRYPT')
    else:
        msgbox.showerror('DES_ENCRYPTION_ERROR','ENTER 8 ASCII CHARACTERS_PLAINTEXT OR LESS TO ENCRYPT')
    
    
def decrypt():
    try:

        cipher_txt = cypher_txt.get()
        key_txt = key.get()
        plain_text = DES_DECRYPTION(cipher_txt,key_txt).decrypt()
        plain_txt.insert(10,plain_text)
    except IndexError:
        msgbox.showerror('DES_DECRYPTION_ERROR','ENTER 16 HEX STRING TO DECRYPT')
def clear():
    cypher_txt.delete(0,'end')
    plain_txt.delete(0,'end')
    key.delete(0,'end')


def exit():
    confirm_exit = msgbox.askokcancel('CONFIRMATION_EXIT','ARE YOU SURE YOU WANT EXIT')
    if confirm_exit :
        root.destroy()
    
    
Button(root ,command=encrypt, font='aerial 10',text='ENCRYPT' ,bg='red',width=10).place(x = 30,y= 250)
Button(root ,command=decrypt, font='aerial 10',text='DECRYPT' ,bg='green',width=10).place(x = 250,y= 250)
Button(root ,command=clear, font='aerial 10',text='CLEAR' ,bg='grey',width=10).place(x = 300,y= 350)
Button(root,command=exit, font='aerial 10',text='EXIT' ,bg='grey',width=10).place(x = 10,y= 350)
    

root.mainloop()

