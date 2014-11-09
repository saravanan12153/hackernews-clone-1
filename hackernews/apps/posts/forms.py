from django.forms import ModelForm

from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Submit, Div
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions

from .models import Post
#from threadedcomments.forms import ThreadedCommentForm
#from threadedcomments.models import ThreadedComment
from fluent_comments.forms import FluentCommentForm 
class PostForm(ModelForm):  

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-xs-2'
    helper.field_class = 'col-xs-8'
    helper.add_input(Submit('submit', 'submit'))
    
    class Meta:
	model = Post
	fields=  ('title', 'url',)

	
class CommentForm(FluentCommentForm):  

    helper = FormHelper()
    #helper.form_class = 'form-horizontal col-xs-6 col-sm-offset-3'
    helper.form_show_labels = False
    #helper.label_class = 'col-xs-2'
    #helper.field_class = 'col-xs-6'
    helper.add_input(Submit('submit', 'submit'))
    



