import requests

with open(r'dataset_3378_3.txt', 'r') as fh:
    for line in fh:
        link = line.strip()

r = requests.get(link)
res = r.text

while res[0:2] != "We":
    link = r'https://stepic.org/media/attachments/course67/3.6.3/' + res
    r = requests.get(link)
    res = r.text

print(res)
