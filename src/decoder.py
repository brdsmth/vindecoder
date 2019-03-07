import requests
import psycopg2
import json


# url = "https://www.decodethis.com/webservices/decodes/1B7HF13Z31J242472/xB6xzN1vUA-dXdL41EZf/1.json"

#	#	#	#	#	#

class Decoder(object):

	def __init__(self, dbconn):
		self.dbconn = dbconn
		self.payload = ""
		self.headers = {
							'cache-control': "no-cache",
							'Postman-Token': "1483c8ff-3ba8-4394-ba73-626f215dfe52"
						}

	def decode_vin(self, propulsionType):

		self.dbconn.query(
			"""SELECT * FROM vins_%s;""" % propulsionType
			)

		rows = self.dbconn.dbcursor.fetchall()
		rows = list(sum(rows, ()))

		for i in range(0, len(rows)):

			vin = rows[i]

			url = "https://www.decodethis.com/webservices/decodes/%s/xB6xzN1vUA-dXdL41EZf/1.json" % vin

			response = requests.request("GET", url, data=self.payload, headers=self.headers)

			resjsonobj = response.json()

			self.sort_decode_vin(resjsonobj, propulsionType)

			self.dbconn.commit()

			print(i)

	def sort_decode_vin(self, resjsonobj, propulsionType):

		self.dbconn.query(
			"""CREATE TABLE IF NOT EXISTS decode_response_%s (
				vin VARCHAR, 
				status VARCHAR,
				make VARCHAR,
				model VARCHAR,
				year VARCHAR
				);""" % propulsionType
			)

		status = resjsonobj['decode']['status']


		if status == 'SUCCESS':

			vin = resjsonobj['decode']['VIN']
			make = resjsonobj['decode']['vehicle'][0]['make']
			model = resjsonobj['decode']['vehicle'][0]['model']
			year = resjsonobj['decode']['vehicle'][0]['year']

			self.dbconn.query(
				"""INSERT INTO decode_response_%s (
						vin, 
						status,
						make, 
						model,
						year) VALUES (
							'%s',
							'%s',
							'%s',
							'%s',
							'%s')
						""" % (propulsionType, vin, status, make, model, year))
		else:

			vin = resjsonobj['decode']['VIN']

			self.dbconn.query(
				"""INSERT INTO decode_response_%s (
						vin, 
						status,
						make, 
						model,
						year) VALUES (
							'%s',
							'%s',
							'-',
							'-',
							'-')
						""" % (propulsionType, vin, status))






