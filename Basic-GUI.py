# Basic-GUI.py
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import csv

# ----------------------------
def timestamp(lao=True):
	if lao == True:
		stamp = datetime.now()
		stamp = stamp.replace(year=stamp.year+543) # ບວກເປັນ ພສ
		stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	else:
		stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	return stamp

def writetext(quantity,total):
	# stamp = datetime.now()
	# stamp = stamp.replace(year=stamp.year+543) # ບວກເປັນ ພສ
	# stamp = stamp.strftime('%Y-%m-%d, %H:%M:%S')
	stamp = timestamp()
	filename = 'data.txt'
	with open(filename,'a',encoding='utf-8') as file:
		file.write('\n'+ 'ວັນ-ເວລາ: {}, ໜັງສື: {} ຫົວ, ລວມຍອດທັງໝົດ: {:,.0f} ກີບ'.format(stamp,quantity,total))

def writecsv(data):
	# data = ['Time',12,55000]
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) # fw = file write
		fw.writerow(data)
	print('Success')

def readcsv():
	with open('data.csv',newline='',encoding='utf-8') as file:
		fr = csv.reader(file)
		# print(list(fr))
		data = list(fr)
	return data

def sumdata():
	# ຟັງຊັ່ນນິ້ໃຊ້ສຳຫຼັບລວມຄ່າທີ່ໄດ້ຈາກ csv ໄຟລ໌ສະຫຼຸບອອກມາເປັນ 2 ຢ່າງ
	result =  readcsv()
	sumlist_quan = []
	sumlist_total = []
	for d in result:
		sumlist_quan.append(float(d[1]))
		sumlist_total.append(float(d[2]))
	sumquan = sum(sumlist_quan)
	sumtotal = sum(sumlist_total)

	return(sumquan,sumtotal)


# ----------------------------

GUI = Tk()
GUI.geometry('500x500')
GUI.title('Program By Hery')

file = PhotoImage(file='books.png')
IMG = Label(GUI,image=file,text='')
IMG.pack()

L1 = Label(GUI,text='ໂປຣແກຣມຄຳນວນຂາຍໜັງສື',font=(None,15,'bold'),fg='grey')
L1.pack() # .place(x,y), .grid(row=0,column=0)

L2 = Label(GUI,text='ກະລຸນາໃສ່ຈຳນວນໜັງສື',font=(None,10),fg='grey')
L2.pack() # .place(x,y), .grid(row=0,column=0)

v_quantity = StringVar() # ຕຳແໜ່ງໂຕແປທີີ່ໃສ່ເກັບຂໍ້ມູນຂອງຊ່ອງຂໍ້ມູນ

E1 = Entry(GUI,textvariable=v_quantity,font=('impact',20))
E1.pack()

def Calculate(event=None):
	quantity = v_quantity.get()
	price = 100000
	print('ຈຳນວນ',float(quantity)*price) 
	cal = float(quantity) * price
	# EN Date
	# stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	# # TH Date
	# stamp = datetime.now()
	# stamp = stamp.replace(year=stamp.year+543) # ບວກເປັນ ພສ
	# stamp = stamp.strftime('%Y-%m-%d, %H:%M:%S')

	# writetext(quantity,cal)
	data = [timestamp(), quantity,cal]
	writecsv(data)

	# pop up
	sm = sumdata()
	title = 'ຍອດທີ່ລູກຄ້າຕ້ອງຈ່າຍ'
	text = 'ໜັງສືຈຳນວນ {} ຫົວ\nລາຄາທັງໝົດ : {:,.0f} ກີບ'.format(quantity,cal)
	messagebox.showinfo(title,text)

	v_quantity.set('') # Clear data
	E1.focus()

B1 = ttk.Button(GUI,text='ຄຳນວນ',command=Calculate)
B1.pack(ipadx=20,ipady=15,pady=15)

E1.bind('<Return>', Calculate)

def SummaryData(event):
	# pop up
	sm = sumdata()
	title = 'ຍອດສະຫຼຸບລວມທັງໝົດ'
	text = 'ຈຳນວນທີ່ຂາຍໄດ້ : {} ຫົວ\nຍອດຂາຍທີ່ຂາຍໄດ້ : {:,.0f} ກີບ'.format(sm[0],sm[1])
	messagebox.showinfo(title,text)

GUI.bind('<F1>',SummaryData)

E1.focus() # ໃຫ້ cursor ໄປຫາຕຳແໜ່ງຂອງ E1
GUI.mainloop()