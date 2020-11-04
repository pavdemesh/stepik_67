import requests

with open(r'dataset_3378_2.txt', 'r') as fh:
    for line in fh:
        link = line.strip()

req = requests.get(link)
res = req.text.splitlines()
print(len(res))

with open('output_req.txt', 'w') as fout:
    for element in res:
        fout.write(element + '\n')
