from django.urls import path, include
from .views import TimeTableView, EntryListView, EntryDetailView, \
    EntryItemCreate, EntryItemUpdate, getEntry
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", TimeTableView)


urlpatterns = [
    path("", include(router.urls)),
    path("<int:table_id>/entries/", EntryListView.as_view()),
    path("<int:table_id>/entries/<int:entry_id>/", EntryDetailView.as_view()),
    path("<int:table_id>/get/<str:entry_day>/", getEntry.as_view()),
    path("entry_item/create/", EntryItemCreate.as_view()),
    path("entry_item/<int:entry_id>/<str:time>/", EntryItemUpdate.as_view()),
]