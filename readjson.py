# readjson.py
import json

def readjson():
	with open('data.json',encoding='utf-8') as file:
		data = json.load(file)
		print(type(data))
		print(data[0])
	return data

def writejson(data):
	jsonobject = json.dumps(data,ensure_ascii=False,indent=4)
	with open('fruit.json','w',encoding='utf-8') as file:
		file.write(jsonobject)

data = {'1254531':['Orange',100,1000],
		'1254532':['Durian',150,35000],
		'1254530':['Apple',150,35000],
		'1254533':['ໝາກມ່ວງ',150,3000]}

writejson(data)