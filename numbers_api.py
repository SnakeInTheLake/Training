import requests

with open('input.txt', 'r') as inp:
    for line in inp:
        number = line.strip()
        # print(number)

        url = f'http://numbersapi.com/{number}/math'
        print(url)
        params = {
            'json': 'true'
        }
        res = requests.get(url, params=params)
        # print(res.status_code)
        # print(res.headers['Content-Type'])
        # print(res.json())
        data = res.json()
        if data['found']:
            print('Interesting')
        else:
            print('Boring')