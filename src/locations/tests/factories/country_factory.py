import factory
from faker.providers.address import Provider

from locations.models import Country


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    # To make sure name corresponds to ISO code and every time a unique country name is generated,
    # we should use Iterator. Also, iterable passed are not infinite, so this factory allows to create each country
    # once and then if fails.
    name = factory.Iterator(Provider.countries)
    iso_code = factory.Iterator(Provider.alpha_2_country_codes)
