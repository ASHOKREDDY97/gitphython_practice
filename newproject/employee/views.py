from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import EmployeeDeatils
from .forms import EmployeeForm
from . import forms
from django.http import HttpResponse
from newproject.settings import EMAIL_HOST_USER
import logging

logging.basicConfig(filename='app.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')

logger = logging.getLogger(__name__)

# get method

def employees_list(request):
    employees = EmployeeDeatils.objects.all()
    logger.info('Retrieved object')
     
    return render(request, 'list.html',{'employees': employees})

# post method
def create_employee(request):
    if request.method == 'POST':
        logger.info('Creating a new object')
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            # Process form data
        return redirect('employees_list')
            
    else:
        form = EmployeeForm()
    return render(request, 'create.html', {'form': form})

# update
def edit_employee(request,pk):
    employee=EmployeeDeatils.objects.get(id=pk)
    logger.info('Updating object')
    form=EmployeeForm(instance=employee)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            logger.info('Object updated successfully')
        return redirect('employees_list')
    return render(request,'edit.html',{'employee':employee,'form':form})

# delete
def destroy(request,pk):
    employee = EmployeeDeatils.objects.get(id=pk)
    employee.delete()
    return redirect('employees_list')


from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage

def send_email(request):
    try:
        if request.method == 'POST':
            logger.info('Creating a new object')
            name = request.POST.get('name')
            employee_id = request.POST.get('id')
            age = request.POST.get('age')
            salary = request.POST.get('salary')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            attachment = request.FILES.get('attachment')
            email_msg = EmailMessage(
                'Employee Details',
                f"Name: {name}\nID: {employee_id}\nAge: {age}\nSalary: {salary}\nEmail: {email}\nPhone: {phone}\nMessage: {message}",
                settings.EMAIL_HOST_USER,
                [email],
            )
            if attachment:
                email_msg.attach(attachment.name, attachment.read(), attachment.content_type)
            email_msg.send(fail_silently=True)

    except KeyError as ke:
        msg = f"Key: {ke} missing in the request!"
        logger.error(msg)
        response = HttpResponse("Your request was processed.")
        response.set_cookie('my_cookie', 'cookie_value')
        return render(request, 'success.html')
    return render(request, 'sendmail.html')
    


# # sending mails
# def sending_mail(request):
#     sub = forms.MyMailForm  
#     if request.method == 'POST':
#         sub = forms.MyMailForm(request.POST)
#         subject = 'Test Mail'
        
#         listOfEmails = ["ashokkumarmvr@gmail.com","akreddy.eeeng@gmail.com"]
#         user_name = "Ashok Reddy"
#         for to_email in listOfEmails:
#             context = {"email" : to_email, "user_name":user_name}
#             html_message = render_to_string('success.html', context)
#             plain_message = strip_tags(html_message)
#             from_email = "ashokkumarmvr@gmail.com"
           
#             mail.send_mail(subject,plain_message, from_email, [to_email], html_message=html_message)
#         # send_mass_mail ((Text,Text2,),fail_silently=False)
#         # send_mail(subject, 
#         #     message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            
#         return render(request, 'success.html' )
#         # {'recepient': recepient})
#     return render(request, 'index.html', {'form':sub})

# def send_email(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         employee_id = request.POST.get('id')
#         # age = request.POST.get('age')
#         salary = request.POST.get('salary')
#         email = request.POST.get('email')
#         # phone = request.POST.get('phone')
#         # msg = request.POST.get['message']
#         message = f"Name: {name}\nID: {employee_id}\nSalary:  {salary}\nEmail: {email}"
       
#         send_mail(   
#             subject='Employee Details',
#             message=message,
#             from_email='MOURITECH<ashokkumarmvr@gmail.com>',
#             recipient_list=[email],
#             fail_silently=False,
#         )
        
#         # return render(request, 'success.html')    
#     return render(request, 'sendmail.html')




