# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:50:20 2019

@author: Roger
"""

import sqlite3
import json
import os
from datetime import datetime

timeframe = '2015-05'
sql_transaction = []

connection = sqlite3.connect('{}2.db'.format(timeframe))
c = connection.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS parent_reply(parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, parent TEXT, comment TEXT, subreddit TEXT, unix INT, score INT)")

def format_data(data):
    data = data.replace('\n',' newlinechar ').replace('\r',' newlinechar ').replace('"',"'")
    return data           

def find_parent(pid):
    try:
        sql = "SELECT comment FROM parent_reply WHERE comment_id = '{}' LIMIT 1".format(pid)
        c.execute(sql)
        result = c.fetchone()
        if result != None:
            return result[0]
        else: return False
    except Exception as e:
        #print(str(e))
        return False

if __name__ == '__main__':
    create_table()
    
if __name__ == '__main__':
    create_table()
    row_counter = 0
    paired_rows = 0
    file_name = os.path.join(os.path.dirname(__file__), 'movie_lines.txt')
    

    with open(file_name, buffering=1000) as f:
        for row in f:    
            row_counter += 1
            row = json.loads(row)
            parent_id = row['parent_id']
            body = format_data(row['body'])
            created_utc = row['created_utc']
            score = row['score']
            comment_id = row['name']
            subreddit = row['subreddit']
            parent_data = find_parent(parent_id)
            
