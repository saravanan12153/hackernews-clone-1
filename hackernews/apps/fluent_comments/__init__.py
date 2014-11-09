"""
API for :ref:`custom-comment-app-api`
"""
from fluent_comments import appsettings
from fluent_comments.models import FluentComment
from fluent_comments.forms import FluentCommentForm

from posts.forms import CommentForm
# following PEP 386
__version__ = "1.0b1"


if appsettings.USE_THREADEDCOMMENTS:
    # Extend the API provided by django-threadedcomments,
    # in case this app uses more hooks of Django's custom comment app API.  
    from threadedcomments import *


def get_model():
    """
    Return the model to use for commenting.
    """
    if appsettings.USE_THREADEDCOMMENTS:
        return ThreadedComment
    else:
        # Our proxy model that performs select_related('user') for the comments
        return FluentComment


def get_form():
    """
    Return the form to use for commenting.
    """
    return CommentForm
