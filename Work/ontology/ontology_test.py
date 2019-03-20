# ontology_test
# Created by JKChang
# 2019-03-05, 21:46
# Tag:
# Description: get ontology response one by one

import time
import json

import requests

with open('../resources/ontology test URLs dev.txt') as fp:
    lines = fp.readlines()

    for line in lines:
        start = time.time()

        if line.startswith('http'):
            print('==' * 30)
            print(line)
            try:
                data = requests.get(line)
                print(json.dumps(data.json(), indent=4, sort_keys=True))
                r = requests.head(line)
                if r.status_code != 200:
                    print(r.status_code)
                # prints the int of the status code. Find more at httpstatusrappers.com :)
            except requests.ConnectionError:
                print("failed to connect")
        print(time.time() - start)
