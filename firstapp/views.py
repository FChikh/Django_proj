import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.
from firstapp.forms import CalcForm
from firstapp.models import CalcHistory
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm


@login_required
def calc(request):
    # Базовый контекст
    context = {}
    history = CalcHistory.objects.all()
    context['history'] = history
    if request.method == 'POST':
        f = CalcForm(request.POST)
        if f.is_valid():
            # обработка вычисления
            a = f.data['first']
            b = f.data['second']
            c = int(a) + int(b)

            # формирование ответа
            context['first'] = a
            context['second'] = b
            context['result'] = c
            context['form'] = f
            item = CalcHistory(date=datetime.datetime.now(),
                               first=a,
                               second=b,
                               result=c,
                               author=request.user)
            item.save()
        else:
            context['form'] = CalcForm()
    else:
        req = request.GET.get('delete', '')
        if req != '':
            item = CalcHistory.objects.filter(id=int(req))
            item.delete()
        context['nothing_entered'] = True
        context['form'] = CalcForm()
        context['first'] = 0
        context['second'] = 0
        context['result'] = 0
    return render(request, 'calculator.html', context)


def index(request):
    return redirect("/calc")


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
