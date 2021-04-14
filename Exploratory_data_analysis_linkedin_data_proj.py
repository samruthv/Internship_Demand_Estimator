# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:41:31 2021

@author: samru
"""


import pandas as pd
import matplotlib.pyplot as mplt
import seaborn as sb
import numpy as np

dfc = pd.read_csv('cleaned_linkedin_data.csv')
dfc.head()
dfc.columns


#Bit more cleaning
dfc.rename(columns = {'Job Location':'Job_Location'}, inplace=True)

dfc['n_state'] = dfc.apply(lambda x: x.Job_Location if x.states =='Not Specified US State' else x.states, axis =1)
dfc['n_state'] = dfc['n_state'].apply(lambda x: x.split(',')[0] if ',' in x else x)

dfc['n_state'] = dfc['n_state'].apply(lambda x: x if x.strip() != 'New York' else 'NY')
dfc['n_state'] = dfc['n_state'].apply(lambda x: x if x.strip() != 'Michigan' else 'MI')
dfc['n_state'] = dfc['n_state'].apply(lambda x: x if x.strip() != 'New Jersey' else 'NJ')
dfc['n_state'] = dfc['n_state'].apply(lambda x: x if x.strip() != 'California' else 'CA')
dfc['n_state'] = dfc['n_state'].apply(lambda x: x if x.strip() != 'Georgia' else 'GA')
dfc['n_state'] = dfc['n_state'].apply(lambda x: x if x.strip() != 'Oregon' else 'OR')
dfc['n_state'] = dfc['n_state'].apply(lambda x: x if x.strip() != 'United States' else 'Not Specified US State')

n_state = dfc.n_state.value_counts()


#which industries attract more attention
#which locations attract more attention
#where are these industries located

stats = dfc.describe()


bins1 = [5,10,15,20,25,30,35,40,45,50,55,60,65,70]
dfc.hist('Time_in_Days',bins=bins1, edgecolor='black')


bins2 = [5,10,15,20,25,30,35,40,45,50,55,60,65,70]
dfc.hist('apps_per_day',bins=bins2, edgecolor='black')

bins3 = [5,10,15,20,25,30,35,40,45,50,55,60,65,70]
dfc.hist('number_of_apps',bins=bins3, edgecolor='black')

dfc.boxplot(column = ['number_of_apps','Time_in_Days','apps_per_day'])



cmap = sb.diverging_palette(220, 42, as_cmap=True)
sb.heatmap(dfc[['number_of_apps','Time_in_Days','apps_per_day']].corr(), vmax=.3, center=0, cmap=cmap, square=True,linewidths=.5, cbar_kws={"shrink":.5})

dfc.columns

cat=dfc[['Job_Location', 'Accommodation and Food Services',
       'Administration, Business Support and Waste Management Services',
       'Agriculture, Forestry, Fishing and Hunting',
       'Arts, Entertainment and Recreation', 'Construction',
       'Educational Services', 'Finance and Insurance',
       'Healthcare and Social Assistance', 'Information', 'Manufacturing',
       'Mining', 'Professional, Scientific and Technical Services',
       'Real Estate and Rental and Leasing', 'Retail Trade',
       'Transportation and Warehousing', 'Utilities', 'Wholesale Trade',
       'Advisory and Financial Services', 'Business Franchises',
       'Consumer Goods and Services',
       'Industrial Machinery, Gas and Chemicals', 'Life Sciences',
       'Online Retail', 'Retail Market Reports',
       'Specialist Engineering, Infrastructure and Contractors', 'Technology',
       'Energy', 'Politics', 'Pharmaceutical', 'Defense', 'Nonprofit',
       'environmental', 'civic', 'Cosmetics and Apperel', 'n_state']]

for i in cat.columns:
    cat_number = dfc[i].value_counts()
    print('graph for %s: total =%d'%(i,len(cat_number)))
    chart=sb.barplot(x=cat_number.index,y=cat_number)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
    
    mplt.show()
    
for i in cat[['Company Name']].columns:
    cat_number = dfc[i].value_counts()[:20]
    print('graph for %s: total =%d'%(i,len(cat_number)))
    chart=sb.barplot(x=cat_number.index,y=cat_number)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
    
    mplt.show()
    


#The compatition, bumber of applicants per posting by state
pd.pivot_table(dfc, index = 'n_state', values = 'number_of_apps').sort_values('number_of_apps',ascending=False)

#The oppertunity, number of postings in that state
pd.pivot_table(dfc, index = 'n_state', values = 'number_of_apps', aggfunc = 'count').sort_values('number_of_apps',ascending=False)



dfc_industry = dfc[['Accommodation and Food Services',
       'Administration, Business Support and Waste Management Services',
       'Agriculture, Forestry, Fishing and Hunting',
       'Arts, Entertainment and Recreation', 'Construction',
       'Educational Services', 'Finance and Insurance',
       'Healthcare and Social Assistance', 'Information', 'Manufacturing',
       'Mining', 'Professional, Scientific and Technical Services',
       'Real Estate and Rental and Leasing', 'Retail Trade',
       'Transportation and Warehousing', 'Utilities', 'Wholesale Trade',
       'Advisory and Financial Services', 'Business Franchises',
       'Consumer Goods and Services',
       'Industrial Machinery, Gas and Chemicals', 'Life Sciences',
       'Online Retail', 'Retail Market Reports',
       'Specialist Engineering, Infrastructure and Contractors', 'Technology',
       'Energy', 'Politics', 'Pharmaceutical', 'Defense', 'Nonprofit',
       'environmental', 'civic', 'Cosmetics and Apperel']]

#The compatition in each industry
for i in dfc_industry.columns:
    indus= pd.pivot_table(dfc, index=[i], values = 'number_of_apps').sort_values('number_of_apps', ascending=False)
    print(indus)
#The oppertunity in each industry
for i in dfc_industry.columns:

    print(pd.pivot_table(dfc, index=i, values = 'number_of_apps', aggfunc = 'count').sort_values('number_of_apps', ascending=False))
    
 
#The compatition in each industry by state       
for i in dfc_industry.columns:
    print(pd.pivot_table(dfc, index='n_state', columns =i , values = 'number_of_apps')) 
#The oppertunity in each industry by state
for i in dfc_industry.columns:
    print(pd.pivot_table(dfc, index='n_state', columns =i , values = 'number_of_apps', aggfunc = 'count')) 
    


'''



dfc.boxplot(column = ['number_of_apps','Time_in_Days','apps_per_day'])

dfc[['number_of_apps','Time_in_Days', 'apps_per_day']].corr()
'''