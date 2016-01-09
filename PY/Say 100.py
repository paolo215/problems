#pvprograms.weebly.com
#Say 100

import http.client

data = "token: Q37PK3OVsjXJGSEWjQ8ANjc5\n"

conn = http.client.HTTPConnection("codeabbey.sourceforge.net")
conn.request("POST", "/say-100.php", data)

response = conn.getresponse()
#print(str(response.status) + " " + response.reason)
test = response.read()
print(test)
test = str(test)
test = test.split(' ')
a = ''
i = 0
while True:
    if test[1][i].isdigit():
        a += test[1][i]
    else:
        break
    i += 1
answer = 100 - int(a)
answer = "answer: " + str(answer) + "\r\n"
conn.request("POST", "/say-100.php", data + answer)
test = conn.getresponse()
print(test.read())
