from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import uuid as uuid_lib

from .const import RESIDENCE_CHOICIES, CRACK_LEVEL_CHOICIES, CATEGORY_CHOICIES


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(
        default=uuid_lib.uuid4,
        primary_key=True,
        editable=False,
    )
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), blank=False)

    sex = models.CharField(
        max_length=5,
        blank=False,
        choices=[('men', '男性'), ('women', '女性')],
    )
    residence = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=RESIDENCE_CHOICIES,
    )
    introduction = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )
    icon = models.ImageField(
        upload_to='images',
        blank=True,
    )
    learning_started_date = models.DateField(
        blank=True,
        null=True,
        help_text=_('When your start learning')
    )
    crack_level = models.CharField(
        max_length=50,
        default=1,
        choices=CRACK_LEVEL_CHOICIES,
    )

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
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = False

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
