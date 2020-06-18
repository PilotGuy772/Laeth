import time
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
    
#6H*0)m<v)W-P87&)8T3-{N<&,R528.2-D1B|R#7(h2B.K'2%a2,a8)zUB$X+4G<8"H<*)[JBaa"3(h2B.K'2%a2,a*%4\<--aB1R00|o
    #233 34 91 3 181
      
    curCharInt -= code[i]
    curCharInt -= 32
    curCharInt %= 94
    curCharInt += 32
    
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
    
    #time.sleep(0.01)
    curCharInt = ord(character) 
    
    curCharInt += code[i]
    curCharInt -= 32
    curCharInt %= 94
    curCharInt += 32
    
    curChar = chr(curCharInt)
    
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
    
