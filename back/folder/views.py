import json
import random
import datetime

from django.db.models import Q
from django.views     import View
from django.http      import JsonResponse, HttpResponse
from folder.models    import Folder
from user.models      import User
from user.utils       import login_check



class FolderView(View):
    @login_check
    def post(self, request):
        data = json.loads(request.body)

        try:
            Folder(
                name             = data['name'] if data['name'] else 'Untitled folder',
                depth_idx        = 0 if data['depth_idx'] == 0 else data['depth_idx'],
                trash_basket     = False,
                parent_folder_id = data['parent_folder_id'] if data['parent_folder_id'] else 0,
                user_id          = User.objects.get(id = request.user.id)
            ).save()

            return JsonResponse({"message": "INSERT_FOLDER"},status=201)
        except KeyError:
            return JsonResponse({"message": "INVALID_KEY"},status=400)

        except Exception as e :
            return JsonResponse({"message": e},status=400)

    @login_check
    def put(self, request):
        data = json.loads(request.body)

        try:

            folder = Folder.objects.get(id        = data['id'],
                                        user_id   = request.user.id,
                                        depth_idx = data['depth_idx'])

            if data['name']: # 이름변경
                folder.name = data['name']
                folder.save()
                return JsonResponse({"message":"UPDATE_SUCCESS"} ,status=200)

            elif data['trash_basket']: # 삭제 바구니로 이동
                folder.trash_basket = True
                folder.save()
                return JsonResponse({"message":"TRASH_BASKET_SUCCESS"} ,status=200)

            elif data['parent_folder'] and data['depth_idx']: # 폴더이동

                return JsonResponse({"message":"TRASH_BASKET_SUCCESS"} ,status=200)
        except KeyError :
            return JsonResponse({"message":"KEY_ERROR"} ,status=400)

        except Exception as e :
            return JsonResponse({"message":e} ,status=400)

    @login_check
    def delete(self , request): # 영구 삭제
        try:

            folder = Folder.objects.get(id        = data['id'],
                                        user_id   = request.user.id ,
                                        depth_idx = data['depth_idx'])
            folder.delete()
            return JsonResponse({"message":"DELETE_SUCCESS"} ,status=200)

        except KeyError :
            return JsonResponse({"message":"KEY_ERROR"} ,status=400)

        except Folder.DoesNotExist:
            return JsonResponse({"message":"DOES_NOT_FOLDER"} ,status=400)

        except Exception as e :
            return JsonResponse({"message":e} ,status=400)

    @login_check
    def get(self ,request):
        # 기본값 id 순으로 출력 
        # 생성일순 으로 출력
        # 이름순으로 출력
        return

