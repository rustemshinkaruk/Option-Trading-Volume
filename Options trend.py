import pandas as pd
import datetime

import matplotlib.pyplot as plt


data=pd.read_csv('daily volume.csv')
data['call']= data.iloc[:,1].str.replace(',', '')
data['put']= data.iloc[:,2].str.replace(',', '')

data.date=data.date.map(lambda x: datetime.datetime.strptime(x,'%m/%d/%Y'))
data['call']=(data['call'].astype(str)).astype(float)
data['put']=(data['put'].astype(str)).astype(float)

data=data.sort_values(by='date')
data['c/p ratio']=data['call']/data['put']
data['total']=data['call']+data['put']
data['dif']=1-data['c/p ratio']
data.set_index('date',inplace=True)



ax = plt.subplot(111)
(data.call/1e7).plot(ax=ax,color='blue')
(data.put/1e7).plot(ax=ax,color='green')
ax.bar(data.index,-data['dif'], width=1.2,edgecolor='black',color="silver")
ax.xaxis_date()
ax.legend(loc=2) 
ax.set_title("Trading Volume of Calls vs Puts")
ax.set_ylabel("volume x 10 millions")

ax.annotate("4",xy=('2020-03-17 00:00:00',1.55587),xytext=('2020-03-30 00:00:00',2),arrowprops=dict(facecolor='black',width=1),
            fontsize=14)
ax.annotate("3",xy=('2020-03-10 00:00:00',1.61299),xytext=('2020-03-17 00:00:00',2.5),arrowprops=dict(facecolor='black',width=1),
            fontsize=14)
ax.annotate("2",xy=('2020-02-25 00:00:00',2.17452),xytext=('2020-03-10 00:00:00',2.7),arrowprops=dict(facecolor='black',width=1),
            fontsize=14)

ax.annotate("1",xy=('2020-02-13 00:00:00',1.30805),xytext=('2020-02-15 00:00:00',1.9),arrowprops=dict(facecolor='black',width=1),
            fontsize=14)





