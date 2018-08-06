from django.shortcuts import render
from .form import UploadFileForm
from .methods import handle_uploaded_file, ploting
from django.http import  Http404, FileResponse
import threading

def pdf_view(request, name):
    try:
        return FileResponse(open(name, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def page(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        save_path='/tmp/'
        if form.is_valid():
            name = handle_uploaded_file(request.FILES['file'])
            name = ploting(name)
            return pdf_view(request, name) 
        else:
            return Http404('Invalid data')
    else:
        form = UploadFileForm()
        return render(request, "linreg/page.html", {'form' : form })
