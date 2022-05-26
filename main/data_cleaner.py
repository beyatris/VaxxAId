import pandas as pd
import numpy as np

patients2021 = pd.read_csv('../data/2021VAERSDATA.csv', encoding='latin1')
vaccine2021 = pd.read_csv('../data/2021VAERSVAX.csv', encoding='latin1')

patients2022 = pd.read_csv('../data/2022VAERSDATA.csv', encoding='latin1')
vaccine2022 = pd.read_csv('../data/2022VAERSVAX.csv', encoding='latin1')

# vaccine = pd.concat([vaccine2021, vaccine2022], axis=0)

# Joining the datasets on VAERS_ID
patients2021 = patients2021.join(vaccine2021.set_index('VAERS_ID'), on='VAERS_ID', how='inner')
patients2022 = patients2022.join(vaccine2022.set_index('VAERS_ID'), on='VAERS_ID', how='inner')

patients2021 = patients2021[patients2021['VAX_TYPE']=='COVID19']
patients2022 = patients2022[patients2022['VAX_TYPE']=='COVID19']

patients = pd.concat([patients2021, patients2022], axis=0)

features = ['VAERS_ID','STATE','AGE_YRS','SEX','DIED','L_THREAT','ER_VISIT','HOSPITAL','DISABLE','BIRTH_DEFECT','RECOVD','V_ADMINBY','VAX_TYPE','VAX_MANU','VAX_SITE','VAX_ROUTE']
patients = patients[features]

patients = patients.drop(['VAX_TYPE'],axis=1)

patients.to_csv('../data/20212022DATA.csv', index=False)
