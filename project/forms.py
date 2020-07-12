from django import forms

class sportsman(forms.Form):
	name=forms.ChoiceField()





class recordsportsman(forms.Form):
	name= forms.ChoiceField()






class competition(forms.Form):
	name = forms.ChoiceField()
	event= forms.ChoiceField()


class forgraph(forms.Form):
	name = forms.ChoiceField()
	event= forms.ChoiceField()


class yearwiseresult(forms.Form):
	event= forms.ChoiceField()
	year=forms.IntegerField()


class graphcountry(forms.Form):
	competition= forms.ChoiceField()