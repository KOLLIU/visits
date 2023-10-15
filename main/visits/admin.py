from django.contrib import admin

from .models import Worker, SalePoint, Visit

admin.site.disable_action('delete_selected')


# Register your models here.
@admin.register(Worker)
class AdminWorker(admin.ModelAdmin):
    list_display = ("name", "phone")
    search_fields = ("name",)

    actions = ["delete_selected"]


@admin.register(SalePoint)
class AdminSalePoint(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)

    actions = ["delete_selected"]


@admin.register(Visit)
class AdminVisit(admin.ModelAdmin):
    list_display = ("sale_point", "datetime", "latitude", "longitude")
    search_fields = ("sale_point")

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(AdminVisit, self).changeform_view(request, object_id, extra_context=extra_context)
