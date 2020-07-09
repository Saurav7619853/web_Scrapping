#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import selenium
import warnings
import time
warnings.filterwarnings('ignore')
from selenium import webdriver as wb
webD = wb.Chrome(r'C:\Users\saurav\Desktop\chromedriver.exe')
webD.get('https://www.marksandspencer.com/printed-yoke-midi-waisted-dress/p/clp60443957?color=BLUEMIX')


#Reading selectors from text file
import pandas as pd
with open(r"C:\Users\saurav\Desktop\text files\M&S.txt",'r') as f:
    content = f.readlines()
content = [x.strip() for x in content]


import re
all_selectors=[]
for i in range(len(content)):
    a=[]
    sentences=re.split(r',',content[i])
    for stuff in sentences:
        a.append(stuff)
    all_selectors.append(a)
all_selectors



for i in range(len(all_selectors)):
    for j in range(len(all_selectors[i])):
        index = all_selectors[i][j].find(':')
        if(index!=-1):
            all_selectors[i][j]=(all_selectors[i][j][0:index],all_selectors[i][j][index+1:])

all_selectors





#VARIABLES
selectors={'information_container_class':all_selectors[0],
          'product_information_class':all_selectors[1],
          'product_name_class':all_selectors[2],
          'product_price_container_class':all_selectors[3],
          'product_description_class':all_selectors[4],
          'delivery_info_class':all_selectors[5],
          'rating':all_selectors[6]}





#whole info container¶
if(len(selectors['information_container_class'])==2):
    try:
        information=webD.find_element_by_class_name(selectors['information_container_class'][0])
        information_footer=webD.find_element_by_class_name(selectors['information_container_class'][1])
    except:
        information=webD.find_element_by_id(selectors['information_container_class'][0])
        information_footer=webD.find_element_by_id(selectors['information_container_class'][1])
else:
    try:
        information=webD.find_element_by_class_name(selectors['information_container_class'][0])
    except:
        try:
            information=webD.find_element_by_id(selectors['information_container_class'][0])
        except:
            try:
                information=webD.find_element_by_tag_name(selectors['information_container_class'][0])
            except:
                pass
            
            
            

            
            
            
#Name
try:
    name=information.find_element_by_class_name(selectors['product_name_class'][0]).text
    
except:
    pass

try:
    name=information.find_element_by_tag_name(selectors['product_name_class'][0]).text
except:
    pass
name






#Price
price=information.find_element_by_class_name(selectors['product_price_container_class'][0]).text
price






#Description
description=[]
for i in range(len(selectors['product_description_class'])):
    if(type(selectors['product_description_class'][i])==tuple):
        try:
            information.find_element_by_class_name(selectors['product_description_class'][i][0]).click()
            time.sleep(3)
        except:
            try:
                information.find_element_by_id(selectors['product_description_class'][i][0]).click()
                time.sleep(3)
            except:
                try:
                    information.find_element_by_xpath(selectors['product_description_class'][i][0]).click()
                    time.sleep(3)
                except:
                    pass
        try:
            des=information.find_element_by_class_name(selectors['product_description_class'][i][1]).text
            print(5)
        except:
            try:
                des=information.find_element_by_id(selectors['product_description_class'][i][1]).text
                print(6)
            except:
                try:
                    des=information.find_element_by_tag_name(selectors['product_description_class'][i][1]).text
                    print(7)
                except:
                    pass
       
    elif(type(selectors['product_description_class'][i])==str):
        try:
            information.find_element_by_class_name(selectors['product_description_class'][i]).click()
            time.sleep(2)
        except:
            try:
                information.find_element_by_id(selectors['product_description_class'][i]).click()
                time.sleep(2)
            except:
                pass
        
        try:
            des=information.find_element_by_class_name(selectors['product_description_class'][i]).text
            print(3)
        except:
            des=information.find_element_by_id(selectors['product_description_class'][i]).text
            print(4)
        
    try:        
        des=re.split(r'\n',des)
        st=[]
        for string in des:
            if(string!=''):
                st.append(string)
        description.append(st)
    except:
        pass
description







#Delivery and Returns
delivery_returns=[]
if(len(selectors['delivery_info_class'])==1):
    try:
        information.find_element_by_xpath(selectors['delivery_info_class'][0][0]).click()
        time.sleep(2)
        print(1)
    except:
        try:
            information.find_element_by_class_name(selectors['delivery_info_class'][0][0]).click()
            time.sleep(2)
            print(2)
        except:
            try:
                information_footer.find_element_by_xpath(selectors['delivery_info_class'][0][0]).click()
                time.sleep(2)
                print(3)
            except:
                try:
                    information_footer.find_element_by_class_name(selectors['delivery_info_class'][0][0]).click()
                    time.sleep(2)
                    print(4)
                except:
                    pass
                
    try:
        del_ret=webD.find_element_by_id(selectors['delivery_info_class'][0][1]).text
        print(5)
    except:
        try:
            del_ret=webD.find_element_by_class_name(selectors['delivery_info_class'][0][1]).text
            print(6)
        except:
            try:
                del_ret=webD.find_element_by_tag_name(selectors['delivery_info_class'][0][1]).text
                print(7)
            except:
                try:
                    del_ret=webD.find_element_by_xpath(selectors['delivery_info_class'][0][1]).text
                    print(7)
                except:
                    pass
    des=re.split(r'\n',del_ret)
    st=[]
    for string in des:
        if(string!=''):
            st.append(string)
    delivery_returns.append(st)
    
    
if(len(selectors['delivery_info_class'])==3):
    try:
        information.find_element_by_xpath(selectors['delivery_info_class'][0]).click()
    except: 
        try:
            information_footer.find_element_by_xpath(selectors['delivery_info_class'][0]).click()
        except:
            try:
                webD.get(information.find_element_by_xpath(selectors['delivery_info_class'][0]).get_property('href'))
            except:
                pass
    
    for i in range(2):
        if(type(selectors['delivery_info_class'][i+1])==tuple):
            try:
                webD.find_element_by_class_name(selectors['delivery_info_class'][i+1][0]).click()
                time.sleep(2)
            except:
                try:
                    webD.find_element_by_id(selectors['delivery_info_class'][i+1][0]).click()
                    time.sleep(2)
                except:
                    try:
                        webD.find_element_by_xpath(selectors['delivery_info_class'][i+1][0]).click()
                        time.sleep(2)
                    except:
                        pass
            try:
                del_ret=webD.find_element_by_class_name(selectors['delivery_info_class'][i+1][1]).text
            except:
                try:
                    del_ret=webD.find_element_by_id(selectors['delivery_info_class'][i+1][1]).text
                except:
                    try:
                        del_ret=webD.find_element_by_tag_name(selectors['delivery_info_class'][i+1][1]).text
                    except:
                        pass
                    
                    
            des=re.split(r'\n',del_ret)
            st=[]
            for string in des:
                if(string!=''):
                    st.append(string)
            delivery_returns.append(st)
            
        else:
            try:
                del_ret=webD.find_element_by_class_name(selectors['delivery_info_class'][i+1]).text
            except:
                try:
                    del_ret=webD.find_element_by_id(selectors['delivery_info_class'][i+1]).text
                except:
                    try:
                        del_ret=webD.find_element_by_tag_name(selectors['delivery_info_class'][i+1]).text
                    except:
                        pass
                    
                    
            des=re.split(r'\n',del_ret)
            st=[]
            for string in des:
                if(string!=''):
                    st.append(string)
            delivery_returns.append(st)
            
            
            
if(len(selectors['delivery_info_class'])==2):
    try:
        print('clickable')
        for i in range(2):
            print('yes')
            try:
                print('did')
                information.find_element_by_class_name(selectors['delivery_info_class'][i][0]).click()
                time.sleep(2)
                print('11')
            except:
                try:
                    information.find_element_by_id(selectors['delivery_info_class'][i][0]).click()
                    time.sleep(2)
                    print('22')
                except:
                    try:
                        information.find_element_by_xpath(selectors['delivery_info_class'][i][0]).click()
                        time.sleep(2)
                        print('33')
                    except:
                        webD.find_element_by_xpath(selectors['delivery_info_class'][i][0]).click()
                        time.sleep(3)
                        print('fuck')
                        
            try:
                del_ret=information.find_element_by_class_name(selectors['delivery_info_class'][i][1]).text
                print('1a')
            except:
                try:
                    del_ret=information.find_element_by_tag_name(selectors['delivery_info_class'][i][1]).text
                    print('1b')
                except:
                    try:
                        del_ret=information.find_element_by_id(selectors['delivery_info_class'][i][1]).text
                        print('1c')
                    except:
                        pass
                
            des=re.split(r'\n',del_ret)
            st=[]
            for string in des:
                if(string!=''):
                    st.append(string)
            delivery_returns.append(st)
            
    except:
        try:
            D_R=[]
            D_R.append(information.find_element_by_xpath(selectors['delivery_info_class'][0][0]).get_property('href'))
            D_R.append(information.find_element_by_xpath(selectors['delivery_info_class'][1][0]).get_property('href'))
            print('href link')
            for i in range(len(D_R)):
                webD.get(D_R[i])
                time.sleep(5)
                try:
                    del_ret=webD.find_element_by_class_name(selectors['delivery_info_class'][i][1]).text
                except:
                    try:
                        del_ret=webD.find_element_by_id(selectors['delivery_info_class'][i][1]).text
                    except:
                        try:
                            del_ret=webD.find_element_by_tag_name(selectors['delivery_info_class'][i][1]).text
                        except:
                            pass
                des=re.split(r'\n',del_ret)
                st=[]
                for string in des:
                    if(string!=''):
                        st.append(string)
                delivery_returns.append(st)

                            
        except:
            try:
                for i in range(2):
                    try:
                        del_ret=information.find_element_by_class_name(selectors['delivery_info_class'][i]).text
                        print('2a')
                    except:
                        try:
                            del_ret=information.find_element_by_tag_name(selectors['delivery_info_class'][i]).text
                            print('2b')
                        except:
                            try:
                                del_ret=information.find_element_by_id(selectors['delivery_info_class'][i]).text
                                print('2c')
                            except:
                                pass

                    des=re.split(r'\n',del_ret)
                    st=[]
                    for string in des:
                        if(string!=''):
                            st.append(string)
                    delivery_returns.append(st)
            except:
                pass

            
delivery_returns





#Rating
rating='no rating'
try:
    rating=information.find_element_by_class_name(selectors['rating']).text
except:
    try:
        rating=information.find_element_by_id(selectors['rating']).text
    except:
        try:
            rating=information.find_element_by_tag_name(selectors['rating']).text
        except:
            pass
rating




data={'name':name,'price':price,'description':description,'deliver and returns':delivery_returns}

