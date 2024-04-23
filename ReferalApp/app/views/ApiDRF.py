from rest_framework import generics
from ..models.invite_cods import BindingInvite
from ..serializers.serializers import BindingInviteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class BindingInviteListView(generics.ListAPIView):
    serializer_class = BindingInviteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        invite_cod = self.request.query_params.get('invite_cod')
        queryset = BindingInvite.objects.filter(invite_cod=invite_cod)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)