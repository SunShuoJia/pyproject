from django.contrib import admin
from .models import *
# Register your models here.
class PersonInfo(admin.TabularInline):
    model = Person
    extra = 3

class HomeAdmin(admin.ModelAdmin):
    inlines = [PersonInfo]

# 针对于人的站点管理类
class PersonAdmin(admin.ModelAdmin):
    def get_oldmen(self):
        if self.age >= 18:
            return '精英'
        else:
            return '太嫩'
    get_oldmen.short_description = '是否精英'
    # 设置显示字段
    list_display = ['name','age',get_oldmen]
    # 添加过滤条件
    list_filter = ['name']
    # 条件搜索
    search_fields = ['name']
    # 分页
    list_per_page = 10
    # 根据字段排序
    ordering = ['age']
    # 分组显示
    fieldsets = [
        ('人的名字',{'fields':('name',)}),
        ('人的年龄', {'fields': ('age',)})
    ]
admin.site.register(Person,PersonAdmin)
admin.site.register(Home,HomeAdmin)