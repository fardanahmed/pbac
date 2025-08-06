from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Staff, Customer, Expenses

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_id', 'position', 'hire_date')
    list_filter = ('position', 'hire_date')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'employee_id')
    readonly_fields = ('user',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('name', 'email')
    readonly_fields = ('created_date',)

@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('staff', 'amount', 'date_incurred', 'status', 'customer', 'created_at')
    list_filter = ('status', 'date_incurred', 'created_at')
    search_fields = ('staff__user__email', 'description', 'customer__name')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'date_incurred'
    list_per_page = 25