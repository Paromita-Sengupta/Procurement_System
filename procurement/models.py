from django.db import models
from django.utils.safestring import mark_safe
from django.utils.timezone import now as timezone_now

MONTH = 30 * 24 * 60 * 60
WEEK = 7 * 24 * 60 * 60
DAY = 24 * 60 * 60
HOUR = 60 * 60
MINUTE = 60


class DashboardModel(models.Model):
    """
    Abstract base model for things which will be displayed on the dashboard, adds in created and updated fields,
    and provides a convenience method which provides a nicely formatted string of the time since update.
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True


    @property
    def time_since_update(self):
        update_delta = timezone_now() - self.updated
        seconds_since_update = update_delta.seconds

        if seconds_since_update / MONTH >= 1:
            quantity = seconds_since_update / MONTH
            units = 'months' if quantity > 1 else 'month'

        elif seconds_since_update / WEEK >= 1:
            quantity = seconds_since_update / WEEK
            units = 'weeks' if quantity > 1 else 'week'

        elif seconds_since_update / DAY >= 1:
            quantity = seconds_since_update / DAY
            units = 'days' if quantity > 1 else 'day'

        elif seconds_since_update / HOUR >= 1:
            quantity = seconds_since_update / HOUR
            units = 'hours' if quantity > 1 else 'hour'

        elif seconds_since_update / MINUTE >= 1:
            quantity = seconds_since_update / MINUTE
            units = 'minutes' if quantity > 1 else 'minute'

        else:
            return "updated just now"

        # Ensure the quantity output is rounded to 2 decimal places
        base_string = 'updated {quantity:.2f} {units} ago'
        return base_string.format(quantity=quantity, units=units)


class Representatives(models.Model):
    """
        Model which represents representatives of suppliers

    """

    class Meta:
        # default_permissions = ('add', 'change', 'delete', 'view')
        verbose_name_plural = "Representatives"

    # This model holds name, email and phone number of a representative
    representative_name = models.CharField(max_length=255, null=True, blank=True)
    representative_email = models.EmailField(max_length=255, null=True, blank=True)
    phone_number = models.CharField('Contact Phone', max_length=12, null=True, blank=True)

    def __str__(self):
        return ' {}'.format(self.representative_name)


class Supplier(DashboardModel):
    """
    Model which represents an individual or organisation which supplies components
    """
    # default_permissions = ('add', 'change', 'delete', 'view')
    name = models.CharField(max_length=255,null=True)
    # To represent multiple Representatives
    representatives = models.ManyToManyField(Representatives,related_name = "suppliers", blank=True)
    is_authorized = models.BooleanField()


    class Meta:
        ordering = ('name',)

    def get_repname(self):

        # function returning representative_names in bullet points
        to_return = '<ul>'
        to_return += '\n'.join('<li>{}</li>'.format(str(name)) for name in self.representatives.values_list('representative_name', flat=True))
        to_return += '</ul>'
        return mark_safe(to_return)



    def get_repemail(self):

        # function returning epresentative_emails in bullet points
        to_return = '<ul>'
        to_return += '\n'.join('<li>{}</li>'.format(str(email)) for email in self.representatives.values_list('representative_email', flat=True))
        to_return += '</ul>'
        return mark_safe(to_return)

    def get_repcontact(self):

        # function returning contact no. in bullet points
        to_return = '<ul>'
        to_return += '\n'.join('<li>{}</li>'.format(str(phn)) for phn in self.representatives.values_list('phone_number', flat=True))
        to_return += '</ul>'
        return mark_safe(to_return)


    # Attribute Names
    get_repname.short_description = 'Representative Name'
    get_repemail.short_description = 'Representative Email'
    get_repcontact.short_description = 'Contact Number'


    def __str__(self):
        return '{} '.format(self.name)



class Component(DashboardModel):
    """
    Model which represents items which may be supplied.
    """
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=50)
    suppliers = models.ManyToManyField(Supplier, related_name='components', blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return '{} ({})'.format(
            self.name,
            self.sku
        )
