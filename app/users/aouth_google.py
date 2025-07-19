from authlib.integrations.starlette_client import OAuth
from starlette.config import Config

from app.config import settings

config = Config('.env')
oauth = OAuth()
oauth.register(
    name='google',
    client_id = settings.CLIENT_GOOGLE_ID,
    client_secret = settings.CLIENT_SECRET_KEY,
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile',
    },
)