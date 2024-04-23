from django.db import models

class BindingInvite(models.Model):
    telephone = models.TextField()
    invite_cod = models.TextField()

    class Meta:
        db_table = "binding_invite"