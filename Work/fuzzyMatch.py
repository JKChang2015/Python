# fuzzyMatch
# Created by JKChang
# 2019-07-09, 09:27
# Tag:
# Description: python based String fuzzy match

from fuzzywuzzy import  fuzz

str1 = 'Apple Inc'
str2 = 'apple inc.'
str3 = 'apple_inc'
str4 = 'Apple-INC'
str5 = 'Inc of Apple'

ratio = fuzz.partial_ratio(str1.lower(),str2.lower())
print(ratio)
ratio = fuzz.partial_ratio(str1.lower(),str3.lower())
print(ratio)
ratio = fuzz.partial_ratio(str1.lower(),str4.lower())
print(ratio)

ratio = fuzz.partial_ratio(str1.lower(),str5.lower())
print(ratio)

# different order
Token_Sort_Ratio = fuzz.token_sort_ratio(str1,str5)
print(Token_Sort_Ratio)
Token_Set_Ratio = fuzz.token_set_ratio(str1,str5)
print(Token_Set_Ratio)

Str1 = "Apple Inc."
Str2 = "Apple Inc."
Result = Str1 == Str2
print(Result)


