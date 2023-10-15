from django.urls import path

from visits.views import SalePointAPIView, VisitAPIView

urlpatterns = [path("sale_point_list", SalePointAPIView.as_view()),
               path("make_visit", VisitAPIView.as_view()),
               ]