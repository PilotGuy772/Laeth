import time
code = [0, 0, 0, 0, 0]
message = ''
encMes = ''
unencMes = ''
curCharInt = 0
curChar = ''
print('before we start, please type "readme" to see the readme.txt file.')
if input('>>').lower() == 'readme':
    print('''
    Please note that this program IS NOT COMPLETE! 
    ---
    Another thing of note: This program was designed to be used in ANOTHER PROGRAM. It still works fine, but this program is not designed to be at it's best with purely the command line. A link to the final project with the adapted version of this program can be found at the bottom of this page when it is complete.
    ===
    INSTRUCTIONS FOR USE:
    1. Enter five numbers from 0-26 (NOTE: must be in order from least to greatest due to a bug that will be patched soon), seperated by spaces. if you're decrypting a message, enter the SAME code as the encrypter. Press ENTER.
    
    2. Then, enter any message of any length. Special characters allowed, but this program doesn't like numbers (Patch for that is coming soon).If your decrypting a message, enter the message you received. Press ENTER.
    
    3. type encrypt if you are encrypting, type decrypt if you're decrypting. Press ENTER
    
    4. If you're encrypting the message, send the encrypted message, the code, and the mode to the recipient in any way you like. make sure they know how to use this software.
    
    5 If you are decrypting, you're all done!
    ><><
    
    ><><
    
    ''')
#123 234 82 5 124
#If you are reading this message, you have successfully followed the steps to use my program. Good job. To confirm, send this message to me via Discord: Happy angels are happy when they eat poisin bananas.
#ifmmp!xpsme/



def decrypt(c,m):

  global encMes, code, curCharInt
  print('Your message is:')

  print(m)
  print('LOADING........')
  i = 0
  code[0] = int(code[0])
  code[1] = int(code[1])
  code[2] = int(code[2])
  code[3] = int(code[3])
  code[4] = int(code[4])
  for character in m:
    
    curCharInt = ord(character)
    
      
    curCharInt -= code[i]
    curCharInt %= 94
    curCharInt = 176 - curCharInt
    print(curCharInt)
    curChar = chr(curCharInt) 
    print(curChar)
    
    encMes += curChar
    if i < 4:
      i +=1
    else:
      i=1
  print('Your new message is:')
  print(encMes)
  #list parser and command prcessing function

def encrypt(c,m):
  global encMes, code, curCharInt
  print('Your message is:')
  
  print(m)
  print('LOADING...')
  i = 0
  code[0] = int(code[0])
  code[1] = int(code[1])
  code[2] = int(code[2])
  code[3] = int(code[3])
  code[4] = int(code[4])
  for character in m:
    
    time.sleep(0.01)
    curCharInt = ord(character) 
    
    curCharInt += code[i]
    curCharInt %= 94
    curCharInt += 31
    print(curCharInt)
    curChar = chr(curCharInt)
    print(curChar)
    encMes += curChar
    if i < 4:
      i += 1
      
    else:
      i=1
      
  print('Your new message is:')
  print(encMes)
  parse()



def parse():
  global code, message, encMes, curCharInt
  code = []
  message = ''
  encMes = ''
  curCharInt = 0
  print('Please enter your code...')
  code = input('INT[5]>>').split()
  #print('Code is'+code[0]+code[1]+code[2]+code[3]+code[4])
  print('Please paste in your message...')
  message = input('STR"any">>')
  print('would you like to encrypt or decrypt?')
  myVar = input('STR"encrypt"OR"decrypt">>').lower()
  if myVar == 'encrypt':
    print("LOADING - PLEASE WAIT!")
    encrypt(code, message)
  else:
    print("LOADING - PLEASE WAIT!")
    decrypt(code, message)
  parse()
  

#encrypter function



parse()






'''
#Defining variables
code = [0, 0, 0, 0, 0]
message = ''
encMes = ''
unencMes = ''
curCharInt = 0
curChar = ''

#123 234 82 5 124
#If you are reading this message, you have successfully followed the steps to use my program. Good job. To confirm, send this message to me via Discord: Happy angels are happy when they eat poisin bananas.
#ifmmp!xpsme/



def decrypt(c,m):

  global encMes, code, curCharInt
  print('Your message is:')

  print(m)
  print('LOADING........')
  i = 0
  code[0] = int(code[0])
  code[1] = int(code[1])
  code[2] = int(code[2])
  code[3] = int(code[3])
  code[4] = int(code[4])
  for character in m:
    
    curCharInt = ord(character)
    
      
    curCharInt -= code[i]
  

    curChar = chr(curCharInt) 
    
    encMes += curChar
    if i < 4:
      i +=1
    else:
      i=1
  print('Your new message is:')
  print(encMes)
  #list parser and command prcessing function

def encrypt(c,m):
  global encMes, code, curCharInt
  print('Your message is:')
  
  print(m)
  print('LOADING...')
  i = 0
  code[0] = int(code[0])
  code[1] = int(code[1])
  code[2] = int(code[2])
  code[3] = int(code[3])
  code[4] = int(code[4])
  for character in m:
    print(i)
    
    curCharInt = ord(character) 
    print(curCharInt)
    curCharInt += code[i]
    print(curCharInt)
    
    curChar = chr(curCharInt)
    print(curChar)
    encMes += curChar
    if i < 4:
      i += 1
      
    else:
      i=1
      
  print('Your new message is:')
  print(encMes)
  parse()



def parse():
  global code, message, encMes, curCharInt
  code = []
  message = ''
  encMes = ''
  curCharInt = 0
  print('Please enter your code...')
  code = input('INT[5]>>').split()
  #print('Code is'+code[0]+code[1]+code[2]+code[3]+code[4])
  print('Please paste in your message...')
  message = input('STR"any">>')
  print('would you like to encrypt or decrypt?')
  myVar = input('STR"encrypt"OR"decrypt">>').lower()
  if myVar == 'encrypt':
    encrypt(code, message)
  else:
    decrypt(code, message)
  parse()
  

#encrypter function



parse()
     
'''
    
