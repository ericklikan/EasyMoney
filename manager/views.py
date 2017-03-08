from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View, CreateView, ListView, UpdateView, ListView, DeleteView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from .models import Budget, Section, Transaction
from .forms import UserForm, BudgetForm, SectionForm

@login_required
def index(request):
    user = request.user
    budgets = Budget.objects.filter(user=user)
    return render(request, 'manager/index.html', {'budgets':budgets,'user':user})

@login_required
def detail(request, budget_id):
    user = request.user
    budget = get_object_or_404(Budget, pk=budget_id)
    sections = Section.objects.filter(budget=budget,user=user)
    return render(request, 'manager/detail.html', {'budget':budget,'user':user,'sections':sections})

@login_required
def budget_create(request):
    user = request.user
    form_class = BudgetForm
    template_name = 'manager/budget_form.html'

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()

            return detail(request,budget.budget_id)

        return render(request, template_name, {'form':form})
    if request.method == 'GET':
        form = form_class(None)
        return render(request, template_name, {'user':user,'form':form})

@login_required
def budget_delete(request, pk):
    user = request.user
    budget = Budget.objects.filter(user=user, pk=pk)
    budget.delete()
    budgets = Budget.objects.filter(user=user)
    return render(request, 'manager/index.html', {'user':user,'budgets':budgets})

@login_required
def section_create(request, budget_id):
    user = request.user
    form_class = SectionForm
    budget = Budget.objects.get(user=user,pk=budget_id)
    sections = Section.objects.filter(budget=budget,user=user)
    total = 0 #Counting total amount of money all the sections have
    for section in sections:
        total = total + section.section_budget.value()
    template_name = 'manager/section_form.html'

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            newSectionAmount = form['section_budget'].value()
            if newSectionAmount < (budget.budget_total - total):
                section = form.save(commit=False)
                section.user = request.user
                section.save()

                return detail(request,budget.budget_id)
            else:
                raise ValidationError('Your sections total to too much!')
        return render(request, template_name, {'form':form})

    if request.method == 'GET':
        form = form_class(None)
        return render(request, template_name, {'user':user,'form':form})


'''
class IndexView(generic.ListView):
    template_name = 'manager/index.html'
    context_object_name = 'all_budgets'

    def get_queryset(self):
        return Budget.objects.all()

class DetailView(generic.DetailView):
    model = Budget
    template_name = 'manager/detail.html'
'''

class BudgetCreate(CreateView):
    model = Budget
    fields = ['budget_title','budget_total']

class BudgetUpdate(UpdateView):
    model = Section
    fields = ['section_title','section_budget']

class BudgetDelete(DeleteView):
    model = Section
    success_url = reverse_lazy('manager:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'manager/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #cleaned and normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns user object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('manager:index')
        return render(request, self.template_name, {'form':form})
