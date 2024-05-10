import requests
import uuid
import threading
import time

def read_proxies(filename):
    with open(filename, 'r') as file:
        proxies = file.read().splitlines()
    return proxies

def send_request(insta, ques, proxy):
    url = "https://ngl.link/api/submit"
    deviceid = str(uuid.uuid1())
    payload = {
        'username': insta,
        'question': ques,
        'deviceId': deviceid,
        'gameSlug': '',
        'refferer': ''
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'
    }

    hostname, port, username, password = proxy.split(':')

    proxies = {
        'https': f'http://{username}:{password}@{hostname}:{port}'
    }

    try:
        response = requests.post(url, headers=headers, data=payload, proxies=proxies)
        if response.status_code == 200:
            print("sent")
        else:
            print("error")
    except Exception as e:
        print("error:", e)

def main():
    insta = input("Instagram username -> ")
    ques = input("Question -> ")
    proxies = read_proxies('proxies.txt')
    num_threads = 50

    while True:
        threads = []
        for proxy in proxies:
            for _ in range(num_threads):
                thread = threading.Thread(target=send_request, args=(insta, ques, proxy))
                thread.start()
                threads.append(thread)
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    main()
