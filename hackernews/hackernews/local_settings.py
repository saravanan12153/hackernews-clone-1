
import os 
import sys
from os.path import join 

SITE_ID = 1

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# CRISPY_FORMS #
CRISPY_TEMPLATE_PACK = 'bootstrap3'


# PROFILE #
AUTH_PROFILE_MODULE = 'profiles.UserProfile'

ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_SIGNUP_FORM_CLASS = None

# LOGIN
LOGIN_URL = '/accounts/login/'
LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'

# comments
# COMMENTS_APP = 'threadedcomments'
FLUENT_COMMENTS_EXCLUDE_FIELDS = ('name', 'email', 'url', 'title')
COMMENTS_APP = 'fluent_comments'


INTERNAL_IPS = ('127.0.0.1',)
