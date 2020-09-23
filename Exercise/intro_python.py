import pandas as pd
import matplotlib.pyplot as plt

#Load data
titanic = pd.read_csv("titanic.csv")

#Remove rows whose element in column 'Age' is NaN
titanic = titanic.dropna(subset=['Age'])

#Compute mean age
print(f"The average age is {titanic['Age'].mean():.2f}")

#Plot histogram of age
#plt.show(titanic.hist(column='Age'))

#Bonus. Compute correlation between age and death
age = titanic['Age']
death = titanic['Survived']

corr = age.corr(death)
print(f"The correlation between age and death is {corr:.2f}")