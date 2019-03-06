# ontology_test
# Created by JKChang
# 2019-03-05, 21:46
# Tag:
# Description: get ontology response one by one

import requests

with open('../resources/ontology test URLs dev.txt') as fp:
    lines = fp.readlines()
    for line in lines:
        if line.startswith('http'):
            print(line)
            try:
                r = requests.head(line)
                if r.status_code != 200:
                    print(r.status_code)
                # prints the int of the status code. Find more at httpstatusrappers.com :)
            except requests.ConnectionError:
                print("failed to connect")
