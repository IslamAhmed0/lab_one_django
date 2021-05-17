from django import forms
from courses.models import Student




class StudentForm(forms.Form):
    fname=forms.CharField(label="fname")
    lname=forms.CharField(label="lname")
    age=forms.IntegerField(label="age")
    email=forms.EmailField(label="track")








class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields=('fname','lname','age','email','student_track')
        #fields='__all__
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.NumberInput(attrs={'size': 10, 'title': 'Search'}),

            'student_track': forms.Select(attrs={'class': 'form-control'}),
        }


#
# class TrackForm(forms.ModelForm):
#     class Meta:
#         model = Track
#         fields=('name')
#         #fields='__all__