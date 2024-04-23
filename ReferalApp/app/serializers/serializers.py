from rest_framework import serializers
from ..models.invite_cods import BindingInvite

class BindingInviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BindingInvite
        fields = ['telephone']