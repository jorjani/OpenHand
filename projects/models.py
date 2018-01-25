from django.db import models

class Project(models.Model):
    name = models.CharField(max_length = 40, helper_text = "project name")
    description = models.TextField(helper_text="project description")
    organization = models.ForeignKey('Organization', on_delete = models.CASCADE)
    FUNDING_STATUS = (
        ('p', 'Pending'),
        ('a', 'Active'),
        ('s', 'Successful'),
        ('c', 'Closed'),
        ('i', 'Inactive')
    )
    status = models.CharField(max_length=1, choices=FUNDING_STATUS, blank=True, default='m', help_text='Project Funding Status')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('model-detail-view', args=[str(self.id)])

class Organization(model.Model):
    name = models.CharField(max_length = 40, helper_text = "organization name")
    description = models.TextField(helper_text="organization description")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('model-detail-view', args=[str(self.id)])


import uuid  # Required for unique book instances


class Donation(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular donation")
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)
    donor = models.ForeignKey('User')
    date = models.DateField(null=True, blank=True)
    amount = models.CharField('Amount')
    currency = models.CharField('Currency')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        """
        String for representing the Model object
        """
        return '{0} ({1})'.format(self.id, self.book.title)


class User(models.Model):
    """
    Model representing a user.
    """
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