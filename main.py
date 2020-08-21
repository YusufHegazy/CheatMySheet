import requests
from bs4 import BeautifulSoup
s = requests.Session()


question_link = 'https://www.chegg.com/homework-help/questions-and-answers/find-area-shaded-region-1-q4816320'
headers = {
    'authority': 'auth.chegg.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.59',
    'content-type': 'application/json;charset=UTF-8',
    'accept': '*/*',
    'origin': 'https://www.chegg.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.chegg.com/auth?action=login&redirect=https%3A%2F%2Fwww.chegg.com%2F',
    'accept-language': 'en-US,en;q=0.9',
}

data = '{"clientId":"CHGG","email":"xxxx@gmail.com","password":"xxxx"}'

login_req = s.post('https://auth.chegg.com/_ajax/auth/v1/login', headers=headers, data=data)

print(login_req.text)

q_req = requests.get(question_link, headers=headers)

q_req_source = q_req.text



soup = BeautifulSoup(q_req_source, "lxml")

divs = soup.find("main", {"class":"responsive-qna"}, recursive=True)
#print(divs)
with open("output.html", "w") as file:
     file.write(str(divs))

