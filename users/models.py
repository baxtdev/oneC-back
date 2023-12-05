from django.db import models
from django.db import transaction

# Create your models here.

class UserInfo(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
        )
    company = models.CharField(
           max_length=250,
    )    
    full_name = models.CharField(
           max_length=250
    )
    user_id = models.BigIntegerField(
    )
    credit = models.FloatField()


    class Meta:
        db_table = 'info'
        managed = True
        verbose_name = 'User Info'
        verbose_name_plural = 'Users Ifos'

    def __str__(self) -> str:
        return self.full_name    
    
    def save(self, *args, **kwargs):
        try:
            us=UserInfo.objects.get(
                user_id=self.user_id
            )
            us.delete()
            super().save(*args, **kwargs)

        except UserInfo.DoesNotExist:
            super().save(*args, **kwargs)