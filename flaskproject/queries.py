import sys
import logging
import rds_config
import pymysql
from flask import jsonify
import time
 

rds_host = rds_config.db_endpoint
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name
port = 3306
logger = logging.getLogger()
logger.setLevel(logging.INFO)
APIKEY = "58c66e96f312aedb78f7f726e5da74ec7ade7e33"
NAME = "Dublin"
STATIONS_URL = "https://api.jcdecaux.com/vls/v1/stations"
try:
    conn = pymysql.connect(rds_host, user=name,
    passwd=password, db=db_name, connect_timeout=10000)
    test = True
    curs = conn.cursor()
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    test = False
    sys.exit()


def availability(x):    
    while test == True:
        #x = int(input('enter stop number'))
        sql = "SELECT * From dublin_bikes_dynamic WHERE number = {0} ORDER BY last_update DESC Limit 1;".format(x)
        curs.execute(sql)
        data = []
        for row in curs.fetchall():
            row = row
        
        return jsonify(available = row)
    
    
def weekly(x):
    #returns day index, Monday = 0
    days = []
    for y in range(7):
          
        sql = """select AVG(available_bikes) from dublin_bikes_dynamic 
                WHERE number = {0} 
                AND ((from_unixtime(last_update/1000, '%w') 
                Between {1}
                and {2}))
                ORDER BY last_update DESC Limit 1;""".format(x, y, y+1)
        curs.execute(sql)
        day = int(curs.fetchall()[0][0])
        
        days.append(day)
    days.append(x)
    return jsonify(daily_average = days)
            #for column in row:
            #data.append(dict(row))
        #return jsonify(available = data)   
        
        
# Experiments with matplotlib and seperate queries. This was the initial live data analysis      
#         labels = 'Available Bikes {0}'.format(row[4]), 'Unavailable Bikes {0}'.format(row[5])
#         sizes = [row[4], row[5]]
#         colors = ['yellowgreen', 'teal']
#         plt.title('{0}, ({1}) \n Status:{2} \n {3}'.format(row[1], row[0], row[2], 3)) 
#           
#         plt.pie(sizes, labels=labels, colors=colors, autopct=None ,startangle=140)
#         patches, texts = plt.pie(sizes, colors=colors)
#         plt.legend(patches, labels, loc="best") 
#         plt.axis('equal')
#         return plt.show()

# def history(x):    
#     while test == True:
#         #x = int(input('enter stop number'))
#         now = time.time()
#         print(now)
#         sql = "SELECT * From dublin_bikes_dynamic WHERE number = {0} ORDER BY last_update DESC Limit 1;".format(x)
#         curs.execute(sql)
#         data = []
#         for row in curs.fetchall():
#             row = row
#         
#         return jsonify(available = row)
