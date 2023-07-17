import requests
import uuid

insta = input("Instagram username -> ")
url = "https://ngl.link/api/submit"
ques = input("Question -> ")

while True:
    deviceid = uuid.uuid1
    payload = f'username={insta}&question={ques}&deviceId={deviceid}&gameSlug=&refferer='
    total = len(payload)

    headers = {
            'authority': 'ngl.link',
            'method': 'POST',
            'path': '/api/submit', 
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.7',
            'content-length': str(total),
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://ngl.link',
            'referer': f'https://ngl.link/{insta}',
            'sec-ch-ua': '"Brave";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'x-requested-with': 'XMLHttpRequest'
    }

    send = requests.post(url, headers=headers, data=payload)
    if send.status_code == 200:
        print("sent")
    else:
        print("error")
