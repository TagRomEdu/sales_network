from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


class Product(models.Model):
    """
    Product's model for network.
    """
    name = models.CharField(
        max_length=200,
        verbose_name=_('Name')
    )
    model = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_('Model')
    )
    release_date = models.DateField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name=_('Release date')
    )

    def __str__(self):
        return f'{self.name} - {self.model} ({self.release_date})'

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class NetworkLink(models.Model):
    """
    Model for network links.
    """

    PLANT = 'plant'
    RETAIL_NETWORK = 'retail_network'
    INDIVIDUAL_ENTREPRENEUR = 'individual_entrepreneur'
    LEVEL_CHOICES = [
        (PLANT, 'Plant'),
        (RETAIL_NETWORK, 'Retail network'),
        (INDIVIDUAL_ENTREPRENEUR, 'Individual entrepreneur')
    ]

    network = models.CharField(
        max_length=23,
        choices=LEVEL_CHOICES,
        verbose_name=_('Network')
    )
    name = models.CharField(
        max_length=150,
        verbose_name=_('Name'),
    )

    # Contacts
    email = models.EmailField(
        verbose_name=_('Email'),
    )
    country = models.CharField(
        max_length=15,
        verbose_name=_('Country'),
    )
    city = models.CharField(
        max_length=25,
        verbose_name=_('City'),
    )
    street = models.CharField(
        max_length=100,
        verbose_name=_('Street'),
    )
    house_number = models.CharField(
        max_length=15,
        verbose_name=_('House number'),
    )

    # Products
    products = models.ManyToManyField(
        Product,
        blank=True,
        related_name='network_links',
        verbose_name=_('Products'),
    )
    distributor = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='network_link',
        verbose_name=_('Distributor'),
        blank=True,
        null=True,
    )
    debt = models.DecimalField(
        max_digits=25,
        decimal_places=2,
        default=0.00,
        verbose_name=_('Debt'),
        help_text=_(
            '''You indicate the debt to the supplier in monetary terms
            from the moment to the penny.'''),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at'),
    )
    hierarchy = models.IntegerField(
        default=0,
        verbose_name=_('Hierarchy'),
        help_text=_('Hierarchy must be between 0 and 2.'),
    )

    def __str__(self):
        return f'{self.name}'

    def clean(self):
        """
        Model validation for hierarchy and debt.
        """
        cleaned_data = super().clean()

        # Validation of distributor link availability
        if self.distributor:
            if self.distributor == self:
                raise ValidationError(_('He cannot be his own distributor.'))
            elif self.distributor.hierarchy == 2:
                raise ValidationError(_('Hierarchy level exceeded.'))
            elif self.debt < 0:
                raise ValidationError(_('Debt must be greater than 0.'))

        # Setting the Hierarchy Level
        if self.network == self.PLANT and not self.distributor:
            self.hierarchy = 0

        elif self.network != self.PLANT and not self.distributor:
            raise ValidationError(
                _('The distributor must have this link in the network.')
                )

        elif self.distributor and not self.distributor.distributor:
            self.hierarchy = 1

        else:
            self.hierarchy = 2

        # Validation of debt
        if self.hierarchy == 0 and self.debt != 0:
            raise ValidationError(
                _('There is no supplier to display the debt.')
                )

        return cleaned_data

    class Meta:
        verbose_name = _('Network link')
        verbose_name_plural = _('Network links')
