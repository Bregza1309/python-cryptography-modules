from tkinter import font
from tkinter.font import Font
from AES_ENCRYPTION import AES128_ENCRYPTION
from tkinter import messagebox as msgbox
from AES128_DECRYPTION import AES128_DECRYPTION
from tkinter import *

# root _window
root = Tk()

# configure root settings
root.configure(bg= 'Gold')
root.geometry('600x400')
root.title('ADVANCED_ENCRYPTION_STANDARD')

# ADD LABELS
Label(root,text='ADVANCED_ENCRYPTION_STANDARD' , font = 'AERIAL  15 ', bg = 'White smoke').place(x =100 , y = 50)
Label(root,text= 'PLAINTEXT_ASCII_TEXT' , font = 'aerial 10',bg= 'white smoke').place(x = 20 , y = 100)
Label (root, text= 'KEY_ASCII_TEXT',font= 'aerial 10 ' , bg= 'white smoke').place(x= 20 ,y = 170)
Label(root , text = 'CYPHERTEXT_HEX' , font = 'aerial 10' , bg= 'white smoke').place(x =20 ,y = 240)

# ADD ENTRY BOXES
plaintext = Entry(root,bg='gold',font= 'aerial 10',width= 40)
plaintext.place(x = 290 , y = 100)

key = Entry(root,font='aerial 10 ',bg= 'gold' , width= 40)
key.place(x = 290 , y = 170)

cyphertext = Entry(root,font='aerial 10',width=40,bg='gold')
cyphertext.place(x = 290, y = 240)
# encrypt function 
def encrypt():
    aes_plaintext = plaintext.get()
    aes_key = key.get()
    if aes_plaintext != '':
        if aes_key != '':
            cypher = AES128_ENCRYPTION(aes_plaintext,aes_key).encrypt()
            cyphertext.insert(10,cypher)
        else:
            msgbox.showerror('AES_ERROR','ENTER KEY 16 ASCII CHARACTERS')
    else:
        msgbox.showerror('AES_ERROR','ENTER PLAIN_TEXT 16 ASCII CHARACTERS')
# decrypt function 
def decrypt():
    aes_cyphertext  = cyphertext.get()
    aes_key = key.get()
    if aes_cyphertext != '':
        if aes_key != '':
            plain_text = AES128_DECRYPTION(aes_cyphertext , aes_key).decrypt()
            plaintext.insert(10,plain_text)
        else:
            msgbox.showerror('AES_ERROR' , 'ENTER KEY 16 ASCII CHARACTERS') 
    else:
        msgbox.showerror('AES_ERROR','ENTER CYPHER_TEXT 32 HEX CHARACTERS')
# reset function
def reset():
    plaintext.delete(0,'end')
    cyphertext.delete(0 , 'end')
    key.delete(0,'end')

# exit window 
def exit():
    root.destroy()

# add_button (encrypt and decrypt)
Button(root,command= encrypt , text='ENCRYPT' ,width=15 ,bg='green').place(x = 100 , y = 300)
Button(root,command= decrypt , text= 'DECRYPT' ,width= 15 , bg= 'red').place(x = 350 , y = 300)
Button(root ,command= reset , text='RESET' , font = 'aerial 10' , bg= 'grey' , width= 10).place(x = 10 , y =340)
Button(root ,command= exit, text= 'EXIT' , bg= 'grey' , font= 'aerial 10' , width= 10).place( x = 450 , y =340)
root.mainloop()