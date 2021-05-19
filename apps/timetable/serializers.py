from rest_framework.serializers import ModelSerializer, StringRelatedField, ReadOnlyField, ValidationError
from .models import TimeTable, Entry, EntryItem


class EntryItemSerializer(ModelSerializer):
    class Meta:
        model = EntryItem
        fields = "__all__"


class EntrySerializer(ModelSerializer):
    items = EntryItemSerializer(many=True, read_only=True)
    class Meta:
        model = Entry
        fields = "__all__"
        extra_kwargs = {"user" : {"read_only" : True}}
    
    def create(self, validated_data):
        instance, created = Entry.objects.get_or_create(**validated_data)
        if not created:
            raise ValidationError("You cannot add a day twice.")
        return instance



class TimeTableSerializer(ModelSerializer):
    entries = EntrySerializer(many=True, read_only=True)
    get_time_intervals = ReadOnlyField()

    
    class Meta:
        model = TimeTable
        fields = "__all__"
        extra_kwargs = {"user" : {"read_only" : True}}


