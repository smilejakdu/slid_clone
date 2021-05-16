import os
import json
import bcrypt
import re
import jwt
import requests

from django.views   import View
from django.http    import JsonResponse
from product.models import Product

class ProductView(View):
    def post(self , request):
        data = json.loads(request.body)
        try:
            Product.objects.create(
                name        = data["name"],
                price       = data["price"],
                description = data["description"],
                active      = data["active"]
            )
            return JsonResponse({"message": "INSERT_SUCCESS!"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except Exception as e:
            return JsonResponse({"message": e}, status=400)

    def put(self , request):
        data = json.loads(request.body)
        try:
            if not Product.objects.filter(name = data["name"]).exists():
                return JsonResponse({"message", "DOESNOT_PRODUCT"}, status=400)

            product_data = Product.objects.get(name = data["name"])

            product_data.name        = data["name"]
            product_data.price       = data["price"]
            product_data.description = data["description"]
            product_data.active      = data["active"]
            product_data.save()

            return JsonResponse({"message":"UPDATE_SUCCESS"},status=200)

        except Product.DoesNotExist:
            return JsonResponse({"message": "Product_DoesNotExist"}, status=404)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except Exception as e:
            return JsonResponse({"message": e}, status=400)

    def get(self , request):
        try:
            product = Product.objects.values()

        except Exception as e:
            return JsonResponse({"GET_SUCCESS": list(product)}, status=400)

    def delete(self , request):
        data = json.loads(request.body)
        try:
            if not Product.objects.filter(id=data["product_idx"]).exists():
                return JsonResponse({"message", "DOESNOT_PRODUCT"}, status=400)

            Product.objects.get(id = data["product_idx"]).delete()
            return JsonResponse({"message":"DELETE_SUCCESS"},status=200)

        except Product.DoesNotExist:
            return JsonResponse({"message": "Product_DoesNotExist"}, status=404)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except Exception as e:
            return JsonResponse({"message": e}, status=400)
