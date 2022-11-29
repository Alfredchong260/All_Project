import pandas
import time
import numpy

# timestamp
# is a way of expression of time
# second millisecond
# used to calculate time in a more accurate way
# print(time.time())

# data = pandas.read_csv('douban_info.csv', encoding='gbk')
# print(data)
# data['citys'] = data['citys'].apply(lambda x:eval(x)[0] if eval(x) else numpy.NaN)
# # apply() used to apply for loop to data
# print(data.columns)
# # columns used to check all the titles in the data

# print(data['times'])
# data['times'] = data['times'].apply(lambda x:x.split(' ')[1])
# print(data)

# print(data['times'])
# data['times'] = pandas.to_datetime(data['times'])


# # usage of eval()
# a = '{"abc": 123}'
# print(a)
# print(eval(a))
# print(type(a))
# print(type(eval(a)))
# # in the DataFrame has not list data type but onject
# # object == string

# pretreatment of pandas
data = pandas.read_csv('meal_order_info.csv', encoding='gbk')
df1 = data.iloc[:10, :3]
df2 = data.iloc[:10, 4: 7]
print(df1)
print(df2)
df3 = pandas.concat([df1, df2], axis=1)
print(df3)
# inner, outer
# left = pandas.DataFrame({'info_id': ['K0', 'K1', 'K2', 'K3']

#     })
