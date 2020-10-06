from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from apps.client.models import Client


def get_user(request):
    try:
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)
            return {'user': user}
        else:
            return {}
    except ObjectDoesNotExist:
        raise Exception("El usuario no existe")