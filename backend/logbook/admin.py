from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget  # 🧩 Step 1: Import JSON editor

from .models import (
    Uav,
    Sort,
    Malfunction,
    Permit,
    ConfigControl,
    ConfigAudit,
    Lru,
    AuditLog,
    UavVersions,
    UavWeightsControl,
    UavBalanceControl
)

# 🧩 Step 2: Custom admin class for Uav
class UavAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget}
    }

# 🧩 Step 3: Use the custom admin for Uav
admin.site.register(Uav, UavAdmin)

# Default registration for other models
admin.site.register(Sort)
admin.site.register(Malfunction)
admin.site.register(Permit)
admin.site.register(ConfigControl)
admin.site.register(ConfigAudit)
admin.site.register(Lru)
admin.site.register(AuditLog)
admin.site.register(UavVersions)
admin.site.register(UavWeightsControl)
# admin.site.register(UavBalanceControl)  # Uncomment if needed later
