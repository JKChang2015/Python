#List
student = ['A', "B" , "C", 'D']
print(student [0]) #print the element of the List
print(student) #print the whole List
student[0] = "AA" # the value of the element can be change

#TUPLE
student2 = ('A', "B" , "C", 'D')
print(student [2]) #print the element of tuple
print(student) # print all
# student2[0] = "AA", error, because tuple doese not support assignment

print ("\n\n")

#SET
studentName1 = set('abcdeeffaade')
studentName2 = set("adnded")
x =  studentName1 & studentName2
print(x)
print(studentName1 | studentName2)
print(studentName1 - studentName2)
new = set(studentName1)
print(new)

print ("\n\n")

#DICTIONARY
st1 = {'name':"David", "Chinese": 123, "Math": 13}
st2 = {'name': "Chan", "Chinese": 21, "Math": 23}

print(st1['name'])
print(st1['Chinese'])
print(st1)
print(st2)

st1['music'] = 221
print(st1)