from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from blog.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "mb-3"
        self.helper.label_class = "form-label"
        self.helper.field_class = "form-control"
        self.helper.add_input(Submit("submit", "Submit", css_class="btn btn-primary"))
