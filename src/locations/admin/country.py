from django.contrib import admin
from django.contrib.admin import display
from django.utils.translation import gettext_lazy as _

from locations.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'iso_code', 'number_of_users')
    readonly_fields = ('number_of_users',)
    search_fields = ('name', 'iso_code')
    ordering = ('id',)

    def get_queryset(self, request):
        return super().get_queryset(request).with_number_of_users()

    @display(description=_('Number of users'))
    def number_of_users(self, obj: Country) -> int:
        return getattr(obj, 'number_of_users', 0)
