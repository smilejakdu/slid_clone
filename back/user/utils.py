# autopep8: off
import os
import jwt
import json

from back                   import my_settings
from pathlib                import Path
from django.http            import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ImproperlyConfigured
from .models                import User


def login_check(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token     = request.headers.get('Authorization', None)
            key       = my_settings.SECRET.get('secret')
            algorithm = my_settings.SECRET.get('algorithm')

            if token == None:
                return JsonResponse({"message" : "TOKEN_DOES_NOT_EXIST"}, status=403)

            decode       = jwt.decode(token, key, algorithm = algorithm)
            user         = User.objects.get(id=decode['user'])
            request.user = user

        except jwt.DecodeError:
            return JsonResponse({"message": "INVALID_TOKEN"}, status=403)
        except User.DoesNotExist:
            return JsonResponse({'message': 'USER_DOES_NOT_EXIST'}, status=403)

        return func(self, request, *args, **kwargs)

    return wrapper
