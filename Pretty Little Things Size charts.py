#!/usr/bin/env python
# coding: utf-8

# In[5]:


import time
import selenium
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from selenium import webdriver as wb
webD = wb.Chrome(r'C:\Users\saurav\Desktop\chromedriver.exe')
webD.get('https://www.prettylittlething.com/pink-low-rise-sweat-mini-skirt.html')
webD.find_element_by_class_name('size-guide-container').click()
time.sleep(5)

diff_types=webD.find_element_by_class_name('size-content-details.tables.accordion-wrapper').find_elements_by_class_name('accordion')
size_charts=[]
size_charts_name={}
size_charts_name_arr=[]
for k in range(len(diff_types)-1):
    diff_types[k].click()
    time.sleep(2)
    print('click for type '+str(k))
    tables=diff_types[k].find_element_by_class_name('active').find_elements_by_tag_name('table')
    tables_name=[]
    A=[]
    for j in range(len(tables)):
        a=[]
        b=[]
        c=[]
        d=[]
        tables_name.append(diff_types[k].find_element_by_class_name('size-table').find_elements_by_class_name('tbltext')[j].text)
        tr_tags=tables[j].find_elements_by_tag_name('tr')
        if(len(tables[j].find_element_by_class_name('page').find_elements_by_xpath("tr[@class='tblheading']"))==2):
            for i in range(len(tr_tags)-2):
                a.append(tr_tags[i+2].find_elements_by_xpath("td[@class='tblrow' or @class='tblrow tblinch']")[len(tr_tags[i+2].find_elements_by_xpath("td[@class='tblrow' or @class='tblrow tblinch']"))-4].text)
                b.append(tr_tags[i+2].find_elements_by_xpath("td[@class='tblrow' or @class='tblrow tblinch']")[len(tr_tags[i+2].find_elements_by_xpath("td[@class='tblrow' or @class='tblrow tblinch']"))-3].text)
                c.append(tr_tags[i+2].find_elements_by_xpath("td[@class='tblrow' or @class='tblrow tblinch']")[len(tr_tags[i+2].find_elements_by_xpath("td[@class='tblrow' or @class='tblrow tblinch']"))-2].text)
                d.append(tr_tags[i+2].find_elements_by_xpath("td[@class='tblrow' or @class='tblrow tblinch']")[len(tr_tags[i+2].find_elements_by_xpath("td[@class='tblrow' or @class='tblrow tblinch']"))-1].text)

            size={tr_tags[0].find_elements_by_xpath("td[@class='tblheading']")[len(tr_tags[0].find_elements_by_xpath("td[@class='tblheading']"))-4].text:a,
                tr_tags[0].find_elements_by_xpath("td[@class='tblheading']")[len(tr_tags[0].find_elements_by_xpath("td[@class='tblheading']"))-3].text:b,
                tr_tags[0].find_elements_by_xpath("td[@class='tblheading']")[len(tr_tags[0].find_elements_by_xpath("td[@class='tblheading']"))-2].text:c,
                tr_tags[0].find_elements_by_xpath("td[@class='tblheading']")[len(tr_tags[0].find_elements_by_xpath("td[@class='tblheading']"))-1].text:d}

        else:
            for i in range(len(tr_tags)-1):
                a.append(tr_tags[i+1].find_elements_by_xpath("td[@class='tblrow' or @class='tblrow tblgrey']")[len(tr_tags[i+1].find_elements_by_xpath("td[@class='tblrow' or @class='tblrow tblgrey']"))-4].text)
                b.append(tr_tags[i+1].find_elements_by_xpath("td[@class='tblrow' or @class='tblrow tblgrey']")[len(tr_tags[i+1].find_elements_by_xpath("td[@class='tblrow' or @class='tblrow tblgrey']"))-3].text)
                c.append(tr_tags[i+1].find_elements_by_xpath("td[@class='tblrow' or @class='tblrow tblgrey']")[len(tr_tags[i+1].find_elements_by_xpath("td[@class='tblrow' or @class='tblrow tblgrey']"))-2].text)
                d.append(tr_tags[i+1].find_elements_by_xpath("td[@class='tblrow' or @class='tblrow tblgrey']")[len(tr_tags[i+1].find_elements_by_xpath("td[@class='tblrow' or @class='tblrow tblgrey']"))-1].text)

            size={tr_tags[0].find_elements_by_xpath("td[@class='tblheading dbltbl']")[len(tr_tags[0].find_elements_by_xpath("td[@class='tblheading dbltbl']"))-4].text:a,
                tr_tags[0].find_elements_by_xpath("td[@class='tblheading dbltbl']")[len(tr_tags[0].find_elements_by_xpath("td[@class='tblheading dbltbl']"))-3].text:b,
                tr_tags[0].find_elements_by_xpath("td[@class='tblheading dbltbl']")[len(tr_tags[0].find_elements_by_xpath("td[@class='tblheading dbltbl']"))-2].text:c,
                tr_tags[0].find_elements_by_xpath("td[@class='tblheading dbltbl']")[len(tr_tags[0].find_elements_by_xpath("td[@class='tblheading dbltbl']"))-1].text:d}

        A.append(size)
    size_charts.append(A)
    size_charts_name.update({diff_types[k].find_element_by_class_name('accordion-title').text:tables_name})
    size_charts_name_arr.append(tables_name)
    

print('\n')
print('\n')    
print(size_charts_name) 
print('\n')
print('\n')
for i in range(len(diff_types)-1):
    for j in range(len(size_charts_name_arr[i])):
        print(size_charts_name_arr[i][j])
        print('\n')
        print(pd.DataFrame(size_charts[i][j]).set_index(pd.DataFrame(size_charts[i][j]).columns[0]))
        print('\n')
    print('\n')
    print('\n')


# In[ ]:




