#Generate random secure token of 64 bytes and random URL
import secrets

#Get the token by using the token_hex() method of secrets
token = secrets.token_hex(64)
print(token)

#Get the random safe url by using the token_urlsafe() method of secrets
random_url = secrets.token_urlsafe(32)
print(random_url)