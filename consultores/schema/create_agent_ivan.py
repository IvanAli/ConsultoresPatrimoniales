# small script to create ivanali as an agente

from django.contrib.auth.models import User
from .models import Agente

user = User.objects.create_user(username='ivanali', password='ivanali',
email='ivanali@outlook.com', first_name='Ivan', last_name='Soto')
user.save()

agente = Agente.objects.create(userAgente=user)
agente.save()
