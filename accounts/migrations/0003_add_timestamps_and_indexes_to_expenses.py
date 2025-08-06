# Generated manually for adding timestamps and indexes to Expenses model

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customer_staff_expenses'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expenses',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date_incurred',
            field=models.DateField(db_index=True),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('reimbursed', 'Reimbursed')], db_index=True, default='pending', max_length=10),
        ),
        migrations.AlterModelOptions(
            name='expenses',
            options={'ordering': ['-date_incurred', '-created_at'], 'permissions': [('can_approve_expense', 'Can approve expense')], 'verbose_name': 'Expense', 'verbose_name_plural': 'Expenses'},
        ),
        migrations.AddIndex(
            model_name='expenses',
            index=models.Index(fields=['status', 'date_incurred'], name='accounts_ex_status_b7c89e_idx'),
        ),
        migrations.AddIndex(
            model_name='expenses',
            index=models.Index(fields=['staff', 'status'], name='accounts_ex_staff_i_4a8b2c_idx'),
        ),
    ]