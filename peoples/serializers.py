from rest_framework import serializers
from peoples.models import People
from peoples.models import Team

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    #team = serializers.SlugRelatedField(queryset=Team.objects.all(),
    #slug_field='name')

    class Meta:
        model = Team
        fields = (
            'id',
            'name'
        )
        

class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = People
        fields = (
            'id',
            'name',
            'email',
            'number')