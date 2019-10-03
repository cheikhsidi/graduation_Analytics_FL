# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 13:52:44 2019

@author: cheikh_Moctar
"""

import requests
import pandas as pd
import json
from bs4 import BeautifulSoup

#getting the data from the URL
source = requests.get('https://www.collegetuitioncompare.com/compare/tables/?state=FL&factor=tuition')
colleges = []
data = {}
lst = []
#load data into bs4
soup = BeautifulSoup(source.content, 'html5lib')
#print(soup)
table = soup.find('tbody')
t = table.findAll('th')
#print(t[3].text)
for i in range(1,len(t),2):
    colleges.append(t[i].text)
td = table.findAll('td')
#print(td[-1])
try:
    for x in range(0,len(td),5):
    #for college in colleges:
        lst.append([td[n].text for n in range(x,x+5)])
except:
    print ("not compatobel")
 #data.setdefault(college, []).append(lst)

        #data= {college:[lst]}
#headers =["Applicants":Applicants, "dmitted":Admitted, "Enrolled":Enrolled, "Acceptance":Acceptance, "Admission":Admission]
Applicants = [item[0] for item in lst]
Admitted = [item[1] for item in lst]
Enrolled = [item[2] for item in lst]
Acceptance = [item[3] for item in lst]
Admission = [item[4] for item in lst]
df = pd.DataFrame({"Colleges":colleges,"RequiredToApply":Applicants, "SAT_25%":Admitted, "SAT_75%":Enrolled, "ACT_25%":Acceptance, "ACT_75%":Admission})
df.to_csv("2019_tuition.csv")