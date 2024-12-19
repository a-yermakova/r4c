from django.db import models
from django.db.models import Count
from typing import List, Dict, Any
from datetime import datetime, timedelta


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)

    @classmethod
    def get_weekly_summary(cls) -> List[Dict[str, Any]]:
        """
        Get data for the last week with grouping by model and version.
        Returns a list of dictionaries with fields: model, version and count.
        """
        last_week = datetime.now() - timedelta(days=7)
        return (
            cls.objects.filter(created__gte=last_week)
            .values('model', 'version')
            .annotate(count=Count('id'))
        )
