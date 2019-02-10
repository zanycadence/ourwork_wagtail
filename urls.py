from django.conf.urls import url, include
from django.contrib import admin
from api.resources import MemberResource,ContractSpecResource

from views import *

member_resource = MemberResource()
contract_spec_resource	= ContractSpecResource()

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^member/', include(member_resource.urls)),
    #url(r'^member/', views.member),
    url(r'^api/member/$',views.mentor_match,name='mentor_match'),
    #url(r'^api/member/mentor_match/<zipcode>/<track>/$','mentor_match',name='urlname2')

]