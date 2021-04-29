# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:50:50 2021

@author: rossd
"""

import psycopg2
import re
import matplotlib.pyplot as plt
import os
import pandas as pd

# connection to database:
try:
    conn = psycopg2.connect("dbname='spatial' user='postgres' host='localhost' password='0dd'")
except:
    print("cant connect to the database")

cur = conn.cursor()
cur2 = conn.cursor()
cur3 = conn.cursor()

sql = "select parid::integer from volusia.parcel p where geom is not null"

print('SQL: ', sql)
cur.execute(sql)

i=0
row = cur.fetchone()
while row is not None:
    i = i + 1
    parid = str(row[0])
    sql2 = "select p.parid::integer, p.geom, ST_Distance(p.geom, (select p2.geom from volusia.parcel p2 where p2.parid=" + parid + "))/5280  from volusia.parcel p where p.luc='2000' order by p.geom <-> (select p2.geom from volusia.parcel p2 where p2.parid=" + parid + ") limit 1;"
    cur2.execute(sql2)
    row2 = cur2.fetchone()
    parid2 = str(row2[0])
    distance = row2[2]
    sql3 = "update volusia.parcel p1 set airport_d = " + str(distance) + " where p1.parid=" + parid + ";"
    cur3.execute(sql3)
    if i%100 == 0:
        print(i)
        conn.commit()
    row = cur.fetchone()

#df = pd.
conn.commit()
conn.close()

