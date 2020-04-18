from rest_framework import generics
from ..models import Subject
from .serializers import SubjectSerializer

class testSequenceListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = testSequenceSerializer

class testSequenceView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = testSequenceSerializer

class productView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = productSerializer

class productView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = productSerializer

class performancedataListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = performancedataSerializer

class performancedataView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = performancedataSerializer

class testStandardListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = testStandardSerializer

class testStandardView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = testStandardSerializer

class serviceListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = serviceSerializer

class serviceView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = serviceSerializer

class clientListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = clientSerializer

class clientView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = clientSerializer

class locationListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = locationSerializer

class locationView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = locationSerializer

class userListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = userSerializer

class userView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = userSerializer

class certificateListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = certificateSerializer

class certificateView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = certificateSerializer
