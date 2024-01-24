from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Booking, Contact, Manzillar, TurPaketlar, PriceIncludesInlines, PriceExludesInlines, TurImagesInlines

class PriceIncludesInline(admin.TabularInline):
    model = PriceIncludesInlines
    extra = 1

class PriceExcludesInline(admin.TabularInline):
    model = PriceExludesInlines
    extra = 1

class TurImagesInline(admin.TabularInline):
    model = TurImagesInlines
    extra = 1

@admin.register(Manzillar)
class ManzillarAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'image',)
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}
    # inlines = [PriceIncludesInline, PriceExcludesInline, TurImagesInline]
    fields = ('title', 'image', 'slug')


@admin.register(TurPaketlar)
class TurPaketlarAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'image', 'price', 'location',)
    list_display_links = ('indented_title',)
    inlines = [PriceIncludesInline, PriceExcludesInline, TurImagesInline]
    prepopulated_fields = {'slug': ('title',)}

    fields = ('title', 'slug', 'image', 'price', 'location', 'kuni', 'desc')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'date', 'tour')
    list_filter = ('date', 'tour')
    search_fields = ('full_name', 'email', 'phone')
    date_hierarchy = 'date'
    ordering = ('-date',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'mavzu', 'comment')
    search_fields = ('full_name', 'email', 'phone', 'mavzu', 'comment')
    list_filter = ('mavzu',)

    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'email', 'phone'),
        }),
        ('Additional Information', {
            'fields': ('mavzu', 'comment'),
        }),
    )
