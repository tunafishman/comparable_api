from credentials import *
from sqlalchemy import create_engine

engine_string = "postgresql+psycopg2://%s:%s@%s:%d/%s" % (credentials.redshift_user, credentials.redshift_pass, credentials.redshift_endpoint, credentials.port, credentials.dbname)

engine = create_engine(engine_string)

df = 

