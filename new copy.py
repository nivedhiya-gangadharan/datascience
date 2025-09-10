# import numpy as np
# a = np.array([1,2,3])
# print(a)
# print(np.zeros((2,3)))
# print(np.ones((2,2)))
# a=np.arange(0,10,2)
# print(a)
# a=np.arrange(6)
# print("original:",a)
# b=a.reshape((2,3))
# print("reshaped:\n,b")
# arr=np.array([1,2,3,4])
# print(np.mean(arr))
# print(np.median(arr))
# print(np.std(arr))
# a=np.random.rand()
# print(a)
# b=np.random.rand(5)
# print(b)
# c=np.random.rand(2,3)
# print(c)
# x=np.random.randint(1,10)
# print(x)
# z=np.random.randint(10,21,size=(3,3))
# print(z)
#otp generation
# z=np.random.randint(10000,999999)
# print(z)
import pandas as pd
# s=pd.Series([10,20,30,40])
# print(s)
# data={'name':['alice','bob'],'age':[25,30]}
# df=pd.DataFrame(data)
# print(df)
# data={
#     'name':['alice','bob','charlie','david','eve','frank'],
#     'age':[25,30,35,None,25,23],
#     'score':[85,90,78,92,88,75]
# }
# df=pd.DataFrame(data)
# print(df.head())
# print(df.head(3))
# print(df.tail())
# print(df.tail(2))
# # df.info()
# print(df.describe())
# print(df.columns)
# print(df.shape)
# data={
#     'name':['alice','bob','charlie','david','eve','frank'],
#     'age':[25,30,35,None,25,23],
#     'score':[85,90,78,92,88,75]
# }
# df=pd.DataFrame(data,index=['a','b','c','d','e','f'])
# print(df.loc['a'])
# print(df.loc['b','name'])
# print(df.iloc[0])
data={
    'name':['alice','bob','charlie','david','eve','frank'],
    'age':[25,30,35,None,25,23],
    'score':[85,90,78,92,88,75]
}
df=pd.DataFrame(data)
print(df.isnull())
df.dropna()
df.fillna(0)
df['age'].fillna(df['age'].mean(),inplace=True)
print(df)+