import config
import psycopg2
import action
import decoder 


# conn = psycopg2.connect(host=config.host, dbname=config.dbname, user=bradleysmith)					
#	returns a connection object
#	connection object creates session w/ database server 
#	'instantiates a persistent client'




myDB = action.myDB()

# myDB.query(
# 	"""CREATE TABLE IF NOT EXISTS testingtesting
# 	AS 
# 	SELECT * FROM am_vehicle;""")

for type in config.propulsionTypes: 
	myDB.query(
		"""CREATE TABLE IF NOT EXISTS vins_%s
				AS 
				SELECT DISTINCT vin FROM am_vehicle
				WHERE propulsion_type = '%s';""" % (type, type)
		)

	myDB.commit()


decode = decoder.Decoder(myDB)
decode.decode_vin('Electric')


#	resources:
#		https://www.dataquest.io/blog/loading-data-into-postgres/





















