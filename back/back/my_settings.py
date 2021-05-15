DATABASES = {
    'default' : {
        'ENGINE'   : 'django.db.backends.mysql',
        'HOST'     : 'localhost',
        'NAME'     : 'slid_clone',
        'USER'     : 'root',
        'PASSWORD' : '##tkakrnl12',
        'PORT'     : '3306',
        'TEST'     :
            {
                'CHARSET'   : 'utfmb4',
                'COLLATION' : 'utf8mb4_general_ci',
            }
    }
}


SECRET_KEY = {
    'secret' :'!1x9$j8w*voo6v#+79rmow$+v=-w!diymd-63ooe_wjj_)4yw7',
}
algorithm = 'HS256'




