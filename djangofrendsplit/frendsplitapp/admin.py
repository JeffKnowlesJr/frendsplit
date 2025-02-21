from django.contrib import admin
from .models import Group, Expense, ExpenseSplit, Settlement

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')
    filter_horizontal = ('members',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'group', 'paid_by', 'split_type', 'created_at')
    list_filter = ('group', 'split_type', 'created_at')

@admin.register(ExpenseSplit)
class ExpenseSplitAdmin(admin.ModelAdmin):
    list_display = ('expense', 'user', 'amount', 'paid')
    list_filter = ('paid', 'user')

@admin.register(Settlement)
class SettlementAdmin(admin.ModelAdmin):
    list_display = ('group', 'payer', 'receiver', 'amount', 'created_at', 'completed')
    list_filter = ('completed', 'group', 'created_at')
