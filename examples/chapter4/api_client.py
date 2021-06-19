import requests

baseUrl = 'https://pokeapi.co'

def query(res_url):
    url = '{}'.format(res_url)

    with requests.get(url) as response:
        if response.status_code == 200:
            return response.json()
        return None

pikachu = query(baseUrl + '/api/v2/pokemon-species/pikachu')

desc_links = pikachu['flavor_text_entries']
desc_links = [x for x in desc_links if x['language']['name'] == 'en']

desc = desc_links[0]['flavor_text']

sprite_link = query(pikachu['varieties'][0]['pokemon']['url'])
sprite = sprite_link['sprites']['front_default']

print(pikachu['name'])
print(desc)
print(sprite)
