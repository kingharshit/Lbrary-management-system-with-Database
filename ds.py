import sqlite3 as sq
import pandas as pd
import matplotlib.pyplot as plt
def plotit():
	conn  = sq.connect('Libbooks.db')
	df = pd.read_sql_query('select * from libbooks',conn, parse_dates=True)
	df1 = df
	df = df.loc[:,['Bkt','sPr']]
	plt.bar(df.Bkt,df.sPr, label = 'Books Graph by Price', color='r')
	plt.show()
	plt.bar(df.Bkt,df.sPr, label = 'Books Price', color='r')
	plt.title("BOOKS GRAPH BY PRICE")
	plt.xlabel("Books")
	plt.ylabel("Price")
	plt.legend()
	plt.show()
	df1.to_csv('books.csv',index=False)
