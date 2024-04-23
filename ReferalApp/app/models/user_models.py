from django.db import models

class User(models.Model):
    telephone = models.TextField()
    status_auth = models.BooleanField()
    personal_invite = models.TextField()
    temporary_code = models.TextField()
    activate_invait = models.BooleanField(default=False)
    telephone_invait = models.TextField()

    class Meta:
        db_table = "users"