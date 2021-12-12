# database.py
import sqlite3

conn = sqlite3.connect('product-database.sqlite3')
c = conn.cursor()

# create table
c.execute("""CREATE TABLE IF NOT EXISTS transaction_history (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				tid TEXT,
				stamp TEXT,
				product TEXT,
				price REAL,
				quan REAL,
				total REAL)""")

print('Success')

def insert_transaction(data):
	# data = {'tid':'132346611','stamp':'2021-12-12 11:39:59'...}
	ID = None
	tid = data['tid']
	stamp = data['stamp']
	product = data['product']
	price = data['price']
	quan = data['quan']
	total = data['total']

	with conn:
		command = 'INSERT INTO transaction_history VALUES (?,?,?,?,?,?,?)'
		c.execute(command,(ID,tid,stamp,product,price,quan,total))
		conn.commit()
	print('inserted!')

def view_transaction():
	with conn:
		c.execute("SELECT * FROM transaction_history")
		data = c.fetchall()
		print(data)

transaction = {'tid':'132346611',
				'stamp':'2021-12-12 11:39:59',
				'product':'books',
				'price':155000,
				'quan':10,
				'total':1550000}

# insert_transaction(transaction)
view_transaction()