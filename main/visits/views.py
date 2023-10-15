from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView

from visits.models import SalePoint, Visit, Worker


def authorize(phone):
    # Checking the correctness of the specified phone number for authorization
    if not phone:
        ok = False
        response = Response(data="The request does not specify a phone number",
                            status=status.HTTP_401_UNAUTHORIZED)
        worker = None
        return ok, response, worker

    try:
        worker = Worker.objects.get(phone=phone)
        ok = True
        response = None
    except Worker.DoesNotExist:
        ok = False
        worker = None
        response = Response(data="The worker with the specified number was not found",
                            status=status.HTTP_401_UNAUTHORIZED)
    return ok, response, worker


class SalePointAPIView(APIView):
    def get(self, request):
        phone = request.GET.get("phone", None)
        ok, response, worker = authorize(phone)
        if not ok:
            return response

        points = list(worker.sale_points.all().values())
        return JsonResponse(points, safe=False, json_dumps_params={'ensure_ascii': False})


class VisitAPIView(APIView):
    def post(self, request):

        # phone check
        phone = request.data.get("phone", None)
        ok, response, worker = authorize(phone)
        if not ok:
            return response

        # sale_point check
        sale_point_pk = request.data.get("sale_point_pk", None)
        if not sale_point_pk:
            return Response(data="The request does not specify a sale point pk",
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            sale_point = SalePoint.objects.get(pk=sale_point_pk)
        except:
            return Response(data="Sale point with the specified sale point pk was not found",
                            status=status.HTTP_400_BAD_REQUEST)

        filtered_workers_query_set = sale_point.workers.filter(id=worker.id)

        if len(filtered_workers_query_set) == 0:
            return Response(data="Sale point with the specified sale point pk was not found",
                            status=status.HTTP_400_BAD_REQUEST)

        latitude = request.data.get("latitude", None)
        longitude = request.data.get("longitude", None)
        if not (latitude and longitude):
            return Response(data="Longitude or latitude were not specified",
                            status=status.HTTP_400_BAD_REQUEST)

        visit = Visit.objects.create(sale_point_id=sale_point.id,
                                     latitude=latitude,
                                     longitude=longitude)

        return Response({"visit_pk": visit.pk, "datetime": visit.datetime}, status=HTTP_201_CREATED)
