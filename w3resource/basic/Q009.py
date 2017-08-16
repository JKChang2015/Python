# -*- coding: UTF-8 -*-
# Q009
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: 
# Description: Write a Python program to display the examination schedule. (extract the date from exam_st_date). 
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

exam_st_date = (25, 12, 2014)
print('%d / %d / %d' % exam_st_date)

# print month-day-year
print('{} - {} - {}'.format(exam_st_date[1], exam_st_date[0], exam_st_date[2]))
