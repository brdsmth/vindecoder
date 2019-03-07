import psycopg2
import config



class myDB(object):

	def __init__(self):
		self.dbconn = psycopg2.connect(host=config.host, dbname=config.dbname, user=config.user)
		self.dbcursor = self.dbconn.cursor()

	def query(self, query):
		return self.dbcursor.execute(query)

	def commit(self):
		self.dbconn.commit()

	def __del__(self):
		self.dbconn.close() 



