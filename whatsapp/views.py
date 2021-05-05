from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,"home.html")

def WhatsappData(Ph, Message):
    import time
    import webbrowser as web
    import pyautogui
    Phone = "+91"+Ph
    web.open('https://web.whatsapp.com/send?phone='+Phone+'&text='+Message)
    time.sleep(30)

    pyautogui.press('enter')


    
def SendData(request):
    if request.method == 'POST':
        Ph = request.POST['Phone']
        Message = request.POST['Message']
        # print(Ph,Message)
        WhatsappData(Ph,Message)
        msg = "Message has successfully sent.."
        return render(request,"home.html",{'msg':msg})
    else:
        return HttpResponse("<h1>404- Not Found :)</h1>")