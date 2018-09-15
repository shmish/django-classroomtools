from django import forms
from django.forms import ModelForm
from .models import Classroom
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm

class VSBSignupForm(SignupForm):

    def save(self, request):

        # Ensure you call the parent classes save.
        # .save() returns a User object.
        user = super(VSBSignupForm, self).save(request)
        user.email_address = user.username + "@vsb.bc.ca"
        user.save()
        print("hello")

        # You must return the original result.
        return user

class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ['course_name', 'grade', 'course_block','class_list']
        
    def __init__(self, *args, **kwargs):
        super(ClassroomForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            
    def validate_unique(self):
        try:
            self.instance.validate_unique(exclude=None)
        except ValidationError as e:
            self._update_errors(e)
          
##    def clean_course_block(self):
##        course_block = self.cleaned_data['course_block']
##        if Classroom.objects.filter(course_block=course_block).exclude(pk=self.instance.pk).exists():
##            raise ValidationError('This course block is already used.')
##        return course_block

class DeleteForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ['course_block']
        

    
