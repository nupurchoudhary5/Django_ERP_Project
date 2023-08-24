from django.shortcuts import render
from .models import StudentResult

def index(request):
    return render(request, 'departments/adminkit/index.html')

# def profile(request):
#     return render(request, 'departments/adminkit/pages-profile.html')

# def signin(request):
#     return render(request, 'departments/adminkit/pages-sign-in.html')

# def signup(request):
#     return render(request, 'departments/adminkit/pages-sign-up.html')

# # Add more views for other HTML templates as needed

# def blank_page(request):
#     return render(request, 'departments/adminkit/pages-blank.html')

# def google_maps(request):
#     return render(request, 'departments/adminkit/maps-google.html')

# def buttons(request):
#     return render(request, 'departments/adminkit/ui-buttons.html')

# def cards(request):
#     return render(request, 'departments/adminkit/ui-cards.html')

# def forms(request):
#     return render(request, 'departments/adminkit/ui-forms.html')

# def typography(request):
#     return render(request, 'departments/adminkit/ui-typography.html')

# def upgrade_to_pro(request):
#     return render(request, 'departments/adminkit/upgrade-to-pro.html')

def student_results(request):
    results = StudentResult.objects.all()
    return render(request, 'departments/adminkit/student_results.html', {'results': results})