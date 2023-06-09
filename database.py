import pathlib
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine import connection

import config

BASE_DIR = pathlib.Path(__file__).resolve().parent  

SOURCE_DIR = BASE_DIR / 'connect-bundle'

settings = config.get_settings() 

ASTRADB_CONNECT_BUNDLE = BASE_DIR / SOURCE_DIR / "secure-connect-blog-db.zip" 
ASTRADB_CLIENT_ID = settings.db_client_id
ASTRADB_CLIENT_SECRET = settings.db_client_secret

def get_session():
    cloud_config= {
            'secure_connect_bundle': ASTRADB_CONNECT_BUNDLE
    }
    auth_provider = PlainTextAuthProvider(ASTRADB_CLIENT_ID, ASTRADB_CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    connection.register_connection(str(session), session=session)
    connection.set_default_connection(str(session))
    return session