# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 15:18:58 2021

@author: samru
"""
import pandas as pd

df = pd.read_csv('DF_MAX.csv')


unique_data=df.drop_duplicates(subset=['Position of Title', 'Company Name', 'Job Location', 'Job Function', 'Industries'],keep='last')

# %%
#interest based on location
#interest based on industry
#interst of company
df_unique = pd.read_csv('DF_unique.csv')

df_unique['under_25_apps'] = df_unique['Number Of Applicants'].apply(lambda x: 1 if 'Be among the first' in x else 0)
df_unique['over_200_apps'] = df_unique['Number Of Applicants'].apply(lambda x: 1 if 'Over' in x else 0)

applicants = df_unique['Number Of Applicants'].apply(lambda x: x.split('appl')[0])
minus_BATFandO = applicants.apply(lambda x: x.replace('Be among the first', '').replace('Over',''))


df_unique['number_of_apps'] = minus_BATFandO.astype(str).astype(int)


df_unique['minutes'] = df_unique['Posted Time'].apply(lambda x: 1 if 'minute' in x else 0)
df_unique['hours'] = df_unique['Posted Time'].apply(lambda x: 1 if 'hour' in x else 0)
df_unique['days'] = df_unique['Posted Time'].apply(lambda x: 1 if 'day' in x else 0)
df_unique['weeks'] = df_unique['Posted Time'].apply(lambda x: 1 if 'week' in x else 0)
df_unique['months'] = df_unique['Posted Time'].apply(lambda x: 1 if 'month' in x else 0)
df_unique['years'] = df_unique['Posted Time'].apply(lambda x: 1 if 'year' in x else 0)

time = df_unique['Posted Time'].apply(lambda x: x.split('minute')[0].split('hour')[0].split('day')[0].split('week')[0].split('month')[0].split('year')[0])


df_unique['abs_time'] = time.astype(str).astype(int)
df_unique['Time_in_Days'] = (df_unique.minutes*df_unique.abs_time/1440)+(df_unique.hours*df_unique.abs_time/24)+(df_unique.days*df_unique.abs_time)+\
    (df_unique.weeks*df_unique.abs_time*7)+(df_unique.months*df_unique.abs_time*30)+(df_unique.years*df_unique.abs_time*365)
df_unique['apps_per_day'] = (df_unique.number_of_apps/df_unique.Time_in_Days) 




df_unique['states'] = df_unique['Job Location'].apply(lambda x: x.split(',')[1] if ',' in x else x)
df_unique['states'] = df_unique['states'].apply(lambda x: x.strip())

df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'new york city metropolitan area' else 'NY')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'san francisco bay area' else 'CA')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'los angeles metropolitan area' else 'CA')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'washington dc-baltimore area' else 'DC')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'denver metropolitan area' else 'CO')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'greater houston' else 'TX')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'san diego metropolitan area' else 'CA')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'texas metropolitan area' else 'TX')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'maranhão' else 'Not in US')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'greater cleveland' else 'OH')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'greater milwaukee' else 'WI')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'dayton metropolitan area' else 'OH')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'shreveport-bossier city area' else 'LA')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'utica-rome area' else 'Not in US')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'dallas-fort worth metroplex' else 'TX')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'greater minneapolis-st. paul area' else 'MN')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'nouvelle-aquitaine' else 'Not in US')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'ohio metropolitan area' else 'OH')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'atlanta metropolitan area' else 'GA')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'karnataka' else 'Not in US')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'missouri area' else 'MO')
df_unique['states'] = df_unique['states'].apply(lambda x: x if x.strip().lower() != 'united states' else 'Not Specified US State')



states=df_unique.states.value_counts()

df_unique['Accommodation and Food Services'] = df_unique['Industries'].apply(lambda x: 1 if 'food' in x.lower() or 'accomidation' in x.lower() else 0)
df_unique['Administration, Business Support and Waste Management Services'] = df_unique['Industries'].apply(lambda x: 1 if 'administration' in x.lower() or 'business support' in x.lower() or 'waste management services' in x.lower() else 0)
df_unique['Agriculture, Forestry, Fishing and Hunting'] = df_unique['Industries'].apply(lambda x: 1 if 'agriculture' in x.lower() or 'forestry' in x.lower() or 'fishing' in x.lower() or 'hunting' in x.lower() or 'farming' in x.lower() else 0)
df_unique['Arts, Entertainment and Recreation'] = df_unique['Industries'].apply(lambda x: 1 if 'arts' in x.lower() or 'entertainment' in x.lower() or 'recreation' in x.lower() or 'music' in x.lower() or 'sports' in x.lower() or 'media' in x.lower() else 0)
df_unique['Construction'] = df_unique['Industries'].apply(lambda x: 1 if 'arts' in x.lower() or 'construction' in x.lower() or 'building' in x.lower() or 'architecture' in x.lower() else 0)
df_unique['Educational Services'] = df_unique['Industries'].apply(lambda x: 1 if 'education' in x.lower() or 'educational' in x.lower() else 0)
df_unique['Finance and Insurance'] = df_unique['Industries'].apply(lambda x: 1 if 'finance' in x.lower() or 'insurance' in x.lower() or 'banking' in x.lower() else 0)
df_unique['Healthcare and Social Assistance'] = df_unique['Industries'].apply(lambda x: 1 if 'healthcare' in x.lower() or 'social assistance' in x.lower() or 'health' in x.lower() else 0)
df_unique['Information'] = df_unique['Industries'].apply(lambda x: 1 if 'information' in x.lower() or 'telecommunication' in x.lower() else 0)
df_unique['Manufacturing'] = df_unique['Industries'].apply(lambda x: 1 if 'manufacturing' in x.lower() else 0)
df_unique['Mining'] = df_unique['Industries'].apply(lambda x: 1 if 'mining' in x.lower() else 0)
df_unique['Professional, Scientific and Technical Services'] = df_unique['Industries'].apply(lambda x: 1 if 'professional' in x.lower() or 'scientific' in x.lower() or 'technical' in x.lower() else 0)
df_unique['Real Estate and Rental and Leasing'] = df_unique['Industries'].apply(lambda x: 1 if 'real estate' in x.lower() or 'rental' in x.lower() or 'leasing' in x.lower() else 0)
df_unique['Retail Trade'] = df_unique['Industries'].apply(lambda x: 1 if 'real estate' in x.lower() or 'retail' in x.lower()  else 0)
df_unique['Transportation and Warehousing'] = df_unique['Industries'].apply(lambda x: 1 if 'transportation' in x.lower() or 'warehousing' in x.lower() or 'automotive' in x.lower() or 'airlines' in x.lower() else 0)
df_unique['Utilities'] = df_unique['Industries'].apply(lambda x: 1 if 'utilities' in x.lower() or 'Utility' in x.lower()  else 0)
df_unique['Wholesale Trade'] = df_unique['Industries'].apply(lambda x: 1 if 'wholesale' in x.lower() else 0)
df_unique['Advisory and Financial Services'] = df_unique['Industries'].apply(lambda x: 1 if 'advisory' in x.lower() or 'financial services' in x.lower() else 0)
df_unique['Business Franchises'] = df_unique['Industries'].apply(lambda x: 1 if 'business' in x.lower() else 0)
df_unique['Consumer Goods and Services'] = df_unique['Industries'].apply(lambda x: 1 if 'consumer goods' in x.lower() else 0)
df_unique['Industrial Machinery, Gas and Chemicals'] = df_unique['Industries'].apply(lambda x: 1 if 'industrial' in x.lower() or 'gas' in x.lower() or 'chemicals' in x.lower() or 'oil' in x.lower() or 'supply chain' in x.lower() else 0)
df_unique['Life Sciences'] = df_unique['Industries'].apply(lambda x: 1 if 'life sciences' in x.lower() or 'life science' in x.lower() else 0)
df_unique['Online Retail'] = df_unique['Industries'].apply(lambda x: 1 if 'online' in x.lower() else 0)
df_unique['Retail Market Reports'] = df_unique['Industries'].apply(lambda x: 1 if 'marketing' in x.lower() else 0)
df_unique['Specialist Engineering, Infrastructure and Contractors'] = df_unique['Industries'].apply(lambda x: 1 if 'engineering' in x.lower()  or 'infrastructure' in x.lower() or 'contractors' in x.lower() else 0)
df_unique['Technology'] = df_unique['Industries'].apply(lambda x: 1 if 'technology' in x.lower() or 'computer' in x.lower() or 'electronics' in x.lower() or 'semiconductors' in x.lower() or 'internet' in x.lower() else 0)
df_unique['Energy'] = df_unique['Industries'].apply(lambda x: 1 if 'energy' in x.lower() or 'renewables' in x.lower() else 0)
df_unique['Politics'] = df_unique['Industries'].apply(lambda x: 1 if 'politics' in x.lower() or 'political' in x.lower() else 0)
df_unique['Pharmaceutical'] = df_unique['Industries'].apply(lambda x: 1 if 'pharmaceutical' in x.lower() else 0)
df_unique['Defense'] = df_unique['Industries'].apply(lambda x: 1 if 'defense' in x.lower() else 0)
df_unique['Nonprofit'] = df_unique['Industries'].apply(lambda x: 1 if 'nonprofit' in x.lower() else 0)
df_unique['environmental'] = df_unique['Industries'].apply(lambda x: 1 if 'environmental' in x.lower() or 'environment' in x.lower() else 0)
df_unique['civic'] = df_unique['Industries'].apply(lambda x: 1 if 'civic' in x.lower() else 0)
df_unique['Cosmetics and Apperel'] = df_unique['Industries'].apply(lambda x: 1 if 'cosmetics' in x.lower() or 'apparel' in x.lower() else 0)



df_unique.columns

df_unique.to_csv('cleaned_linkedin_data.csv', index = False)







'''
df_unique['job_state'] = df_unique['Job Location'].apply(lambda x: x.split(',')[1])


'''
'''
Accommodation and Food Services/
Administration, Business Support and Waste Management Services/2
Agriculture, Forestry, Fishing and Hunting/3
Arts, Entertainment and Recreation/4
Construction/5
Educational Services/
Finance and Insurance/
Healthcare and Social Assistance/
Information/9
Manufacturing/
Mining/
Other Services (except Public Administration)
Professional, Scientific and Technical Services/
Real Estate and Rental and Leasing/
Retail Trade/
Transportation and Warehousing/10
Utilities/
Wholesale Trade/
Advisory and Financial Services/
Business Franchises/
Consumer Goods and Services/
Industrial Machinery, Gas and Chemicals/14
Life Sciences/
Online Retail/
Retail Market Reports/
Specialist Engineering, Infrastructure and Contractors/
Technology/16

-
why are some 0???

 or 'sports' in x.lower()
 
df_unique['Cosmetics and Apperel'] = df_unique['Industries'].apply(lambda x: 1 if 'cosmetics' in x.lower() or if 'apperel' in x.lower() else 0)

 
health/
cs/
internet16/
semiconducters16/
energy_new/
politics_new/
internet16/
pharma_new/
defense_new/
banking
marketing
oil14/
farming3/
nonprofit_new/
telecommunications9/
automotive10/
supplychain
eniormental_new/
building5/
civic_new/
sports4/
policy
cosmetics and apperel_new/
electronics/
music/
'''
