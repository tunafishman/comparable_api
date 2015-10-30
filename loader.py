import credentials
import sqlalchemy

rs_engine_string = "postgresql+psycopg2://%s:%s@%s:%d/%s" \
    % ( credentials.redshift_user, credentials.redshift_pass, credentials.redshift_endpoint, credentials.redshift_port, credentials.redshift_dbname )
print rs_engine_string
redshift = sqlalchemy.create_engine(rs_engine_string)
tplog = redshift.connect()

prod_engine_string = "postgresql+psycopg2://%s/%s" % ( credentials.production_endpoint, credentials.production_dbname )
print prod_engine_string
prod = sqlalchemy.create_engine(prod_engine_string)
reduced_logs = prod.connect()

print "query to RS"
tp_results = tplog.execute("SELECT * FROM tplog WHERE CID = 3521 AND DATETIME > 2015-10-29 LIMIT 5")
print "localhost query"
prod_results = reduced_logs.execute("SELECT * FROM reduced_logs")

for row in tp_results:
    print row

for row in prod_results:
    print row
