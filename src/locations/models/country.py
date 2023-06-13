from django.db import models
from django.db.models import Count
from django.utils.translation import gettext_lazy as _


class CountryQuerySet(models.QuerySet):
    def with_number_of_users(self):
        return self.annotate(number_of_users=Count('users', distinct=True))


class Country(models.Model):
    objects = CountryQuerySet.as_manager()

    name = models.CharField(_('Name'), max_length=128, unique=True)
    iso_code = models.CharField(_('ISO Code'), max_length=8, unique=True)

    def __str__(self):
        return f'{self.name} ({self.iso_code})'

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
