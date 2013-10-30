from django import forms

class AddForm(forms.Form):
	Gender = ((u'M', u'Male'), (u'F', u'Female'))
	name = forms.CharField(max_length = 20, required = True)
	sex = forms.ChoiceField(choices = Gender, label = u'Gender', required = True)
	number = forms.CharField(max_length = 8, required = False)
	popo = forms.EmailField(required = False)
	phone = forms.CharField(max_length = 15, required = False)
