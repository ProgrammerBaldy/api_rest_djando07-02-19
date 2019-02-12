from django.conf.urls import url, include
from django.urls import path  
from valores_banco.models import valorModel, newsModel
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class valorModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = valorModel
        fields = ('valor_banco_brasil', 'valor_banco_bradesco')

class newsModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = newsModel
        fields = ('title', 'text', 'date')
# ViewSets define the view behavior.
class valorModelViewSet(viewsets.ModelViewSet):
    queryset = valorModel.objects.all()
    serializer_class = valorModelSerializer

class newsModelViewSet(viewsets.ModelViewSet):
    queryset = newsModel.objects.all()
    serializer_class = newsModelSerializer
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'valor', valorModelViewSet)
router.register(r'news', newsModelViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
