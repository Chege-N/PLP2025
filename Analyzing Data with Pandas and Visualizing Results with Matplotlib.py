#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Task 1: Load and Explore the Dataset

# In[3]:


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)


# In[6]:


print("First 5 rows of the dataset:")
print(df.head())


# In[7]:


print("\nDataset Info:")
print(df.info())


# In[8]:


print("\nMissing Values:")
print(df.isnull().sum())


# # Task 2: Basic Data Analysis
# # Basic statistics of numerical columns

# In[9]:


print("\nBasic Statistics:")
print(df.describe())


# In[10]:


# Group by species and compute mean for numerical columns
grouped_means = df.groupby('species').mean()
print("\nMean values by species:")
print(grouped_means)


# In[11]:


# Observations:
print("\nObservations from Analysis:")
print("- The dataset contains 150 samples with 5 columns: 4 numerical features and 1 categorical (species).")
print("- No missing values in the dataset.")
print("- Setosa species tends to have smaller measurements overall compared to versicolor and virginica.")
print("- Virginica generally has the largest sepal and petal measurements.")


# # Task 3: Data Visualization
# # Create a figure with subplots

# In[12]:


plt.figure(figsize=(15, 10))


# In[13]:


# 1. Line Chart (Using petal length as a pseudo-time series for demonstration)
plt.subplot(2, 2, 1)
for species in df['species'].unique():
    species_data = df[df['species'] == species]['petal_length']
    plt.plot(species_data.values, label=species)
plt.title('Petal Length Across Samples by Species')
plt.xlabel('Sample Index')
plt.ylabel('Petal Length (cm)')
plt.legend()


# In[14]:


# 2. Bar Chart (Average sepal length by species)
plt.subplot(2, 2, 2)
means = df.groupby('species')['sepal_length'].mean()
plt.bar(means.index, means.values, color=['#FF9999', '#66B2FF', '#99FF99'])
plt.title('Average Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Length (cm)')


# In[15]:


# 3. Histogram (Petal length distribution)
plt.subplot(2, 2, 3)
plt.hist(df['petal_length'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')


# In[16]:


# 4. Scatter Plot (Sepal length vs Petal length)
plt.subplot(2, 2, 4)
for species in df['species'].unique():
    species_data = df[df['species'] == species]
    plt.scatter(species_data['sepal_length'], species_data['petal_length'], 
                label=species, alpha=0.6)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()


# In[17]:


# Adjust layout and display
plt.tight_layout()
plt.show()


# In[18]:


# Save the plots to a file
plt.savefig('iris_analysis_plots.png')
print("\nPlots saved as 'iris_analysis_plots.png'")


# In[19]:


# Additional Findings
print("\nAdditional Findings:")
print("- The line chart shows distinct patterns in petal length for each species.")
print("- The bar chart confirms setosa has the shortest average sepal length.")
print("- The histogram shows petal length has a bimodal distribution.")
print("- The scatter plot reveals clear clustering of species based on sepal and petal length.")


# In[ ]:




