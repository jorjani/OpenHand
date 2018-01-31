from django.shortcuts import render
from .models import Campaign, Organization, Donation, User


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_campaigns = Campaign.objects.all().count()
    num_organizations = Organization.objects.all().count()
    num_successful_campaigns = Campaign.objects.filter(status__exact='s').count()
    num_users = User.objects.count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_organizations': num_organizations, 'num_campaigns': num_campaigns,
                 'num_successful_campaigns': num_successful_campaigns, 'num_users': num_users},
    )