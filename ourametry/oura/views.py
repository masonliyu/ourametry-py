from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets

from ourametry.quickstart.serializers import GroupSerializer

from django.conf import settings

class OuraViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    token = settings.OURA_PERSONAL_ACCESS_TOKEN
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
