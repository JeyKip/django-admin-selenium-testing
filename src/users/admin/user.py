from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.forms import BaseUserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from users.models import User


class UserCreationForm(BaseUserCreationForm):
    def clean_email(self):
        """Reject emails that differ only in case."""
        email = self.cleaned_data.get('email')

        if email and self._meta.model.objects.filter(email__iexact=email).exists():
            self._update_errors(
                ValidationError({
                    'email': _('A user with that email already exists.')
                })
            )
        else:
            return email

    class Meta(BaseUserCreationForm.Meta):
        fields = ('email',)


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    add_form_template = 'admin/users/add_form.html'
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'date_of_birth')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2'),
            },
        ),
    )
    add_form = UserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('date_joined',)
