from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "pages/home.html")

def services(request):
    context = {
        'services': ["system repairs", "system update", "faulty parts replacements", "conflicts resolution", "system configuration"]
    }
    return render(request, "pages/services.html", context)

def testimonials(request):
    context = {
        'testimonials': 
        {
        'Barry Allen': "5 stars. I got my Phone battery replaced in a phone I have been using for 5 years, and it now works as good as new.",
        'Bruce Wayne': "4 stars. They helped me to update my system, but the update is worse than the last one. Ofcourse, it's not their fault, they didn't make the system, but a little dissatisfaction means no 5 stars.",
        'Diana Prince': "5 stars. They are very good.",
        'Clark Kent': "5 stars. They fixed my tablet's screen perfectly."
        }
    }
    return render(request, "pages/testimonials.html", context)

def pricing(request):
    context = {
        'services':{
        'system repairs': {'phone repairs': 500, 'laptop repairs': 700, 'CPU repairs': 1000},
        'system update': {'phone updates': 200, 'laptop updates': 400},
        'faulty parts replacements': {'phone parts': 300, 'laptop parts': 500, 'CPU parts': 800},
        'conflicts resolution': {'phone resolution': 100, 'laptop resolution': 200},
        'system configuration': {'phone configuration': 200, 'laptop configuration': 400}
        }
    }
    return render(request, "pages/pricing.html", context)

def blog(request):
    return render(request, "pages/blog.html")

def case_studies(request):
    return render(request, "pages/case-studies.html")