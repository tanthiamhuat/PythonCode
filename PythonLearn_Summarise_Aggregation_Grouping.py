## load in CSV files
import pandas as pd
import dateutil
data = pd.read_csv('https://shanelynnwebsite-mid9n9g1q9y8tt.netdna-ssl.com/wp-content/uploads/2015/06/phone_data.csv',delimiter=',')
data.dtypes
data['date']=data['date'].apply(dateutil.parser.parse,dayfirst=True)

data['item'].count()
data['duration'].max()
data['month'].value_counts()
data['network'].nunique()

data.groupby(['month']).groups.keys()
len(data.groupby(['month']).groups['2014-11'])
