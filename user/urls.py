from django.urls import include, path
from rest_framework import routers
from .views import ListEducation, ListDetails, EducationViewset, DetailsViewset

router = routers.DefaultRouter()
router.register('education', EducationViewset, basename='education')
router.register('details', DetailsViewset, basename='details' )

urlpatterns = [
    path('', include(router.urls)),
    path('education-list/', ListEducation.as_view(), name='list-education'),
    path('details-list/', ListDetails.as_view(), name='list-details'),
]