from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self,request, format=None):
        api_view = [
            'Uses HTTP methods as functions',
            'Is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'Is mapped to manually to URLs'
        ]
        return Response({'message': 'Hello', 'api_view': api_view})
# Create your views here.
