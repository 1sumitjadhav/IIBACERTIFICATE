from fileinput import filename
import imghdr
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from .forms import CsvModelForm
from .models import Csv
import csv
from reportlab.pdfgen import canvas
from django.core.mail import send_mail, EmailMessage
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.message import EmailMessage
from django.contrib.auth.decorators import login_required
import os

@login_required(login_url='login')
def Upload(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm
        obj = Csv.objects.get(activated=False)
        with open(obj.file.path, 'r') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                    row = ",".join(row)
                    row = row.replace(',', ' ')
                    row = row.split()
                    name = row[0]
                    email = row[1]
                    course = row[2]

                    cert = canvas.Canvas(filename=f'{name}.pdf')
                    cname = cert.beginText()
                    cname.textLine(name)

                    cert.drawText(cname)
                    cert.showPage()
                    cert.save()

                    email_sender = 'dummyaccdevteam@gmail.com'
                    password = 'careteam1234'
                    subject = 'heres ur email'
                    send_email = email
                    msg = EmailMessage()
                    msg['From'] = email_sender
                    msg['To'] = email
                    msg['Subject'] = subject

                    file = open(f'{name}.pdf', 'rb')
                    file_data = file.read()
                    file_name = file.name

                    msg.add_attachment(file_data, maintype = 'pdf', subtype = 'file', filename=file_name)
                    # msg.attach(MIMEText(text, "plain"))
#                     attach_file_name = f'{name}.pdf'
#                     attach_file = open(attach_file_name, 'rb')
#                     payload = MIMEBase('application', 'octate-stream')
#                     payload.set_payload((attach_file).read())
#                     encoders.encode_base64(payload) #encode the attachment
# #add payload header with filename
#                     payload.add_header('Content-Decomposition', 'attachment', filename=f'{name}.pdf')
#                     msg.attach(payload)



                    
                    
                    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                   
                    server.login(email_sender, password)
                    text = msg.as_string()
                    server.send_message(msg)
                    server.quit()




              
            obj.activated = True
            obj.save()
            return HttpResponse('Sent Successfully')
        # return redirect(request, 'input/event.html')
        # return FileResponse(as_attachment=True, filename=f'{name}.pdf')
    context ={'form':form}
    return render(request, 'certgen/cert.html', context)
# Create your views here.

def sample(request):
    csv = open('media/test.csv', 'rb')
    return FileResponse(csv)