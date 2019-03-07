

#	parameters for local machine	#

# host=
# port=
# dbname=
# user=
# password=

#	parameters for aws rds	#

# host="vehcon-hawaii.cgmgdxs9awxg.us-east-2.rds.amazonaws.com"
# port=5432
# dbname="vehcon-hawaii"
# user="vehcon"
# password="vehconhawaii"

host="localhost"
port=5432
dbname="rpm_reproduction"
user="bradleysmith"
# password="postgres"

#	other parameters	#
propulsionTypes = ['Electric', 'Hybrid', 'Gasoline', 'Diesel']
# propulsionTypes = ['Electric', 'Hybrid', 'Gasoline', 'Diesel', 'Plugin Hybrid']

decode_payload = ""
decode_headers = {
		'cache-control': "no-cache",
		'Postman-Token': "1483c8ff-3ba8-4394-ba73-626f215dfe52"
		}


#	test parameters	#

test='testing'