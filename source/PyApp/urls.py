from django.conf.urls import include, url
from django.contrib import admin

urlpatterns=[
 		url(r'^register/$', 'PyApp.views.registration', name='registration'),	
        url(r"^image-posts/$",'PyApp.views.image_posts',name='image_posts'),
        url(r"^auth-users/$","PyApp.views.auth_users",name="auth_users"),
        url(r"^order-by-firstname/$","PyApp.views.order_by_firstname",name="order_by_firstname"),
        url(r"^image-posts/new/$","PyApp.views.post_a_new_image",name='post_a_new_image'),
        url(r"^success/$","PyApp.views.success",name='success'),
        url(r"^error/$","PyApp.views.error",name='error'),
        url(r"^login/$","PyApp.views.login",name='login'),
    ] 
