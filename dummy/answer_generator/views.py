from django.http import HttpResponse
from django.template import loader
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView, DetailView, ListView

from .forms import FileForm
from .models import PdfFile

from . import views

def index(request):
    template = loader.get_template('answer_generator/index.html')
    context = {
        'company_name': 'Hunar smart',
    }
    return HttpResponse(template.render(context, request))


 # Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView, DetailView, ListView

from .forms import FileForm
from .models import PdfFile

class PdfFileView(FormView):
	template_name = 'answer_generator/pdf_file_form.html'
	form_class = FileForm

	def get_success_url(self):
		return ('answer_generator')

	def form_valid(self, form):
		Pdf_File = PdfFile(
		file=self.get_form_kwargs().get('files')['file'])
		Pdf_File.save()
		self.id = Pdf_File.id
		return HttpResponseRedirect((self.get_success_url()))



