import os

db_user = os.environ.get('EMAIL_USER')
db_password = os.environ.get('EMAIL_PASS')

print(db_password, db_user)
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
print(EMAIL_HOST_USER)
print(EMAIL_HOST_PASSWORD)