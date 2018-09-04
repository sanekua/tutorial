from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
#
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
#

from django.http import HttpResponse
from django.template import loader

#
# from .models import Question
#
#
#
#
#
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

#
# from django.shortcuts import render
# from django.views import View
#
#
# def my_index_view(request):
#     data = {'text':"Hello world"}
#     render(request,'university/custom_html.html',data)
#
#
# class MyView(View):
#     data = {'text': "Hello world"}
#     #form = StudentForm
#     template_name = 'university/custom_html.html'
#
#     def get(self, request, *args, **kwargs):
#         #form = self.form_class(initial=self.initial)
#         return render(request, self.template_name,self.data)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')
    #
    #     return render(request, self.template_name, {'form': form})


from django.shortcuts import render


def index(request):
    return render(request, "index.html")