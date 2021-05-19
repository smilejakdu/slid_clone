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
                depth_idx        = 1 if data['depth_idx'] == 1 else data['depth_idx'],
                trash_basket     = False,
                parent_folder_id = data['parent_folder_id'],
                user_id          = request.user.id
            ).save()

            return JsonResponse({"message": "INSERT_SUCCESS_FOLDER"},status=201)

        except KeyError: # 키값 확인
            return JsonResponse({"message": "INVALID_KEY"},status=400)

        except ValueError: # value 값 확인
            return JsonResponse({"message": "VALUE_ERROR"},status=400) 

        except Exception as e:
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

            elif data['parent_folder_id'] and data['depth_idx']: # 폴더이동
                folder.parent_folder_id = data['parent_folder_id']
                folder.depth_idx        = data['depth_idx']
                folder.save()

                return JsonResponse({"message":"TRASH_BASKET_SUCCESS"} ,status=200)

        except ValueError :# value 에러
            return JsonResponse({"message":"VALUE_ERROR"} ,status=400)

        except KeyError : # key 에러 
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
        print(request.user.id)
        # 기본값 depth_idx 순으로 출력  ==> 첫번째 바로 보여주게 될때 
        # 일반적인 검색이랑 같지않을까?? 생각을 함 
        folder = (Folder.
                  objects.
                  prefetch_related('folder_set').
                  filter(depth_idx=1))

        # 생성일순 으로 출력
        # 이름순으로 출력
        return

