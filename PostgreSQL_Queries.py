import pandas as pd
import psycopg2

try:
    conn = psycopg2.connect("dbname='amrstaging' user= 'thiamhuat' host='52.77.188.178' password= 'thiamhuat1234##'")
except:
    print("I am unable to connect to the database")

meter= "SELECT * from meter"
service_point= "SELECT * from service_point"
leak_alarm= "SELECT * from leak_alarm"

meter_DF = pd.read_sql_query(meter,conn)
servicepoint_DF = pd.read_sql_query(service_point,conn)
leakalarm_DF = pd.read_sql_query(leak_alarm,conn)

servicepoint_DF[servicepoint_DF.site=='Tuas']
Yuhua_Open = leakalarm_DF[(leakalarm_DF.site=='Yuhua') & (leakalarm_DF.status=='Open')]
Punggol_Open = leakalarm_DF[(leakalarm_DF.site=='Punggol') & (leakalarm_DF.status=='Open')]

models_manufacturer = pd.DataFrame.drop_duplicates(meter_DF[['manufacturer','model']])

print(models_manufacturer)

