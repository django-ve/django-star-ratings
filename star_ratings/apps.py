from __future__ import unicode_literals

from django.apps import AppConfig
from django.db.models.signals import post_save, post_delete
from django.utils.translation import gettext_lazy as _


class StarRatingsAppConfig(AppConfig):
    name = 'star_ratings'
    verbose_name = _('Star Ratings')

    def ready(self):
        from .models import UserRating
        from .signals import calculate_ratings

        post_save.connect(calculate_ratings, sender=UserRating)
        post_delete.connect(calculate_ratings, sender=UserRating)

        # Add System checks
        from .checks import rerate_check  # NOQA
        from django.core.checks import Tags, register as register_check

        register_check(rerate_check, Tags.compatibility)
