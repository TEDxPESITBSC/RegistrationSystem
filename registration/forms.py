from django import forms

class RegForm(forms.Form):
	explara_barcode	= forms.CharField(label="Explara barcode",max_length=100,required=False)
	mobile_number	= forms.CharField(label="Mobile number",max_length=15,required=False)
	pesit_barcode	= forms.CharField(label="PESIT barcode",max_length=100,required=False)

class LoginForm(forms.Form):
	username 	= forms.CharField(label="Username",max_length=50,required=True)
	password	= forms.CharField(label="Password",max_length=50,required=True,widget=forms.PasswordInput)

class LunchForm(forms.Form):
	pesit_barcode	= forms.CharField(label="PESIT barcode",max_length=100,required=True)

class CSVImportForm(forms.Form):
	csv_data	= forms.CharField(label="Enter the CSV to import",max_length=40000,required=True,widget=forms.Textarea)