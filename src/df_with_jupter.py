import numpy as np
import pandas as pd

def automate_report(employee_number):

    df_first_shift = pd.read_excel("D://PlantData1-2.xlsx", sheet_name='First')
    df_second_shift = pd.read_excel("D://PlantData1-2.xlsx", sheet_name='Second')
    df_third_shift = pd.read_excel("D://PlantData3.xlsx")

    frames = [df_first_shift, df_second_shift, df_third_shift]
    total_information_df = pd.concat(frames, axis=0)

    total_information_df["Time Per Unit"] = total_information_df["Amount Produced"] / total_information_df["Working Time (Minutes)"]
    employee_df = total_information_df[total_information_df['Worker'] == employee_number]
    employee_df.to_excel(str(employee_number) + '-Report.xlsx')


