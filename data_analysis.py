import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "heart(2).csv"
df=pd.read_csv("C:/Users/Hp/Downloads/heart (2).csv")
print("First five rows of the dataset:")
print(df.tail())

chol="chol"
if chol in df.columns:
    average_value = df[chol].mean()
    print(f"\nAverage of {chol} : {average_value}")
else:
    print(f"\nColumn '{chol}' not found in the dataset.")    

print("Statistics Summary:")
print(df.describe()) 

missing_values = df.isnull().sum()
print("\nMissing Values in each coloumn:")
print(missing_values)


target="target"
if target in df.columns:
    target = df[target].value_counts()
    target.plot(kind='bar',color='skyblue')
    plt.title(f'Bar Chart of{target}')
    plt.xlabel('Categories')
    plt.ylabel('Count')
    plt.show()
else:
    print(f"\nColumn {target} not found or not target") 

trestbps="Trestbps"
chol="Choletrol"
if trestbps in df.columns and chol in df.columns:
    plt.scatter(df[trestbps],df[chol],alpha=0.5, color='teal')
    plt.title(f'Scatter Plot of {trestbps} vs.{chol}')
    plt.xlabel(trestbps)
    plt.ylabel(chol)
    plt.show()  
else:
    print(f'\nColumns {trestbps} and/or {chol} not found in the  dataset.')

plt.figure(figsize=(10,8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm',fmt=".2f")
plt.title('Heatmap of Correlation Matrix')
plt.show()             

