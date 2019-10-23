import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_file = 'D://SalesData.xlsx'

def automate_report(excel_file):
    df = pd.read_excel(excel_file)
    df_unreceived = df[(df['Delivered']=='No') & ((df['Product'] == 'Iphone 7') | (df['Product'] == 'Iphone 8'))]
    df_unreceived.to_excel('unreceived_iphones_iphone7-8.xlsx')

    df_commission = df.groupby(['Employee For Commission']).sum()['Commission']
    df_commission.to_excel('Commission.xlsx')

    df_total_sales = df.groupby(['Product']).sum()['Value']
    df_total_sales.plot(kind='bar')
    plt.title('Value of Iphone Sales')
    plt.xlabel('Iphone')
    plt.ylabel('Total Value of Sales')
    plt.show()

    return True

automate_report(excel_file)