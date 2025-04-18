# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models import Sum
from django.shortcuts import render

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'services'

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CustomerUsage(models.Model):
    customer = models.ForeignKey('Customers', models.DO_NOTHING, blank=True, null=True)
    data_used = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=20, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    subscription = models.ForeignKey('Subscriptions', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_usage'


class Customers(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Discounts(models.Model):
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discounts'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Feedback(models.Model):
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    feedback_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback'


class Invoices(models.Model):
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=7, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    subscription = models.ForeignKey('Subscriptions', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoices'


class Payments(models.Model):
    subscription = models.ForeignKey('Subscriptions', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=7, blank=True, null=True)
    invoice = models.ForeignKey(Invoices, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments'


class Plans(models.Model):
    plan_name = models.CharField(max_length=100, blank=True, null=True)
    data_limit = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plans'


class Subscriptions(models.Model):
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    plan = models.ForeignKey(Plans, models.DO_NOTHING, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscriptions'


class SupportTickets(models.Model):
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    issue_description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=7, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    closed_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'support_tickets'

# my works now 

class CompanyProfile(models.Model):
    # Basic company information
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    
    # Additional fields from the second class
    tagline = models.CharField(max_length=255, blank=True, null=True)
    mission_statement = models.TextField(blank=True, null=True)
    about_us_text = models.TextField()
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)  # Requires Pillow
    social_media_links = models.JSONField(blank=True, null=True)  # Store social media links as JSON
    founded_on = models.DateField(blank=True, null=True)  # Date the company was founded
    team_size = models.PositiveIntegerField(blank=True, null=True)  # Number of team members

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'company_profile'

 

def home(request):
    # Fetch company profile data (assuming only one company profile exists)
    company = CompanyProfile.objects.first()

    # Fetch data from other models for dynamic metrics
    total_customers = Customers.objects.count()
    total_payments = Payments.objects.aggregate(total=Sum('amount'))['total'] or 0
    recent_feedback = Feedback.objects.order_by('-date')[:5]  # Get latest 5 feedbacks
    active_subscriptions = Subscriptions.objects.filter(is_active=True).count()

    # Pass all data to template
    context = {
        'company': company,
        'total_customers': total_customers,
        'total_payments': total_payments,
        'recent_feedback': recent_feedback,
        'active_subscriptions': active_subscriptions,
    }

    return render(request, 'home.html', context)

