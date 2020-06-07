# -*- coding: utf-8 -*-
"""
Created on Wed May  1 23:14:28 2019

@author: ssahu
"""

import spacy
import pandas as pd
from io import StringIO
from tabulate import tabulate
import plotly.plotly as py
import plotly.figure_factory as ff

text = """Fycompa 4 mg film-coated tablets
crocine 12 mg film-coated tablets 
Quadrameterer 1.3 GBq/mL solution for injection 
Topotecan123 Actavis 1mg powder for concentrate for solution 
4mg –packs of 7, 28, 84 and 98
Topotecan2344 Actavis 2mg powder for concentrate for solution
Topotecan45 Actavis 1mg powder for concentrate for solution


 """
    
nlp = spacy.load("cogna")
doc = nlp(text)

param = [[ent.text,ent.label_] for ent in doc.ents]
df=pd.DataFrame(param)
headers = ['Entity','Category']
df.columns = headers 




df_table= pd.read_table(StringIO(str(df)), sep="\s+", header=0)

print(tabulate(df_table, headers='keys', tablefmt='psql'))