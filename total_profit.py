import pandas as pd
import numpy as np
import os

csv_file = [f for f in os.listdir('.\\input') if f.endswith('.csv')]
df = pd.concat([pd.read_csv('input/'+csv) for csv in csv_file],ignore_index=True)
columns_needed = ['symbol','trade_date','trade_type','quantity','price','order_execution_time']
df = df[columns_needed]
df.sort_values(['order_execution_time'],inplace=True)
di = {}
profit = 0
li = []
for i in df.values:
    if i[0] not in di.keys():
        if 'buy' in i:
            di[i[0]] = {'quantity' : i[3],'avg_price' : i[4]}
            li.append(list(i))
    else:
        if 'buy' in i:
            di[i[0]]['avg_price'] = (di[i[0]]['quantity']*di[i[0]]['avg_price']+i[3]*i[4]) / (di[i[0]]['quantity'] + i[3])
            di[i[0]]['quantity'] += i[3]
            li.append(list(i))
        if 'sell' in i:
            di[i[0]]['quantity'] -= i[3]
            profit += (i[3]*i[4] - di[i[0]]['avg_price']*i[3])
            li.append(list(np.append(i,i[3]*i[4] - di[i[0]]['avg_price']*i[3])))
            if di[i[0]]['quantity'] == 0:
                di.pop(i[0])
columns = list(df.columns)
columns.append('profit')
li.append(['','','','','','Total Profit',profit])
df_final = pd.DataFrame(li,columns=columns)
df_final.fillna('NA',inplace=True)
df_final.to_csv('consolidated_report_trade.csv',index=False)
print(f"Current holdings \n {di}")
print(f'Total profit = {profit}')