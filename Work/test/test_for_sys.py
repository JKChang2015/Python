# test_for_sys
# Created by JKChang
# 15/04/2020, 22:17
# Tag:
# Description:

import argparse

def test_for_sys(year, name, body):
    print('the year is', year)
    print('the name is', name)
    print('the body is', body)

parser = argparse.ArgumentParser(description='update Metabolights untarget information')
parser.add_argument('--name', '-n', help='name, Non-essential parameter')
parser.add_argument('--year', '-y', help = 'year, default value', default = 2020)
parser.add_argument('--body', '-b', help='body, essential parameter', required=True)
args = parser.parse_args()

if __name__ == '__main__':
    try:
        test_for_sys(args.year, args.name, args.body)
    except Exception as e:
        print(e)