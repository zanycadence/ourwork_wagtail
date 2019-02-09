from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from api.models import Member
from api.models import ContractSpec


class MemberResource(ModelResource):
    class Meta:
        queryset = Member.objects.all()
        resource_name = 'member'
        
        authorization = Authorization()

class ContractSpecResource(ModelResource):
    class Meta:
        queryset = ContractSpec.objects.all()
        resource_name = 'contract'
        
        authorization = Authorization()

