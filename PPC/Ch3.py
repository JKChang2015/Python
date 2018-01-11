# Ch3
# Created by JKChang
# 07/01/2018, 12:26
# Tag:
# Description: List

l = ['Munich', 'Casablanca', 'Altiplano', 'Tokyo', 'Seattle']
print('original list: ' + '  '.join(l))

# ------------sorted---------------------------------------
sort_l = sorted(l)
print()
print('original list:\t\t' + '  '.join(l))
print('sorted list:\t\t' + '  '.join(sort_l))

# ------------sorted(reverse =True)------------------------
r_sort_l = sorted(l, reverse=True)
print()
print('original list:\t\t' + '  '.join(l))
print('r_sorted list:\t\t' + '  '.join(r_sort_l))

# ------------list.sort()----------------------------------
l.sort()
print()
print('sorted list:\t\t' + '  '.join(l))

# ------------list.sort(reverse=True)----------------------
l.sort(reverse=True)
print()
print('sorted list:\t\t' + '  '.join(l))

print('\nlength of the list is', len(l))
