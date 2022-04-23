from django.db.models.signals import post_save
from django.dispatch import receiver

from user_app.models import User,Achetteur,Vendeur

@receiver(post_save,sender=User)
def post_save_created(sender,instance,created,**kwargs):
    if created:
        if instance.type==User.Type.ACHETTEUR:
            Achetteur.objects.create(user=instance)

        elif instance.type==User.Type.VENDEUR:
            Vendeur.objects.create(user=instance)
