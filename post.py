
import requests
import string
import random
import signal
import sys
from string import digits
import time

total = 0 

def signal_handler(sig, frame):

  
  print('\ntotal sent: ' + str(total))
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

url = 'https://webpage87678.000webhostapp.com/' #URL DEL SITIO

uname = '' #USERNAME INPUT  Y TAL
pword = '' #LO MISMO PASSWORD
email = '' #TAL


fnames = open('fnames.txt', 'r').read().split() #primeros nombres NO RELLENAR
lnames = open('lnames.txt', 'r').read().split() #ultimos nombres NO RELLENAR
email_addrs = open('addrs.txt', 'r').read().split() #dominios NO RELLENAR


while(1==1):


 
  uname = random.choice(fnames) + "." + random.choice(lnames) + str(random.randint(1,9))
  

  pword = ''.join((random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(random.randint(7,12))))


  email = uname + '@' + random.choice(email_addrs)

  if(random.randint(0,1) == 0):
   
    uname = uname.replace('.','') 
    uname = uname.translate(None, digits) 
    uname = uname + ''.join(str(random.randint(0, 9)) for _ in range(random.randint(1,5))) 


  #
  #los datos que quieres joder
  dataForm = {
    'wb_form_id': '95a5b61e',
    'message': 'tal y cual', 
    'wb_input_0': email,
    'wb_input_1': uname,
    'wb_input_2': pword
  }

  print('email: ' + email + '\nuname: ' + uname + '\npword: ' + pword)


  try:
    r = requests.post(url, allow_redirects=False, data=dataForm)
    if(r.status_code == 302):
      #yay it went through
      total = total + 1
      print('POST ' + str(total) + ": " + str(r.status_code) + 'guay')
    else:
      print(str(r.status_code) + 'fallito')
    print('')
  except:
    print('\nCAGASTE\n')
    time.sleep(1) #perate 1 seg

