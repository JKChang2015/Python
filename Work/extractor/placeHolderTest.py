# placeHolderTest
# Created by JKChang
# 2019-07-26, 11:46
# Tag:
# Description: using ontology ws to test placeholder

import pandas as pd
import time
import json

import requests

df = pd.read_csv('placeHolder.tsv',sep = '\t')
terms = df['name'].tolist()



for term in terms:
    print('=' * 30)
    print(term)
    start = time.time()
    term = term.replace(" ", "%20")
    url = "https://wwwdev.ebi.ac.uk/metabolights/ws/ebi-internal/ontology?term=" + term + "&queryFields=%7BMTBLS%2CMTBLS_Zooma%2CZooma%2COLS%2C%20Bioportal%7D"
    try:
        data = requests.get(url)
        print(json.dumps(data.json(), indent=4, sort_keys=True))
        r = requests.head(url)
        if r.status_code != 200:
            print(r.status_code)
        # prints the int of the status code. Find more at httpstatusrappers.com :)
    except requests.ConnectionError:
        print("failed to connect")

    print(time.time() - start)


print()

