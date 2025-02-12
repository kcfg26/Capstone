from django.contrib import admin
from .models import Equipment, BorrowRecord, OverdueRecord, AuditLog

admin.site.register(Equipment)
admin.site.register(BorrowRecord)
admin.site.register(OverdueRecord)
admin.site.register(AuditLog)
