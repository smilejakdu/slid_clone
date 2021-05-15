import os
import json
import bcrypt
import re
import jwt
import requests

from django.views           import View
from user.models            import User
from django.http            import JsonResponse
from back                   import my_settings

class SignUpView(View):
    def post(self , request):
        try:

            data = json.loads(request.body)
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if not (re.search(regex , data['email'])):
                return JsonResponse({"message": "INVALID_EMAIL"}, status=400)
            
            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({"message": "EMAIL_EXISTS"}, status=400)

            password       = data['password'].encode('utf-8')
            password_crypt = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')

            User(
                email    = data['email'],
                password = password_crypt
            ).save()

            return JsonResponse({"message": "SIGNUP_SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except ValueError:
            return JsonResponse({"message": "VALUE_ERROR"}, status=400)
        
        except Exception as e:
            return JsonResponse({"message": e}, status=400)
 
class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User.objects.get(email=data['email'])

            if bcrypt.checkpw(data['password'].encode('UTF-8'), user.password.encode('UTF-8')):
                key       = my_settings.SECRET.get('secret')
                algorithm = my_settings.SECRET.get('algorithm')
                token     = jwt.encode({'user' : user.id},key, algorithm = algorithm).decode('UTF-8')

                return JsonResponse({"token"  : token,
                                    "message" : "SIGNIN_SUCCESS",
                                     "email"  : user.email}, status=200)

            else:
                return JsonResponse({"message": "INVALID_PASSWORD"}, status=401)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except ValueError:
            return JsonResponse({"message": "VALUE_ERROR"}, status=400)

        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=401)
