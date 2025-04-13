from django.contrib import admin
from django import forms
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
import json

# Custom ModelForm for Uav to handle JSON safely
class UavAdminForm(forms.ModelForm):
    class Meta:
        model = Uav
        fields = '__all__'

    def clean_lru_items(self):
        data = self.cleaned_data.get('lru_items')
        if isinstance(data, str):
            try:
                return json.loads(data)
            except json.JSONDecodeError:
                raise forms.ValidationError("Invalid JSON format.")
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'lru_items' in self.initial and isinstance(self.initial['lru_items'], dict):
            self.initial['lru_items'] = json.dumps(self.initial['lru_items'], indent=2)

class UavAdmin(admin.ModelAdmin):
    form = UavAdminForm

admin.site.register(Uav, UavAdmin)
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
