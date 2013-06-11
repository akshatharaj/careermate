STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

INSTALLED_APPS = INSTALLED_APPS + (
    'storages',
)

AWS_ACCESS_KEY_ID = 'AKIAIJDUTOXXAX2HWNBA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'maggeraj'

# Parse database configuration from $DATABASE_URL
#import dj_database_url
#DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
