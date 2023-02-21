from django.contrib import admin
from .models import\
    MusicianPerformer, Album, Song, AlbumSong


@admin.register(MusicianPerformer)
class MPAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('is_active',)
    ordering = ('-created_at',)
    list_display = (
        'name',
        'updated_at',
        'created_at',
        'is_active',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id'
    )


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('is_active',)
    ordering = ('-created_at',)
    list_display = (
        'name',
        'year_of_issue',
        'musician_performer',
        'updated_at',
        'created_at',
        'is_active',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id'
    )


@admin.register(AlbumSong)
class AlbumSong(admin.ModelAdmin):
    search_fields = ('song',)
    list_filter = ('is_active',)
    ordering = ('-created_at',)
    list_display = (
        'song',
        'album',
        'position',
        'updated_at',
        'created_at',
        'is_active',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id'
    )


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('is_active',)
    ordering = ('-created_at',)
    list_display = (
        'name',
        'updated_at',
        'created_at',
        'is_active',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id'
    )
