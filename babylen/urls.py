"""babylen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from baby_user.views import register, login, get_user_datalist, u_user_datalist, get_baby_datalist, updata_user_pic, get_center_bonne
from baby_user.views import u_barcode_relevance_m2c, u_barcode_relevance_b2c, u_barcode_relevance_b2m, u_barcode_relevance_b2p
from baby_user.views import bonne_care_chart, add_baby_auth, get_header_pic
from babylen.views import get_main_datalist
from baby.views import cu_baby, u_baby_relevance_remove, u_baby_relevance_b2m, c_baby_picture, updata_baby_pic
from baby.views import cu_baby_record, get_baby_picture_imglist, get_baby_record_simple, get_baby_record_detail, get_baby_data
from center.views import get_center_record_simple, get_center_record_detail, c_barcode_cneter_visit
from center.views import updata_center_pic, u_center_record_detail
from notification.views import cu_notification_id, get_notification_datalist
from discuss.views import get_discuss_group_datalist, get_discuss_article_datalist, c_discuss_group, c_discuss_article, updata_discuss_pic
from produce.views import get_shop_datalist, get_shop_tradelist, c_shop_trade

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # baby_user.views
    url(r'^api/v1/register/', register),
    url(r'^api/v1/login/', login),
    url(r'^api/v1/get_baby_datalist/', get_baby_datalist),
    url(r'^api/v1/get_user_datalist/', get_user_datalist),
    url(r'^api/v1/u_user_datalist/', u_user_datalist),
    url(r'^api/v1/u_barcode_relevance_m2c/', u_barcode_relevance_m2c),
    url(r'^api/v1/u_barcode_relevance_b2c/', u_barcode_relevance_b2c),
    url(r'^api/v1/u_barcode_relevance_b2m/', u_barcode_relevance_b2m),
    url(r'^api/v1/u_barcode_relevance_b2p/', u_barcode_relevance_b2p),
    url(r'^api/v1/updata_user_pic/', updata_user_pic),
    url(r'^api/v1/get_center_bonne/', get_center_bonne),
    url(r'^api/v1/add_baby_auth/', add_baby_auth),
    url(r'^api/v1/bonne_care_chart/', bonne_care_chart),
    url(r'^api/v1/get_header_pic/', get_header_pic),
    # babylen.views
    url(r'^api/v1/get_main_datalist/', get_main_datalist),
    # baby.views
    url(r'^api/v1/cu_baby/', cu_baby),
    url(r'^api/v1/u_baby_relevance_remove/', u_baby_relevance_remove),
    url(r'^api/v1/u_baby_relevance_b2m/', u_baby_relevance_b2m),
    url(r'^api/v1/cu_baby_record/', cu_baby_record),
    url(r'^api/v1/get_baby_picture_imglist/', get_baby_picture_imglist),
    url(r'^api/v1/c_baby_picture/', c_baby_picture),
    url(r'^api/v1/get_baby_record_simple/', get_baby_record_simple),
    url(r'^api/v1/get_baby_record_detail/', get_baby_record_detail),
    url(r'^api/v1/updata_baby_pic/', updata_baby_pic),
    url(r'^api/v1/get_baby_data/', get_baby_data),
    # center.views
    url(r'^api/v1/get_center_record_simple/', get_center_record_simple),
    url(r'^api/v1/get_center_record_detail/', get_center_record_detail),
    url(r'^api/v1/c_barcode_cneter_visit/', c_barcode_cneter_visit),
    url(r'^api/v1/u_center_record_detail/', u_center_record_detail),
    url(r'^api/v1/updata_center_pic/', updata_center_pic),
    # notification.views
    url(r'^api/v1/cu_notification_id/', cu_notification_id),
    url(r'^api/v1/get_notification_datalist/', get_notification_datalist),
    # discuss.views
    url(r'^api/v1/get_discuss_group_datalist/', get_discuss_group_datalist),
    url(r'^api/v1/get_discuss_article_datalist/', get_discuss_article_datalist),
    url(r'^api/v1/c_discuss_group/', c_discuss_group),
    url(r'^api/v1/c_discuss_article/', c_discuss_article),
    url(r'^api/v1/updata_discuss_pic/', updata_discuss_pic),
    # produce.view
    url(r'^api/v1/get_shop_datalist', get_shop_datalist),
    url(r'^api/v1/get_shop_tradelist', get_shop_tradelist),
    url(r'^api/v1/c_shop_trade', c_shop_trade),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
