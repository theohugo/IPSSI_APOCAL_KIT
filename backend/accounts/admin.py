"""Admin Django.

Le modèle User par défaut suffit (pas de modèle custom). On expose en revanche
les objets RGPD (J3-bis) en LECTURE SEULE : ce sont des traces réglementaires
qu'un admin consulte mais ne doit pas éditer à la main.
"""

from django.contrib import admin

from .models import AuditEvent, DataRequest


@admin.register(DataRequest)
class DataRequestAdmin(admin.ModelAdmin):
    list_display = ("requester", "status", "requested_format", "requested_at", "responded_at")
    list_filter = ("status", "requested_format")
    search_fields = ("requester__email", "requester__username", "export_sha256")
    readonly_fields = tuple(f.name for f in DataRequest._meta.fields)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(AuditEvent)
class AuditEventAdmin(admin.ModelAdmin):
    list_display = ("user", "event_type", "message", "created_at")
    list_filter = ("event_type",)
    search_fields = ("user__email", "user__username", "message")
    readonly_fields = tuple(f.name for f in AuditEvent._meta.fields)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
