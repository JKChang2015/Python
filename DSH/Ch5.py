# Ch5
# Created by JKChang
# 07/01/2018, 14:25
# Tag:
# Description: if statement

age = int(input('please input your age： '))
if age < 2:
    print('you are a baby')
elif age >= 2 and age < 4:
    print('you are a kid')
elif age >= 4 and age < 13:
    print('you are a child')
elif age >= 13 and age < 20:
    print('you are a young')
elif age >= 20 and age < 65:
    print('you are a adults')
else:
    print('you are a elder')

# ------------------ 5-10 -----------------------
print('\n')
cur_users = ['Paul', 'David', 'Ken', 'Claire', 'Gareth']
new_users = ['Tom', 'david', 'Ken']

print(cur_users)
print(new_users)

for user in new_users:
    duplicate = False
    for d_user in cur_users:
        if user.lower() == d_user.lower():
            print('sorry the', user, 'has been taken')
            duplicate = True
            break
    if (not duplicate):
        cur_users.append(user)

print(cur_users)

# ------------------ 5-11 -----------------------
print('\n')
nums = [str(x) for x in range(1, 10)]
res = []
for n in nums:
    if n == '1':
        res.append(n + 'st')
    elif n == '2':
        res.append(n + 'nd')
    elif n == '3':
        res.append(n + 'rd')
    else:
        res.append(n + 'th')

print(', '.join(res))
