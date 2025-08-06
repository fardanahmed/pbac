from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Expenses

@login_required
@permission_required('accounts.can_approve_expense', raise_exception=True)
def approve_expense(request, expense_id):
    expense = get_object_or_404(Expenses, id=expense_id)
    if request.method == 'POST' and expense.status == 'pending':
        expense.status = 'approved'
        expense.save()
        return redirect('expense_list')
    return render(request, 'approve_expense.html', {'expense': expense})

@login_required
def expense_list(request):
    expenses = Expenses.objects.select_related('staff__user', 'customer').all()
    return render(request, 'expense_list.html', {'expenses': expenses})