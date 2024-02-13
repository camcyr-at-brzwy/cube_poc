# Install the PyJWT with pip install PyJWT
import jwt
from os import getenv
import datetime
 
# Secret key to sign the token
CUBEJS_API_SECRET = getenv('CUBEJS_API_SECRET')
 
# Create the token
token_payload = {
  'user_id': 42,
  'password': 'lolnope'
}
 
# Generate the JWT token
token = jwt.encode(token_payload, CUBEJS_API_SECRET, algorithm='HS256')