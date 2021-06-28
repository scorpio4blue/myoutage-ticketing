from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from outageticketing.settings import EMAIL_HOST_USER

def mail(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get(f'{new_closed}') # This will come from New & Closed
        content = request.POST.get('content')
        html = request.POST.get('html')
        msg = EmailMultiAlternatives(f'{subject}', f'{text_content}', EMAIL_HOST_USER)
    return render(request, 'email.html')
