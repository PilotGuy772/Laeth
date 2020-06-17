
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

'look at me. i`m a random string!'


def decrypt(c,m):

  global encMes, code
  print('Your message is:')

  print(m)
  print('LOADING........')
  i = 0
  for letter in m:
    code[i] = int(code[i])
    curCharInt = ord(letter)
    
      
    curCharInt -= code[i]
    print(curCharInt)

    curChar = chr(curCharInt) 
    print(curChar)
    encMes += curChar
    if i < 5:
      i +1
    else:
      i=1
  print('Your new message is:')
  print(encMes)
  #list parser and command prcessing function

def encrypt(c,m):
  global encMes, code
  print('Your message is:')
  
  print(m)
  print('LOADING...')
  i = 0
  for letter in m:
    code[i] = int(code[i]) 
    curCharInt = ord(letter) 
    
    curCharInt += code[i]
    
    
    curChar = chr(curCharInt)
    encMes += curChar
    if i < 5:
      i +1
    else:
      i=1
  print('Your new message is:')
  print(encMes)
  parse()



def parse():
  global code, message, encMes
  code = []
  message = ''
  encMes = ''
  print('Please enter your code...')
  code = input('INT[5]>>').split()
  print('Code is'+code[0]+code[1]+code[2]+code[3]+code[4])
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
     

    
