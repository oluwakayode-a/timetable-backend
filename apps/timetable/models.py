from django.db import models
from apps.users.models import User
from apps.utils.models import Timestamp
from datetime import timedelta, datetime, date

# Create your models here.
class TimeTable(Timestamp, models.Model):
    title = models.CharField(max_length=255)
    start_time = models.TimeField()
    interval = models.CharField(max_length=10, help_text="Divided time by minutes.")
    table_length = models.CharField(max_length=10, help_text="How many rows?")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    @property
    def get_time_intervals(self):
        time_ranges = []
        for i in range(int(self.table_length)):
            self.start_time = (
                datetime.combine(date(1,1,1), self.start_time) + timedelta(minutes=int(self.interval))).time()
            time_ranges.append(self.start_time.strftime("%H:%M"))
        return time_ranges


class Entry(Timestamp, models.Model):
    day = models.CharField(max_length=100)
    table = models.ForeignKey(TimeTable, on_delete=models.CASCADE, related_name="entries")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.day} ({self.table})"
    
    class Meta:
        verbose_name_plural = "Entries"

class EntryItem(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="items")
    time_range = models.CharField(max_length=20, help_text="3.00 - 4.00")
    activity = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}"

