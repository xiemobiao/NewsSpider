# -*- coding: utf-8 -*- 
#!/usr/bin/python
import json
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

file = open('title.json')
conn = sqlite3.connect('news.db')
while 1:
	line = file.readline()
	if not line:
		break
	data = json.loads(line)
	insertsql = "insert into news(title,time,url) values ('"+str(data['title']).decode('utf-8')+"','"+str(data['time']).decode('utf-8')+"','"+str(data['url']).decode('utf-8')+"')"
	print insertsql
	conn.execute(insertsql)
	conn.commit()

conn.close()