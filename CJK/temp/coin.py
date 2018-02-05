# coin
# Created by JKChang
# 05/02/2018, 14:57
# Tag:
# Description: 
#
def find_changes(n, coins):
    if n < 0:
        return []
    if n == 0:
         return [[]]
    all_changes = []

    for last_used_coin in coins:
        combos = find_changes(n - last_used_coin, coins)
        for combo in combos:
            combo.append(last_used_coin)
            all_changes.append(combo)

    return all_changes

all = find_changes(10, [1,2,5])
res = set([tuple(t) for t in [sorted(l) for l in all]])
print ('\n'.join(str(x) for x in res))

