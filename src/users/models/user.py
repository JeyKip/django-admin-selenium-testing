from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=128, validators=[
        RegexValidator(regex=r'^[^<>&"]*$')
    ])
    last_name = models.CharField(_('last name'), max_length=128, validators=[
        RegexValidator(regex=r'^[^<>&"]*$')
    ])
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_of_birth = models.DateField(_('date of birth'), null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now, db_index=True)

    USERNAME_FIELD = 'email'

    class Meta:
        swappable = 'AUTH_USER_MODEL'
