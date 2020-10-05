from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from apps.client.models import Client


def get_user(request):
    try:
        user = User.objects.get(username=request.user)
        client = Client.objects.get(user=user)
        return {'client': client, 'user': user}
    except ObjectDoesNotExist:
        raise Exception("El usuario no existe")