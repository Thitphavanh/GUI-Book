# writefile.py
from datetime import datetime

def writetext(quantity,total):
	stamp = datetime.now()
	stamp = stamp.replace(year=stamp.year+543) # ບວກເປັນ ພສ
	stamp = stamp.strftime('%Y-%m-%d, %H:%M:%S')
	filename = 'data.txt'
	with

