from django.db import models
from django.urls import reverse


class Campaign(models.Model):
    name = models.CharField(max_length = 40)
    description = models.TextField()
    organization = models.ForeignKey('Organization', on_delete = models.CASCADE)
    FUNDING_STATUS = (
        ('p', 'Pending'),
        ('a', 'Active'),
        ('s', 'Successful'),
        ('c', 'Closed'),
        ('i', 'Inactive')
    )
    status = models.CharField(max_length=1, choices=FUNDING_STATUS, blank=True, default='m', help_text='Campaign Funding Status')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('model-detail-view', args=[str(self.id)])


class Organization(models.Model):
    name = models.CharField(max_length = 40)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('organization', args=[str(self.id)])


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular user instance.
        """
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.last_name, self.first_name)


class Donation(models.Model):
        """
        Model representing a specific copy of a book (i.e. that can be borrowed from the library).
        """
        campaign = models.ForeignKey('Campaign', on_delete=models.SET_NULL, null=True)
        donor = models.ForeignKey('User', on_delete = "Protect")
        date = models.DateField(null=True, blank=True)
        amount = models.CharField('Amount', max_length=10)
        currency = models.CharField('Currency', max_length=3)

        def __str__(self):
            """
            String for representing the Model object
            """
            return '{0} ({1})'.format(self.id, self.book.title)