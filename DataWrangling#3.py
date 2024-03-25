#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

get_ipython().system('pip install matplotlib-venn')

from matplotlib_venn import venn2, venn2_circles


# In[2]:


df = pd.read_csv('DW3_set_exercise.csv')


# In[3]:


diabetes_codes = ['E08', 'E09', 'E10', 'E11', 'E13']
covid_codes = ['U07.1', 'J12.82']


# In[4]:


diabetes_patients = df[df['Diagnosis Code'].isin(diabetes_codes)]['Patient ID'].unique()
diabetes_cardinality = len(diabetes_patients)


# In[5]:


covid_patients = df[df['Diagnosis Code'].isin(covid_codes)]['Patient ID'].unique()
covid_cardinality = len(covid_patients)


# In[6]:


intersection_patients = set(diabetes_patients) & set(covid_patients)
intersection_cardinality = len(intersection_patients)


# In[7]:


union_patients = set(diabetes_patients) | set(covid_patients)
union_cardinality = len(union_patients)


# In[8]:


venn2(subsets=(diabetes_cardinality, covid_cardinality, intersection_cardinality),
      set_labels=('Diabetes', 'COVID'))
plt.title('Venn Diagram of Diabetes and COVID Sets')
plt.show()


# In[9]:


diabetes_after_covid = df[(df['Diagnosis Code'].isin(diabetes_codes)) & 
                           (df['Patient ID'].isin(covid_patients))]['Patient ID'].unique()
diabetes_after_covid_cardinality = len(diabetes_after_covid)


# In[10]:


diabetes_codes_after_covid = df[(df['Diagnosis Code'].isin(diabetes_codes)) & 
                                 (df['Patient ID'].isin(covid_patients))]['Diagnosis Code'].value_counts()


# In[11]:


print("1. Diabetes Set:")
print("a. Patients with Diabetes:", diabetes_patients)
print("b. Cardinality of Diabetes set:", diabetes_cardinality)
print()
print("2. COVID Set:")
print("a. Patients with COVID:", covid_patients)
print("b. Cardinality of COVID set:", covid_cardinality)
print()
print("3. Intersection Set:")
print("a. Patients with Diabetes and COVID:", intersection_patients)
print("b. Cardinality of Intersection set:", intersection_cardinality)
print()
print("4. Union Set:")
print("a. Patients with Diabetes or COVID:", union_patients)
print("b. Cardinality of Union set:", union_cardinality)
print()
print("6. Diabetes only after COVID Set:")
print("a. Patients with Diabetes only after COVID:", diabetes_after_covid)
print("b. Cardinality of Diabetes only after COVID set:", diabetes_after_covid_cardinality)
print("c. Count breakdown for diabetes codes after COVID:")
print(diabetes_codes_after_covid)


# In[ ]:




