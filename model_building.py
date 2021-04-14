# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 13:01:40 2021

@author: samru
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dfc = pd.read_csv('cleaned_linkedin_data.csv')

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

dfc.columns

model_dfc = dfc[['number_of_apps','n_state','Accommodation and Food Services',
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

dummies_dfc = pd.get_dummies(model_dfc)

from sklearn.model_selection import train_test_split

X = dummies_dfc.drop('number_of_apps', axis =1)
y = dummies_dfc.number_of_apps.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y, X_sm)
model.fit().summary()

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score


lm = LinearRegression()
lm.fit(X_train, y_train)

np.mean(cross_val_score(lm, X_train, y_train, scoring = 'neg_mean_absolute_error', cv=5))

lm_l = Lasso(alpha=.2)
lm_l.fit(X_train,y_train)
np.mean(cross_val_score(lm_l, X_train, y_train, scoring = 'neg_mean_absolute_error'))

alpha = []
error = []

for i in range(1,100):
    alpha.append(i/100)
    lml = Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lml, X_train, y_train, scoring = 'neg_mean_absolute_error')))
    
plt.plot(alpha,error)

err = tuple(zip(alpha, error))
error_dfc = pd.DataFrame(err, columns = ['alpha', 'error'])
error_dfc[error_dfc.error == max(error_dfc.error)]

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()

cross_val_score(rf,X_train,y_train,scoring = 'neg_mean_absolute_error' )

from sklearn.model_selection import GridSearchCV

parameters = {'n_estimators': range(10,200,10), 'criterion':('mse','mae'), 'max_features':('auto','sqrt','log2')}

gs = GridSearchCV(rf, parameters, scoring='neg_mean_absolute_error',cv=5)
gs.fit(X_train, y_train)

gs.best_score_
gs.best_estimator_

tpred_lm = lm.predict(X_test)
tpred_lml = lm_l.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test, tpred_lm)
mean_absolute_error(y_test, tpred_lml)
mean_absolute_error(y_test, tpred_rf)
mean_absolute_error

import pickle
pick1 = {'model':gs.best_estimator_}
pickle.dump(pick1, open('model_file'+'.p',"wb"))
file_name='model_file.p'
with open(file_name,'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']
    
model.predict(X_test.iloc[1,:].values.reshape(1,-1))

X_test.iloc[1,:].values

list(X_test.iloc[1,:])
