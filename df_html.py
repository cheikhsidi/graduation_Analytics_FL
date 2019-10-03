# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 20:09:34 2019

@author: cheikh_Moctar
"""

import pandas as pd
import lxml

df_tuition = pd.read_html("https://www.collegetuitioncompare.com/compare/tables/?state=FL&factor=tuition")
df_tuition[0]