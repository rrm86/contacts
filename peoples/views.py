from peoples.models import People
from peoples.models import Team
from peoples.serializers import TeamSerializer
from peoples.serializers import PeopleSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

class PeopleList(generics.ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class =  PeopleSerializer
    name = 'people-list'

class PeopleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = People.objects.all()
    serializer_class =  PeopleSerializer
    name = 'people-detail'

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class =  TeamSerializer
    name = 'team-list'

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class =  TeamSerializer
    name = 'team-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'peoples': reverse(PeopleList.name, request=request),
            'teams': reverse(TeamList.name, request=request)
        })
