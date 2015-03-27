from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegForm, LunchForm, CSVImportForm
from .models import Attendee

def login_user(request):
	context = {}
	if request.method == 'GET':
		if request.user.is_authenticated():
			return redirect('register')
			
		form = LoginForm()
		context['form'] = form

		return render(request,'login.html',context)

	elif request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			data = form.cleaned_data

			username = data['username']
			password = data['password']

			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)

					return redirect('register')

				else:
					context['form']			= LoginForm()
					context['message']		= "Account disabled."
					context['messageclass']	= "error"

					return render(request,'login.html',context)
			else:
				context['form']			= LoginForm()
				context['message']		= "Invalid username or password."
				context['messageclass']	= "error"

				return render(request,'login.html',context)


@login_required(login_url='/')
def register(request):
	context = {}

	if request.method == "GET":

		form = RegForm()
		context['form']			= form
		context['form_type']	= 1

		return render(request,'register.html',context)

	elif request.method == "POST":

		form = RegForm(request.POST)

		if form.is_valid():
			data = form.cleaned_data

			explara_barcode = str(data['explara_barcode'])
			mobile_number	= data['mobile_number']
			pesit_barcode	= str(data['pesit_barcode'])

			if not pesit_barcode:

				if explara_barcode:
					try:
						att = Attendee.objects.get(explara_barcode=explara_barcode)
					except:
						context['message']		= "No record found with those details."
						context['messageclass'] = "error"
						context['form']			= RegForm()

						return render(request,'register.html',context)

				elif mobile_number:
					try:
						att = Attendee.objects.get(mobile_number=mobile_number)
					except:
						context['message']		= "No record found with those details."
						context['messageclass'] = "error"
						context['form']			= RegForm()

						return render(request,'register.html',context)

				else:
					form = RegForm()

					return render(request,'register.html',context)

				attendee_details = {}
				attendee_details['name'] 			= att.attendee_name
				attendee_details['mobile'] 			= att.mobile_number
				attendee_details['email'] 			= att.attendee_email
				attendee_details['lunch'] 			= "Yes" if att.had_lunch else "No"
				attendee_details['goodie_bag'] 	= "Yes" if att.got_goodie_bag else "No"
				attendee_details['explara_bcode']	= att.explara_barcode
				attendee_details['pesit_bcode']		= att.pesit_barcode
				attendee_details['order_no']		= att.order_number
				attendee_details['ticket_no']		= att.ticket_number
				attendee_details['meal_pref']		= att.lunch_type

				initial_dict = dict()
				if explara_barcode:
					initial_dict['explara_barcode'] = explara_barcode
				if mobile_number:
					initial_dict['mobile_number']	= mobile_number

				form = RegForm(initial=initial_dict)

				context['attendee_details'] = attendee_details
				context['form']				= form
				context['form_type']		= 2	

				return render(request,'register.html',context)

			else:
				if explara_barcode:
					try:
						att = Attendee.objects.get(explara_barcode=explara_barcode)
					except:
						context['message']		= "No record found with those details."
						context['messageclass'] = "error"
						context['form']			= RegForm()
						context['form_type']	= 1	
						return render(request,'register.html',context)

				elif mobile_number:
					try:
						att = Attendee.objects.get(mobile_number=mobile_number)
					except:
						context['message'] 		= "No record found with those details."
						context['messageclass'] = "error"
						context['form']			= RegForm()
						context['form_type']	= 1
						return render(request,'register.html',context)

				att.pesit_barcode = pesit_barcode
				att.got_goodie_bag = True
				att.save()

				form = RegForm()

				context['form']				= form
				context['message']			= "Registered successfully."
				context['messageclass']		= "success"
				context['form_type']		= 1


				return render(request,'register.html',context)

@login_required(login_url='/')
def lunch(request):
	context = {}

	if request.method == 'GET':
		form_lunch	= LunchForm(prefix='lunch')

		context['form_lunch']	= form_lunch

		return render(request,'lunch.html',context)

	elif request.method == 'POST':

		form_lunch	= LunchForm(request.POST,prefix='lunch')

		if form_lunch.is_valid():
			pesit_barcode = form_lunch.cleaned_data['pesit_barcode']
			try:
				a = Attendee.objects.get(pesit_barcode=str(pesit_barcode))
			except:
				context['message']		= "No user found with those details."
				context['messageclass']	= "error"
				context['form_lunch']	= LunchForm(prefix='lunch')

				return render(request,'lunch.html',context)

			if not a.had_lunch:
				a.had_lunch = True
				a.save()
				context['message']		= "Lunch request successful for {}.".format(a.attendee_name)
				context['messageclass']	= "success"
				context['form_lunch']	= LunchForm(prefix='lunch')
				return render(request,'lunch.html',context)
			else:
				context['message']		= "Lunch request has been already processed for this user."
				context['messageclass']	= "error"
				context['form_lunch']	= LunchForm(prefix='lunch')

				return render(request,'lunch.html',context)

		


def logout_user(request):
	logout(request)

	return redirect('login')

def csv_import(request):
	context = {}

	if request.method == "GET":
		form = CSVImportForm()

		context['form']			= form

		return render(request,'csv_import.html',context)

	elif request.method == "POST":
		form = CSVImportForm(request.POST)

		if form.is_valid():

			count = 0

			csv = form.cleaned_data['csv_data']
			csv = csv.replace('"','').replace('\r','').strip().split('\n')

			for line in csv[1:]:
				csv_fields = line.split(',')

				if not Attendee.objects.filter(explara_barcode=str(csv_fields[14])).exists():
					Attendee.objects.create(
						date_registered	= csv_fields[0],
						attendee_name	= csv_fields[1],
						attendee_email	= csv_fields[2],
						ticket_name		= csv_fields[3],
						ticket_category	= csv_fields[4],
						order_number 	= csv_fields[5],
						ticket_number	= csv_fields[6],
						buyer_name		= csv_fields[7],
						buyer_email		= csv_fields[8],
						mobile_number	= csv_fields[9],
						seat_number		= csv_fields[10],
						contact_number	= csv_fields[11],
						lunch_type		= csv_fields[12],
						comment			= csv_fields[13],
						explara_barcode	= str(csv_fields[14])
					)

					count = count + 1

			context['message']		= "CSV Import successful. {} records added.".format(count)
			context['messageclass']	= "success"
			context['form']			= CSVImportForm()

			return render(request,'csv_import.html',context)

