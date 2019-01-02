# グラフ化に必要なものの準備
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.style.use('ggplot')
font = {'family': 'meiryo'}
matplotlib.rc('font', **font)

df = pd.read_csv('ticker.csv', sep=',')

print(df['timestamp'])
print(df['ltp'])

# type(df['timestamp'])

df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)

# x = df['timestamp']

y = df['ltp']

df.plot(y='ltp')
plt.show()

# print(df)


#df.plot(x, y)
# df.plot().line()
#plt.gcf().autofmt_xdate()
#plt.show()
