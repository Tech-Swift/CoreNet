from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone
from .models import CompanyProfile, Customers, Payments, Feedback, Subscriptions, Invoices
from django.http import HttpResponse, JsonResponse
from  django_daraja.mpesa.core import MpesaClient  # Assuming you have a client for M-Pesa integration
from django.views.decorators.csrf import csrf_exempt
from datetime import date
import json

def home(request):
    """
    Renders the homepage with company profile information and key metrics.
    """
    try:
        company_profile = CompanyProfile.objects.first()
    except CompanyProfile.DoesNotExist:
        company_profile = None  # Handle the case where no profile exists yet

    total_customers = Customers.objects.count()
    total_payments = Payments.objects.aggregate(total=Sum('amount'))['total'] or 0
    recent_feedback = Feedback.objects.order_by('-feedback_date')[:3]  # Get the 3 most recent feedback entries
    active_subscriptions = Subscriptions.objects.filter(end_date__gte=timezone.now()).count() # Count active subscriptions

    context = {
        'company': company_profile,
        'total_customers': total_customers,
        'total_payments': total_payments,
        'recent_feedback': recent_feedback,
        'active_subscriptions': active_subscriptions,
    }

    return render(request, 'home.html', context)


