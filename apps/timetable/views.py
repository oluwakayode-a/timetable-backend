from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListCreateAPIView, GenericAPIView, \
    RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import TimeTable, Entry, EntryItem
from .serializers import TimeTableSerializer, EntrySerializer, EntryItemSerializer


# Create your views here.
class TimeTableView(ModelViewSet):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer

    def list(self, request):
        timetables = TimeTable.objects.filter(user=request.user)
        data = TimeTableSerializer(timetables, many=True).data
        return Response(data)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EntryListView(ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    def get(self, request, table_id):
        entries = Entry.objects.filter(table=table_id, user=request.user)
        data = EntrySerializer(entries, many=True).data
        return Response(data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class EntryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    def get(self, request, table_id, entry_id):
        entry = get_object_or_404(Entry, user=request.user, table=table_id, id=entry_id)
        data = EntrySerializer(entry).data
        return Response(data)


class getEntry(RetrieveAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    def get(self, request, entry_day, table_id):
        entry = get_object_or_404(Entry, table=table_id, day=entry_day)
        return Response({
            "entry_id" : entry.id
        })


class EntryItemCreate(CreateAPIView):
    queryset = EntryItem.objects.all()
    serializer_class = EntryItemSerializer


class EntryItemUpdate(RetrieveUpdateDestroyAPIView):
    queryset = EntryItem.objects.all()
    serializer_class = EntryItemSerializer

    def get_object(self):
        # Get URL parameters.
        entry = int(self.kwargs["entry_id"])
        time_range = self.kwargs["time"]

        obj, created = EntryItem.objects.get_or_create(entry_id=entry, time_range=time_range)
        # obj = get_object_or_404(EntryItem, entry=entry, time_range=time_range)
        self.check_object_permissions(self.request, obj)

        return obj

