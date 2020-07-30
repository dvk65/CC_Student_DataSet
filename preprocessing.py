import pandas as pd

data=pd.read_csv("DS_DATESET.csv")
data.head()
data_try=f'DS_DATESET.csv'
data.info(data_try)
data.isnull().sum()
data.drop(["Certifications/Achievement/ Research papers","Link to updated Resume (Google/ One Drive link preferred)","link to Linkedin profile","First Name", "Last Name", "Zip Code","Contact Number","DOB [DD/MM/YYYY]","Emergency Contact Number", "Course Type", "Current Employment Status"], axis=1, inplace=True)
data