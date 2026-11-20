from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Function View

def home(request):
    # return HttpResponse("""
    # "<h1>Hey I am a django server</h1>
    # <p style="color:red">lorem32</p>
    # """)

    peoples=[
        {'name':'Raj', 'age':34},
        {'name':'Shubham', 'age':17},
        {'name':'Snehal', 'age':24},
        {'name':'Prakash', 'age':27}
    ]

    vegetables = ['tomato','potato','cucumber','pumpkin']
    text="""
        dnklhdjkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
    """
    return render(request, 'home/index.html', context={'peoples':peoples, 'text':text, 'vegetables':vegetables})

def success_page(request):
    return HttpResponse("<h1>This is a success page<h1>")

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')