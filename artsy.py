import requests

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsImV4cCI6MTU0ODQzMjIwMCwiaWF0IjoxNTQ3ODI3NDAwLCJhdWQiO' \
        'iI1YzQxZjhjN2FhNWNlMzAwMmNkMzFhODYiLCJpc3MiOiJHcmF2aXR5IiwianRpIjoiNWM0MWY4YzhkYjIxNGE0MjAzYTQwMzE5In0.9J0J' \
        'qU78_Lb17jQdeILZTIoTX1QrTWbH1zOt1ZgsWow'

artists = {}
with open('input.txt', 'r') as inp:
    for line in inp:
        artist_id = line.strip()
        url = f'https://api.artsy.net/api/artists/{artist_id}'
        headers = {'X-Xapp-Token': token}
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        print(res.status_code)
        print(res.headers['Content-Type'])
        art = res.json()
        if art['birthday'] not in artists:
            artists[art['birthday']] = [art['sortable_name']]
        else:
            artists[art['birthday']].append(art['sortable_name'])
print(artists)
years = sorted(list(artists.keys()))
for year in years:
    print(*sorted(artists.get(year)), sep='\n')