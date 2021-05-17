from django.urls import path , include

urlpatterns = [
    # 로그인 / 회원가입
    path('users/', include("user.urls")),
    # 상품
    path('product',include("product.urls")),
    # 폴더
    path('folder',include("folder.urls")),
    # 삭제된 문서
]
