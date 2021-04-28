import pandas as pd
import requests


def requestUniprot(uniprot_id, keyword, length):
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
keyword = 'Apoptosis'
length = '[* TO 600]'
matched = []
unmatched = []

df_res = pd.DataFrame(columns=df.columns)

for _, row in df.iterrows():
    uniprot_id = row['protein_uniprot_id']
    if row['protein_uniprot_id'] in matched:
        df_res.loc[len(df_res)] = row
        print('directly added ' + uniprot_id)
        continue
    elif row['protein_uniprot_id'] in unmatched:
        print('directly skipped ' + uniprot_id)
        continue

    uniport_search = requestUniprot(uniprot_id, keyword, length)

    if uniport_search:
        print('matched ' + uniprot_id)
        df_res.loc[len(df_res)] = row
        matched.append(uniprot_id)
    else:
        print('unmatched ' + uniprot_id)
        unmatched.append(uniprot_id)

df_res.to_csv('results2.csv', index=False)

# +AND+keyword:Apoptosis+AND+length:[600 TO *]