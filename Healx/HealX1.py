import pandas as pd
import requests


def requestUniprot(uniprot_id, keyword, length):
    print(uniprot_id)
    source = 'query=accession:{id}+AND+keyword:{keyword}+AND+length:{length}&format=tab&columns=id'.format(
        id=uniprot_id, keyword=keyword, length=length)
    ws_url = 'https://www.uniprot.org/uniprot/?' + source
    try:
        resp = requests.get(ws_url)
        if int(resp.headers['content-length']) > 0:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


df = pd.read_csv('healx-test-rare-disease-genes.csv')
df['res'] = df['protein_uniprot_id'].apply(lambda x: requestUniprot(x, 'Apoptosis', '[* TO 600]'))
df = df[df['res'] == True].drop(['res'], axis=1)
df.to_csv('results.csv', index=False)
