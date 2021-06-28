from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

DATETIME_FORMAT = "%m-%d-%Y  %M:%S"


class Outage(models.Model):
    LEVELS = (
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    )
    STATUS = (
        ('pending', 'P'),
        ('active', 'A'),
        ('resolved', 'R'),
        ('closed', 'C'),  # Close 72 hours after resolved
    )
    slug = models.SlugField(default='', editable=False, max_length=100)
    status = models.CharField(max_length=10, choices=STATUS, default='pending',
                              help_text='Update the Status to Closed after 72 hours')
    isp_provider = models.CharField(max_length=45, default='Bell')
    issue_type = models.CharField(max_length=45, default='No Sync')
    service_area = models.CharField(max_length=45, default="Location in Splunk")
    ccp_account_reference = models.CharField(blank=True, max_length=60, default='101444777')
    start_time = models.DateTimeField(blank=True, auto_now_add=False, auto_now=False, default=timezone.now,
                                      help_text="Use EST Timezone")
    etr = models.CharField(blank=True, max_length=60, default="NO ETR")
    ticket_number = models.CharField(blank=True, max_length=20, default='BR number')
    impact_level = models.CharField(blank=True, max_length=1, choices=LEVELS, default='L')
    notes = models.TextField(blank=True, max_length=150, default='none')

    def __str__(self):
        outage_name = self.isp_provider + " \"" +self.issue_type + "\" " + self.service_area
        outage_name_status = outage_name + " " + \
            "(" + self.status + ")"
        return outage_name_status


    def get_absolute_url(self):
        """ Django Admin View returns slug. Add <str:slug> to URL"""
        return reverse("outages:outage-detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        """
        On save creates slug based on
        ISP Provider Issue Type and Service Area
        """
        outage_name = self.isp_provider + " \"" + self.issue_type + "\" " + self.service_area
        self.slug = slugify(outage_name, allow_unicode=True)
        if self.status == 'resolved':
            self.notes = 'Closed ON date created'
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['status']

        """
        Resolved date with be based on the ISP time of repair. 
        Updating the status to Resolved will create a Closed ON date.       
        """