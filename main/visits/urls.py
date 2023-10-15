from django.urls import path

from visits.views import SalePointAPIView, VisitAPIView

urlpatterns = [path("api/v1/sale_point_list", SalePointAPIView.as_view()),
               path("api/v1/make_visit", VisitAPIView.as_view()),
               ]