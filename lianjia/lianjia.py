#!/usr/bin/python
#coding:utf-8

from bs4 import BeautifulSoup
import requests
import MySQLdb
import chardet
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

header = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
	'Host':'cd.lianjia.com',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
}


district_dict = {"jinjiang":510104,"qingyang":510105,"jinniu":510106,"wuhou":510107,"chenghua":510108,"hitech":510109,"tianfu":510110}
#which district to search?
district = "jinjiang"
district_id = district_dict[district]


conn = MySQLdb.connect('172.26.35.122','root','tapass315','fcyj')
conn.set_character_set('utf8')

for i in range(31,63):	
	url = 'https://cd.lianjia.com/ershoufang/%s/pg%d' %(district,i)
	res = requests.get(url,headers=header)
	res.encoding='utf-8'
	html = res.text
	bs = BeautifulSoup(html,"html5lib")
	info = bs.find_all("div",class_="info clear")	
	cursor = conn.cursor()
	for h in info:
		houseid = long(h.find("div",class_="title").a.get("data-housecode"))
		cellid = long(h.find("div",class_="unitPrice").get("data-rid").encode('utf8'))
		cell_name = h.find("div",class_="houseInfo").a.string.encode('utf8')
		title = h.find("div",class_="title").a.string.encode('utf8')
		unit_price = int(h.find("div",class_="unitPrice").get("data-price").encode('utf8'))
		total_price = float(h.find("div",class_="totalPrice").span.string.encode('utf8'))
		sql = "INSERT IGNORE INTO fccx_house(houseid,cellid,district_id,cell_name,title,unit_price,total_price) \
		values ('%d','%d','%d','%s','%s','%d','%f')on duplicate key update cellid=values(cellid),district_id=values(district_id),cell_name=values(cell_name),unit_price=values(unit_price),total_price=values(total_price)" \
		%(houseid,cellid,district_id,cell_name,title,unit_price,total_price)
		cursor.execute(sql)
	time.sleep(10)
	conn.commit()
conn.close()