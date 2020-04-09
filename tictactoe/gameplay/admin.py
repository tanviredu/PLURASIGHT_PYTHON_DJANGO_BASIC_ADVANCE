from django.contrib import admin
from .models import Game,Move
# Register your models here.

# admin.site.register(Game)
# admin.site.register(Move)



## this will change the default view of admin for game
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    ## here we will show how this data will be displayed
    list_display  = ('id','first_player','second_player','status')
    ## you must give the comma
    list_editable = ('status',)

admin.site.register(Move)