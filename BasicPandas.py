import pandas as pd
list1 = ["sunil ","Harish","Arti","Suman"]
df = pd.DataFrame(list1)
print("the dataframe is ")
print(df)
#creating the dataFrame from the dictionary
dict1 = {
    "name":["Sunil","Harish","Arti","Suman","khushboo"],
    "age":[12,13,14,15,16]
}
print("the dictionery is ")
print(dict1)
df = pd.DataFrame(dict1)
print("the dataFrame is ")
print(df)


#Creating the dictionary of the employee data
data = {
    "Name":["Sunil","Harish","Suman","khushboo"],
    "age":[1,2,3,4],
    "address":["Lucknow","Kanpur","delhi","Gurugram"]
}
print("the dictionary is ")
print(data)
df = pd.DataFrame(data)
print("the dataFrame is ")
print(df)
# selecting the two column in the pd.DataFrame
print("the two column is ")
print(df[["Name","age"]])
# checking the missing values 
import numpy as np
list1 = {
    "FirstScore":[100,np.nan,200,300,np.nan],
    "SecondScore":[300,500,600,np.nan,np.nan]
}
print("the list of the array is ")
print(list1)
df = pd.DataFrame(list1)
print("the dataFrame is ")
print(df)
print("checking the missing values in the list")
print(df.isnull())
