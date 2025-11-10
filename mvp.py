import pandas as pd
data = { 
    'name':['张三','李四','王五','小明'],
    'sex':['female','female','male', 'male'],
    'year':[2001,2001,2003,2002],
    'city':['北京','上海','广州','北京']
}
df = pd.DataFrame(data)
print(df)
df3 = pd.DataFrame(data,
                   columns = ['name', 'sex', 'year', 'city'],
                   index = ['a', 'b', 'c', 'd']) 
print(df3)
df3.index = df3.index.insert(1,'w')