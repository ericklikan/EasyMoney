from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View, CreateView, ListView, UpdateView, ListView, DeleteView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from .models import Budget, Section
from .forms import UserForm

@login_required
def index(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'manager/index.html', {'budgets':budgets})

@login_required
def detail(request, budget_id):
    budget = get_object_or_404(Budget, pk=budget_id)
    return render(request, 'manager/detail.html', {'budget':budget})

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
        return render(request, self.template_name, {{'form':form}})
