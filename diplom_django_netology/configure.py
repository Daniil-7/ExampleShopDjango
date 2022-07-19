# diplom_django_netology/configure.py
# cloudinary
cloudinary_cloud_name = "cloud name"
cloudinary_api_key = "api key"
cloudinary_api_secret = "api secret"

# mail используется gmail
# внимание данный проект рассчитан на gmail если вы используете другую почту тогда исправти в коде TLS на SSL
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "mail"
EMAIL_HOST_PASSWORD = "password app"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = "mail"
SERVER_EMAIL = "mail"


# fondy(cloudipsp)
cloudipsp_merchant_id = 1396424
cloudipsp_secret_key="test"