import json
import glob

def generate_indexes():
    coins = []
    
    for filename in glob.glob('./coins/*/*.json'):
        with open(filename) as fcoin:
            coin = json.loads(fcoin.read())

            if 'id' in coin:
                id = coin['id']
                name = coin['name']
                symbol = coin['symbol']
                url = coin.get('url', '')
                github_org = coin.get('github_org', None)
                
                coins.append((id, name, symbol, url, github_org))

    with open('./INDEX.md', 'w') as f:
        idx = 0
        for c in coins:
            idx += 1
            id, name, symbol, url, _ = c
            f.write(f'[{idx}. {symbol.upper()}](./coins/{id[0]}/{id}.json), {url}<br/>')

    with open('./github_orgs.txt', 'w') as f:
        visited = {}
        for c in coins:
            github_org = c[-1]

            if github_org and github_org not in visited:
                visited[github_org] = True
                f.write(f'{github_org}\n')

if __name__ == '__main__':
    generate_indexes()