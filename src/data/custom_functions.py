#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_file_name(file_name):
    name_ext = file_name.split("\\")[-1]
    name = name_ext.split(".")[0]
    
    return name

