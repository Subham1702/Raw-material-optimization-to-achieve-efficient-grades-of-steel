# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 19:09:18 2024

@author: mital
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pip install mysql-connector-python
import mysql.connector

# Database connection details
host = 'localhost'
user = 'root'
password = 'password'
database = 'Steel_db'

# Establishing the connection
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Creating a cursor object
cursor = conn.cursor()

# SQL query
query = "SELECT * FROM steel_prod"

# Executing the query
cursor.execute(query)

# Fetching all rows from the executed query
rows = cursor.fetchall()

# Getting column names
columns = cursor.column_names

# Converting to DataFrame
raw_data = pd.DataFrame(rows, columns=columns)

# Display the DataFrame
print(raw_data.head())

# Closing the cursor and connection
cursor.close()
conn.close()


raw_data = raw_data.astype({'steel_grade': 'object', 'auto_app': 'object'})

raw_data['phosphorus'] = raw_data['phosphorus'].str.replace('%', '').astype(int)
raw_data['melting_time_EAF'] = raw_data['melting_time_EAF'].str.replace('hours', '').astype(float)
raw_data['scrap_steel'] = raw_data['scrap_steel'].str.replace('%', '').astype(int)
raw_data['pig_iron'] = raw_data['pig_iron'].str.replace('%', '').astype(int)
raw_data['iron_ore'] = raw_data['iron_ore'].str.replace('%', '').astype(int)
raw_data['carbon'] = raw_data['carbon'].str.replace('%', '').astype(int)
raw_data['prod_vol'] = raw_data['prod_vol'].str.replace('tons', '').astype(int)
raw_data['Yield'] = raw_data['Yield'].str.replace('%', '').astype(int)
raw_data['OriginalCost_Ton'] = raw_data['OriginalCost_Ton'].str.replace('$', '').astype(int)
raw_data['new_scrap_steel'] = raw_data['new_scrap_steel'].str.replace('%', '').astype(float)
raw_data['new_pig_iron'] = raw_data['new_pig_iron'].str.replace('%', '').astype(int)
raw_data['new_iron_ore'] = raw_data['new_iron_ore'].str.replace('%', '').astype(int)
raw_data['BF_SCT'] = raw_data['BF_SCT'].str.replace('hours', '').astype(float)
raw_data['EAF_SCT'] = raw_data['EAF_SCT'].str.replace('hours', '').astype(float)
raw_data['LRF_SCT'] = raw_data['LRF_SCT'].str.replace('hours', '').astype(float)
raw_data['Total_CT'] = raw_data['Total_CT'].str.replace('hours', '').astype(float)


columns_to_process = ['BF_El', 'EAF_El', 'LRF_El', 'Total_El_Con', 'new_el_con', 'BF_El_new', 'EAF_El_new', 'LRF_El_new', 'Estimated_cost_per_ton']
for column in columns_to_process:
    raw_data[column] = raw_data[column].astype(int)




                    ### EDA ###
raw_data.dtypes                   
raw_data.isna().sum()


raw_data['scrap_steel'].mean()
raw_data['Yield'].mean()
raw_data['Estimated_cost_per_ton'].mean()
raw_data['auto_app'].mean()
raw_data['pig_iron'].mean()
raw_data['phosphorus'].mean()
raw_data['carbon'].mean()
raw_data['melting_time_EAF'].mean()
raw_data['OriginalCost_Ton'].mean()
raw_data['Estimated_cost_per_ton'].mean()
raw_data['Total_CT'].mean()


raw_data['scrap_steel'].median()
raw_data['Yield'].median()
raw_data['Estimated_cost_per_ton'].median()
raw_data['auto_app'].median()
raw_data['pig_iron'].median()
raw_data['phosphorus'].median()
raw_data['carbon'].median()
raw_data['melting_time_EAF'].median()
raw_data['OriginalCost_Ton'].median()
raw_data['Estimated_cost_per_ton'].median()
raw_data['Total_CT'].median()


raw_data['steel_grade'].mode()
raw_data['auto_app'].mode()
raw_data['scrap_steel'].mode()
raw_data['Yield'].mode()
raw_data['Estimated_cost_per_ton'].mode()
raw_data['auto_app'].mode()
raw_data['pig_iron'].mode()
raw_data['phosphorus'].mode()
raw_data['carbon'].mode()
raw_data['melting_time_EAF'].mode()
raw_data['OriginalCost_Ton'].mode()
raw_data['Estimated_cost_per_ton'].mode()
raw_data['Total_CT'].mode()


raw_data['scrap_steel'].std()
raw_data['Yield'].std()
raw_data['Estimated_cost_per_ton'].std()
raw_data['auto_app'].std()
raw_data['pig_iron'].std()
raw_data['phosphorus'].std()
raw_data['carbon'].std()
raw_data['melting_time_EAF'].std()
raw_data['OriginalCost_Ton'].std()
raw_data['Estimated_cost_per_ton'].std()
raw_data['Total_CT'].std()


raw_data['scrap_steel'].var()
raw_data['Yield'].var()
raw_data['Estimated_cost_per_ton'].var()
raw_data['auto_app'].var()
raw_data['pig_iron'].var()
raw_data['phosphorus'].var()
raw_data['carbon'].var()
raw_data['melting_time_EAF'].var()
raw_data['OriginalCost_Ton'].var()
raw_data['Estimated_cost_per_ton'].var()
raw_data['Total_CT'].var()


r1 = raw_data['scrap_steel'].max() - raw_data['scrap_steel'].min()
r2 = raw_data['pig_iron'].max() - raw_data['pig_iron'].min()
r3 = raw_data['iron_ore'].max() - raw_data['iron_ore'].min()
r4 = raw_data['Yield'].max() - raw_data['Yield'].min()
r5 = raw_data['BF_SCT'].max() - raw_data['BF_SCT'].min()
r6 = raw_data['LRF_SCT'].max() - raw_data['LRF_SCT'].min()
r7 = raw_data['Total_CT'].max() - raw_data['Total_CT'].min()
r8 = raw_data['melting_time_EAF'].max() - raw_data['melting_time_EAF'].min()
r9 = raw_data['OriginalCost_Ton'].max() - raw_data['OriginalCost_Ton'].min()
r10 = raw_data['Estmated_cost_per_ton'].max() - raw_data['Estimated_cost_per_ton'].min()


raw_data['scrap_steel'].skew()
raw_data['Yield'].skew()
raw_data['Estimated_cost_per_ton'].skew()
raw_data['auto_app'].skew()
raw_data['pig_iron'].skew()
raw_data['phosphorus'].skew()
raw_data['carbon'].skew()
raw_data['melting_time_EAF'].skew()
raw_data['OriginalCost_Ton'].skew()
raw_data['Estimated_cost_per_ton'].skew()
raw_data['Total_CT'].skew()


raw_data['scrap_steel'].kurt()
raw_data['Yield'].kurt()
raw_data['Estimated_cost_per_ton'].kurt()
raw_data['auto_app'].kurt()
raw_data['pig_iron'].kurt()
raw_data['phosphorus'].kurt()
raw_data['carbon'].kurt()
raw_data['melting_time_EAF'].kurt()
raw_data['OriginalCost_Ton'].kurt()
raw_data['Estimated_cost_per_ton'].kurt()
   
                         
                            ### Data Preprocessing ###
# Save to CSV
raw_data.to_csv("output_utf8.csv", index=False, encoding='utf-8')

from autoviz.AutoViz_Class import AutoViz_Class

# AutoViz
AV = AutoViz_Class()
df = pd.read_csv('output_utf8.csv', encoding='utf-8')

df_av = AV.AutoViz('', dfte=df)

# Pandas Profiling
pip install --upgrade pandas pandas-profiling

pip install pandas-profiling

import pandas as pd
from pandas_profiling import ProfileReport

# Read CSV with UTF-8 encoding
df = pd.read_csv('output_utf8.csv', encoding='utf-8')

# Generate profile report
profile = ProfileReport(df, title="Pandas Profiling Report")
profile.to_file("pandas_profiling_report.html")


# SweetViz
import pandas as pd
import sweetviz as sv

# Read CSV with UTF-8 encoding
df = pd.read_csv('output_utf8.csv', encoding='utf-8')

# Generate Sweetviz report
report = sv.analyze(df)
report.show_html('sweetviz_report.html')


# D tale
pip install dtale
import pandas as pd
import dtale

# Read CSV with UTF-8 encoding
df = pd.read_csv('output_utf8.csv', encoding='utf-8')

# Show D-Tale interface
d = dtale.show(df)
d.open_browser()



# outlier analysis
import seaborn as sns
sns.boxplot(raw_data.scrap_steel)
sns.boxplot(raw_data.pig_iron)  #
sns.boxplot(raw_data.iron_ore)   #
sns.boxplot(raw_data.phosphorus)
sns.boxplot(raw_data.carbon)  
sns.boxplot(raw_data.melting_time_EAF)
sns.boxplot(raw_data.Yield)
sns.boxplot(raw_data.BF_SCT)
sns.boxplot(raw_data.EAF_SCT)
sns.boxplot(raw_data.LRF_SCT)
sns.boxplot(raw_data.Total_CT)
sns.boxplot(raw_data.OriginalCost_Ton) #
sns.boxplot(raw_data.new_scrap_steel) #
sns.boxplot(raw_data.new_pig_iron) #
sns.boxplot(raw_data.new_iron_ore) #
sns.boxplot(raw_data.new_el_con)
sns.boxplot(raw_data.BF_El_new)
sns.boxplot(raw_data.EAF_El_new)
sns.boxplot(raw_data.LRF_El_new)
sns.boxplot(raw_data.prod_vol)
sns.boxplot(raw_data.BF_El)
sns.boxplot(raw_data.EAF_El)
sns.boxplot(raw_data.LRF_El)
sns.boxplot(raw_data.Total_El_Con)
sns.boxplot(raw_data.BF_El_new)
sns.boxplot(raw_data.EAF_El_new)   # 
sns.boxplot(raw_data.LRF_El_new)
sns.boxplot(raw_data.Estimated_cost_per_ton)
sns.boxplot(raw_data.BF_El)



                    # outlier treatment #
import numpy as np                    
IQR = raw_data['phosphorus'].quantile(0.75) - raw_data['phosphorus'].quantile(0.25)
lower_limit = raw_data['phosphorus'].quantile(0.25) - 1.5*IQR
upper_limit = raw_data['phosphorus'].quantile(0.75) + 1.5*IQR

# flagging the outliers #
outliers_df = np.where(raw_data.phosphorus > upper_limit, True, np.where(raw_data.phosphorus < lower_limit, True, False))

# Replacing the outlier values with the upper and lower limits #
raw_data['phosphorus'] = pd.DataFrame(np.where(raw_data['phosphorus'] > upper_limit, upper_limit, np.where(raw_data['phosphorus'] < lower_limit, lower_limit, raw_data['phosphorus'])))
sns.boxplot(raw_data.phosphorus)

                    
IQR = raw_data['prod_vol'].quantile(0.75) - raw_data['prod_vol'].quantile(0.25)
lower_limit = raw_data['prod_vol'].quantile(0.25) - 1.5*IQR
upper_limit = raw_data['prod_vol'].quantile(0.75) + 1.5*IQR

# flagging the outliers #
outliers_df = np.where(raw_data.prod_vol > upper_limit, True, np.where(raw_data.prod_vol < lower_limit, True, False))


# Replacing the outlier values with the upper and lower limits #
raw_data['prod_vol'] = pd.DataFrame(np.where(raw_data['prod_vol'] > upper_limit, upper_limit, np.where(raw_data['prod_vol'] < lower_limit, lower_limit, raw_data['prod_vol'])))

sns.boxplot(raw_data.prod_vol)


IQR = raw_data['BF_El'].quantile(0.75) - raw_data['BF_El'].quantile(0.25)
lower_limit = raw_data['BF_El'].quantile(0.25) - 1.5*IQR
upper_limit = raw_data['BF_El'].quantile(0.75) + 1.5*IQR

# flagging the outliers #
outliers_df = np.where(raw_data.BF_El > upper_limit, True, np.where(raw_data.BF_El < lower_limit, True, False))


# Replacing the outlier values with the upper and lower limits #
raw_data['BF_El'] = pd.DataFrame(np.where(raw_data['BF_El'] > upper_limit, upper_limit, np.where(raw_data['BF_El'] < lower_limit, lower_limit, raw_data['BF_El'])))

sns.boxplot(raw_data.BF_El)


IQR = raw_data['EAF_El'].quantile(0.75) - raw_data['EAF_El'].quantile(0.25)
lower_limit = raw_data['EAF_El'].quantile(0.25) - 1.5*IQR
upper_limit = raw_data['EAF_El'].quantile(0.75) + 1.5*IQR

# flagging the outliers #
outliers_df = np.where(raw_data.EAF_El > upper_limit, True, np.where(raw_data.EAF_El < lower_limit, True, False))


# Replacing the outlier values with the upper and lower limits #
raw_data['EAF_El'] = pd.DataFrame(np.where(raw_data['EAF_El'] > upper_limit, upper_limit, np.where(raw_data['EAF_El'] < lower_limit, lower_limit, raw_data['EAF_El'])))

sns.boxplot(raw_data.EAF_El)


IQR = raw_data['LRF_El'].quantile(0.75) - raw_data['LRF_El'].quantile(0.25)
lower_limit = raw_data['LRF_El'].quantile(0.25) - 1.5*IQR
upper_limit = raw_data['LRF_El'].quantile(0.75) + 1.5*IQR

# flagging the outliers #
outliers_df = np.where(raw_data.LRF_El > upper_limit, True, np.where(raw_data.LRF_El < lower_limit, True, False))


# Replacing the outlier values with the upper and lower limits #
raw_data['LRF_El'] = pd.DataFrame(np.where(raw_data['LRF_El'] > upper_limit, upper_limit, np.where(raw_data['LRF_El'] < lower_limit, lower_limit, raw_data['LRF_El'])))

sns.boxplot(raw_data.LRF_El)


IQR = raw_data['Total_CT'].quantile(0.75) - raw_data['Total_CT'].quantile(0.25)
lower_limit = raw_data['Total_CT'].quantile(0.25) - 1.5*IQR
upper_limit = raw_data['Total_CT'].quantile(0.75) + 1.5*IQR

# flagging the outliers #
outliers_df = np.where(raw_data.Total_CT > upper_limit, True, np.where(raw_data.Total_CT < lower_limit, True, False))


# Replacing the outlier values with the upper and lower limits #
raw_data['Total_CT'] = pd.DataFrame(np.where(raw_data['Total_CT'] > upper_limit, upper_limit, np.where(raw_data['Total_CT'] < lower_limit, lower_limit, raw_data['Total_CT'])))

sns.boxplot(raw_data.Total_CT)

IQR = raw_data['BF_El'].quantile(0.75) - raw_data['BF_El'].quantile(0.25)
lower_limit = raw_data['BF_El'].quantile(0.25) - 1.5*IQR
upper_limit = raw_data['BF_El'].quantile(0.75) + 1.5*IQR

# flagging the outliers #
outliers_df = np.where(raw_data.BF_El > upper_limit, True, np.where(raw_data.BF_El < lower_limit, True, False))


# Replacing the outlier values with the upper and lower limits #
raw_data['BF_El'] = pd.DataFrame(np.where(raw_data['BF_El'] > upper_limit, upper_limit, np.where(raw_data['BF_El'] < lower_limit, lower_limit, raw_data['BF_El'])))

sns.boxplot(raw_data.BF_El)

IQR = raw_data['LRF_El'].quantile(0.75) - raw_data['LRF_El'].quantile(0.25)
lower_limit = raw_data['LRF_El'].quantile(0.25) - 1.5*IQR
upper_limit = raw_data['LRF_El'].quantile(0.75) + 1.5*IQR

# flagging the outliers #
outliers_df = np.where(raw_data.LRF_El > upper_limit, True, np.where(raw_data.LRF_El < lower_limit, True, False))


# Replacing the outlier values with the upper and lower limits #
raw_data['LRF_El'] = pd.DataFrame(np.where(raw_data['LRF_El'] > upper_limit, upper_limit, np.where(raw_data['LRF_El'] < lower_limit, lower_limit, raw_data['LRF_El'])))

sns.boxplot(raw_data.LRF_El)


IQR = raw_data['Total_El_Con'].quantile(0.75) - raw_data['Total_El_Con'].quantile(0.25)
lower_limit = raw_data['Total_El_Con'].quantile(0.25) - 1.5*IQR
upper_limit = raw_data['Total_El_Con'].quantile(0.75) + 1.5*IQR

# flagging the outliers #
outliers_df = np.where(raw_data.Total_El_Con > upper_limit, True, np.where(raw_data.Total_El_Con < lower_limit, True, False))


# Replacing the outlier values with the upper and lower limits #
raw_data['Total_El_Con'] = pd.DataFrame(np.where(raw_data['Total_El_Con'] > upper_limit, upper_limit, np.where(raw_data['Total_El_Con'] < lower_limit, lower_limit, raw_data['Total_El_Con'])))

sns.boxplot(raw_data.Total_El_Con)


IQR = raw_data['carbon'].quantile(0.75) - raw_data['carbon'].quantile(0.25)
lower_limit = raw_data['carbon'].quantile(0.25) - 1.5*IQR
upper_limit = raw_data['carbon'].quantile(0.75) + 1.5*IQR

# flagging the outliers #
outliers_df = np.where(raw_data.carbon > upper_limit, True, np.where(raw_data.carbon < lower_limit, True, False))

# Replacing the outlier values with the upper and lower limits #
raw_data['carbon'] = pd.DataFrame(np.where(raw_data['carbon'] > upper_limit, upper_limit, np.where(raw_data['carbon'] < lower_limit, lower_limit, raw_data['carbon'])))

sns.boxplot(raw_data.carbon)


IQR = raw_data['Yield'].quantile(0.75) - raw_data['Yield'].quantile(0.25)
lower_limit = raw_data['Yield'].quantile(0.25) - 1.5*IQR
upper_limit = raw_data['Yield'].quantile(0.75) + 1.5*IQR

# flagging the outliers #
outliers_df = np.where(raw_data.Yield > upper_limit, True, np.where(raw_data.Yield < lower_limit, True, False))


# Replacing the outlier values with the upper and lower limits #
raw_data['Yield'] = pd.DataFrame(np.where(raw_data['Yield'] > upper_limit, upper_limit, np.where(raw_data['Yield'] < lower_limit, lower_limit, raw_data['Yield'])))

sns.boxplot(raw_data.Yield)


# Encoding categorical data
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
enc_df = pd.DataFrame(enc.fit_transform(raw_data.iloc[:, 1:3]).toarray())
enc_df



                            # Transformation #
import scipy.stats as stats                            
import pylab

# checking for normal distribution #
stats.probplot(raw_data['Total_El_Con'], dist = 'norm', plot=pylab)
stats.probplot(raw_data['Estimated_cost_per_ton'], dist = 'norm', plot = pylab)


#  Function Transformation
import numpy as np           
stats.probplot(np.log(raw_data.Total_El_Con), dist = 'norm', plot = pylab)
stats.probplot(np.log(raw_data.Estimated_cost_per_ton), dist = 'norm', plot = pylab)


# power transformation - Yeo-Johnson transformation #
from feature_engine import transformation
tf = transformation.YeoJohnsonTransformer(variables='Total_El_Con')
raw_data_tf = tf.fit_transform(raw_data)

prob = stats.probplot(raw_data_tf['Total_El_Con'], dist = 'norm', plot = pylab)


tf = transformation.YeoJohnsonTransformer(variables = 'Estimated_cost_per_ton')
raw_data_tf = tf.fit_transform(raw_data)

prob = stats.probplot(raw_data_tf.Estimated_cost_per_ton, dist='norm', plot=pylab)

                            

# Save to CSV
raw_data.to_csv("clean_utf8.csv", index=False, encoding='utf-8')

raw_data.to_csv('data.csv', index=False)

import os
print(os.getcwd())


# time conversion
from datetime import timedelta

raw_data['melting_time_EAF'] = pd.to_timedelta(raw_data['melting_time_EAF'], unit='h')
raw_data['BF_SCT'] = pd.to_timedelta(raw_data['BF_SCT'], unit='h')
raw_data['EAF_SCT'] = pd.to_timedelta(raw_data['EAF_SCT'], unit='h')
raw_data['LRF_SCT'] = pd.to_timedelta(raw_data['LRF_SCT'], unit='h')
raw_data['Total_CT'] = pd.to_timedelta(raw_data['Total_CT'], unit='h')



# Save the DataFrame to an Excel file
raw_data.to_excel('data_3.xlsx', index=False)


    









