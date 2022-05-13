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


#the use of the fillna() in the array
dict = {
    "FirstScore":[100,90,np.nan,95],
    "SecondScore":[30,45,56,np.nan],
    "thirdScore":[np.nan,40,80,98]
}
print("the dictionary is ")
print(dict)
df = pd.DataFrame(dict)
print(df)
print("after the use of fillna()")
print(df.fillna(0))

#the use of  dropna() in pandas
dict1 = {
    "FirstScore":[1,2,3,np.nan,23],
    "SecondScore":[11,22,33,45,np.nan],
    "thirdScore":[111,np.nan,333,np.nan,555],
    "fourthScore":[1111,2222,np.nan,np.nan,222]
}
print("the dict is ")
print(dict1)
df = pd.DataFrame(dict1)
print(df)
print("after the use of dropna()")
print(df.dropna())


#applying the iteration over rows 
dict11 = {
    "Name":["Sunil","Harish","Suman","Arti"],
    "degree":["Btech","Btech","11","7"],
    "score":[90,99,98,100]
}
print("the dict is ")
print(dict11)
df = pd.DataFrame(dict11)
print(df)
for i , j in df.iterrows():
    print(i,j)
    print("->>")

# applying iteration overs the column
# dict21 = {
#     "Name":["Sunil","Harish","Arti","Suman","Khushboo"],
#     "degree":["Btech,Btech","7th","11th","10th"],
#     "score":[90,99,99,100,100]
# }
# print("the dictionary is ")
# print(dict21)
# df1 = pd.DataFrame(dict21)
# print("the dataframe is ")
# print(df1)

#to iterate the dataframe over column first convert into the list 
# column = list(df1)
# print("the cloumn of the dataframe is ")
# print(column)
# for i in column:
#     print(df1[i])
#     print("****->*******")

#concatenating DataFrame using concate()
dict1 = {
    "Name":["Jai","Princi","Gaurav","Anuj"],
    "Age":[27,24,22,32],
    "Address":["Nagpur","Kanpur","Alahabad","kannauj"],
    "Qualifications":["Msc","MA","MCA","Phd"]
}
dict2 = {
    "Name":["Abhi","Ayushi","Dhiraj","Hitesh"],
    "Age":[17,14,12,52],
    "Address":["Nagpur","Kanpur","Allahabad","Kannauj"],
    "Qualification":["Btech","B.A","Bcom","B.hons"]
}
print("the data1 is ")
print(dict1)
print("the data2 is ")
print(dict2)

#now concatenating the two different data 

#First convert into the dataFrame 
df1 = pd.DataFrame(dict1,index=[0,1,2,3])
print("the first DataFrame is ")
print(df1)

#Second convert into th dataFrame 
df2 = pd.DataFrame(dict2,index=[4,5,6,7])
print("the second dataFrame is ")
print(df2)

Frames = [df1,df2]
res1 = pd.concat(Frames)
print("after concatenation of the two data sets")
print(res1)

#Finding the intersection of the dataFrame 
dict31 = {
    "Name":["Jai","Princi","Gaurav","Anuj"],
    "Age":[27,24,22,32],
    "Address":["Nagpur","Kanpur","Allahabad","Kannauj"],
    "Qualification":["MSc","MA","MCA","Phd"],
    "Mobile No":[97,91,58,76]
}

dict32 = {
    "Name":["Gaurav","Anuj","Dhiraj","Hitesh"],
    "Age":[22,32,12,52],
    "Address":["Allahabad","Kannauj","Allahabad","Kannauj"],
    "Qualification":["MCA","Phd","Bcom","B.Hons"],
    "salary":[1000,2000,3000,4000]
}
print("the first data sets is ")
print(dict31)
print("the second datasets is ")
print(dict32)

#converting the datasets into dataFrame from the dictinary
df1 = pd.DataFrame(dict31,index=[0,1,2,3])
print("the  first dataFrame is ")
print(df1)
df2 = pd.DataFrame(dict32,index=[2,3,6,7])
print("the second dataFrame is ")
print(df2)

Frames1 = [df1,df2]
print("the Frame1 is ")
print(Frames1)
res = pd.concat(Frames1,axis=1,join="inner")
print(res)
