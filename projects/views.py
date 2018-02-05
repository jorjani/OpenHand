from django.shortcuts import render
from .models import Campaign, Organization, Donation, User
from django.views import generic


class OrganizationListView(generic.ListView):
    model = Organization
    #context_object_name = 'all_org_list'  # your own name for the list as a template variable
    #queryset = Organization.objects.filter(name__icontains='foundation')[:5]
    #template_name = 'organizations/my_arbitrary_template_name_list.html'  # Specify your own template name/location

    #def get_queryset(self):
    #   return Organization.objects.filter(name__icontains='child')[:5]  # Get 5 organizations containing child


class OrganizationDetailView(generic.DetailView):
    model = Organization

class CampaignListView(generic.ListView):
    model = Campaign

class CampaignDetailView(generic.DetailView):
    model = Campaign


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