from django.db import models


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)

    @classmethod
    def create_robot(cls, model: str, version: str, created: str):
        serial = f"{model}-{version}"
        robot = Robot(
            serial=serial,
            model=model,
            version=version,
            created=created,
        )
        robot.save()
        return robot
