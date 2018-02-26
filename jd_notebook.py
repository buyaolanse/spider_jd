import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from pylab import *  

mpl.rcParams['font.sans-serif'] = ['SimHei'] 
mpl.rcParams['axes.unicode_minus'] = False
product_list = pd.read_csv(open(r'data_for_ana\京东商品信息爬虫.csv'))

grade_split = pd.DataFrame((x.split('￥') for x in product_list.price),index=product_list.index,columns=['no_use','price'])#将price列进行分列

product_list=pd.merge(product_list,grade_split,right_index=True, left_index=True) #将分列后的数据merge回原dataframe

product_list.price_y = pd.to_numeric(product_list.price_y, errors='coerce')   #str to int


#按照价格分布
hour = product_list.groupby('price_y').size()
#plt.xlim(0,25)
plt.plot(hour,linestyle='solid',color='royalblue',marker='8')    
