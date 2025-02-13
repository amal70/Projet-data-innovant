#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd # type: ignore

# Charger le fichier Excel
file_path = "/Users/amaloubaba/Downloads/DI/DATA_UGA.xlsx"
xls = pd.ExcelFile(file_path)

# Charger la feuille de calcul
df = pd.read_excel(xls, sheet_name='Sheet1')


# In[9]:


df


# In[11]:


# Sauvegarde du fichier transformé avec les résultats
output_path = "/Users/amaloubaba/Downloads/DI/DATA_UGA_FINAL.xlsx"
df.to_excel(output_path, index=False)


# In[ ]:




