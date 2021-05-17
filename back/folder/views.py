import json
import random
import datetime
import utils

from django.db.models import Q
from django.views     import View
from django.http      import JsonResponse, HttpResponse
from folder.models    import Folder
from user.models      import User
from user.utils       import login_check

#name        = models.CharField(max_length=100)
#depth_idx   = models.IntegerField(null=True)
#trash_bool  = models.BooleanField(default=False)
#folder_path = models.ForeignKey('self' , on_delete=models.CASCADE , null=True)
#user        = models.ForeignKey(User , on_delete=models.CASCADE)
#created_at  = models.DateTimeField(auto_now_add=True)


class FolderView(View):
    @login_check
    def post(self, request):
        data = json.loads(request.body)

        try:
           Folder(
            name           = data['name'] if data['name'] else 'Untitled folder',
            depth_idx      = 0 if data['depth_idx'] == 0 else data['depth_idx'],
            folder_path_id = data['depth_idx'] - 1,
            user_id        = User.objects.get(id = request.user.id)
           ).save()
           return
        except KeyError:
            return JsonResponse({"message": "INVALID_KEY"},status=400)

        except Exception as e :
            return JsonResponse({"message": e},status=400)
    def put(self, request):
        return
    def delete(self , request):
        return
    def get(self ,request):
        # 기본값 id 순으로 출력 
        # 생성일순 으로 출력
        # 이름순으로 출력
        return

