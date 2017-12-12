
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np


# In[3]:

namelist = pd.read_csv('./namelist.csv')


# In[4]:

num_student = namelist.shape[0]


# In[5]:

namelist['l4d'] = namelist['ID'].apply(lambda x: x%10000)


# In[6]:

display_text = """
(a) Add new entry
(q) quit
Please select your action:
"""
var = input(display_text)
while var == 'a':
    entry_name = input("Entry name: ")
    namelist[entry_name] = np.zeros(num_student)
    var = input("Last 4 digits of student id [or type q to quit]: ")
    while var != 'q':
        if len(var) == 4:
            sid = int(var)
            if namelist.loc[namelist.l4d == sid].shape[0] > 1:
                print("More than one students found:")
                print(namelist.loc[namelist.l4d == sid])
                var = input("Enter the full student id: ")
                sid = int(var)
                namelist.loc[namelist.ID == sid, entry_name] = 1
                print(namelist.loc[namelist.ID == sid])
            else:
                namelist.loc[namelist.l4d == sid, entry_name] = 1
                print(namelist.loc[namelist.l4d == sid])
        else:
            print('You type something that is not 4 digit.')
        
        #ask again
        var = input("Last 4 digits of student id [or type q to quit]: ")
    var = input(display_text)

var = input("save to file with name: ")
writer = pd.ExcelWriter('{}.xlsx'.format(var))
namelist.to_excel(writer,'Sheet1')
writer.save()
print('{}.xlsx saved.'.format(var), 'Program ended.')


# In[ ]:

np.zeros(num_student)


# In[ ]:

num_student


# In[ ]:



