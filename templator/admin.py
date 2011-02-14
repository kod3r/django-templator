from django.contrib import admin

from templator.models import TemplateContext, Template

admin.site.register(TemplateContext)
admin.site.register(Template)
