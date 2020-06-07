# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import spacy 
from spacy import displacy
from spacy.displacy import render
import pandas as pd
from io import StringIO
from tabulate import tabulate
import plotly.plotly as py
import plotly.figure_factory as ff


#input text 
text = """Fycompa 4 mg film-coated tablets
crocine 12 mg film-coated tablets 
Quadrameterer 1.3 GBq/mL solution for injection 
Topotecan123 Actavis 1mg powder for concentrate for solution 
4mg –packs of 7, 28, 84 and 98
Topotecan2344 Actavis 2mg powder for concentrate for solution
Topotecan45 Actavis 1mg powder for concentrate for solution
"""

#loading the trained model 
nlp = spacy.load("cogna")
doc = nlp(text)
options = {"ents": ["PACKAGE_ITEM_QTY","Tablet","injection"], "colors": {"PACKAGE_ITEM_QTY":"Red","Tablet":"Yellow"}}
#print(displacy.render(doc, style="dep", page=False, minify=False, jupyter=None, options=options, manual=False))
results=displacy.parse_ents(doc, options=options)
import json 
print(json.dumps(results))


#NER output data as dataframe(tabular format)
param = [[ent.text,ent.label_] for ent in doc.ents]
df=pd.DataFrame(param)
headers = ['Entity','Category']
df.columns = headers 
df_table= pd.read_table(StringIO(str(df)), sep="\s+", header=0)

print(tabulate(df_table, headers='keys', tablefmt='psql'))


#output data  visulalization in spacy 
options = {"ents": ["PACKAGE_ITEM_QTY","Tablet","injection"], "colors": {"PACKAGE_ITEM_QTY":"Red","Tablet":"Yellow"}}
displacy.serve(doc, style="ent")



