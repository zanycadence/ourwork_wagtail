from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from api.models import Member
from api.models import ContractSpec


class MemberResource(ModelResource):
    class Meta:
        queryset = Member.objects.all()
        resource_name = 'member'
        authorization = Authorization()

        #fields=['location','track']
       # filtering = {
        #    "location": ALL,
         #   "location": ALL_WITH_RELATIONS
        #}


class ContractSpecResource(ModelResource):
    class Meta:
        queryset = ContractSpec.objects.all()
        resource_name = 'contract'
        
        authorization = Authorization()

