import sqlite3
import pandas as pd

conn = sqlite3.connect('books.db')
c = conn.cursor()
tiles = pd.read_csv('Titles.csv')
tiles.to_sql('titles', conn, if_exists='append', index = False, chunksize = 1000)