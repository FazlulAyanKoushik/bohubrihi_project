from .models import Status
from .serializers import StatusSerializer
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from .pagination import MypageNumberPagination


# Create your views here.

'''
    The way no 1 for (List and Create)
'''
# class StatusAPIView(APIView):
#     def get(self, request, format=None):
#         status_list = Status.objects.all()
#         status_serializer = StatusSerializer(status_list, many=True)
#         return Response(status_serializer.data)

# class StatusListAPIView(generics.ListAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
    
# class StatusCreateAPIView(generics.CreateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer



'''
    The way no 2 for (List and Create)
'''
# class StatusListCreateView(generics.ListAPIView, mixins.CreateModelMixin):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     pagination_class = MypageNumberPagination
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



'''
    The way no 3 for (List and Create)
'''
class StatusListCreateView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer



'''
    The way no 1 for (Retrive, Update and Delete)
'''
# class StatusUpdateAPIView(generics.UpdateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = "id"
    
# class StatusDeleteAPIView(generics.DestroyAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = "id"



'''
    The way no 2 for (Retrive, Update and Delete)
'''
# class StatusDetailAPIView(generics.RetrieveAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = "id"
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
'''    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('id')
    #     return Status.objects.get(id=kw_id)'''
    
    

'''
    The way no 3 for (Retrive, Update and Delete)
'''
class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"