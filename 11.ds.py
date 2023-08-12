import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\giris_pu2cvr5\\Downloads\\temp.csv")
df.plot(kind='line',x='month',y='temp',title='temperature ta each month',color='r')
plt.show()

d=pd.read_csv("C:\\Users\\giris_pu2cvr5\\Downloads\\rain.csv")
d.plot(kind='scatter',x='month',y='rain',title='rainfall at each month',color='r')
plt.show()
