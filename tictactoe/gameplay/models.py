from django.db import models
from django.contrib.auth.models import User



## this is the first table

## we change the default admin view
## for the game staus stored in the database
## and to make it you 
## must follow this 
GAME_STATUS_CHOICES = (
    ('F','First Player To Move'),
    ('S','Second Player To Move'),
    ('W','First Player Win'),
    ('L','Second Player Win'),
    ('D','Draw'),


)







class Game(models.Model):

    ## now remember this foreign key in django is 
    ## by default a one to many relationship
    # so the first player can be anyone from the User class
    ## and so does the second player
    ## so the related name is the user foreign key table name
    # in the Game table willb e the related_name 


    first_player = models.ForeignKey(User,related_name='games_first_player',on_delete=models.CASCADE)
    second_player = models.ForeignKey(User,related_name='games_second_player',on_delete=models.CASCADE)

    ## now we add the starting and ending time of the game 
    ## in the database


    ## the time can be automatically add
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)

    ## now if you add a new column after a migration
    ## it will give you problem
    ## because the database can have existing data
    ## and when you add another column 
    ## djnago ask you that what value in default they
    ## and because this column add a empty row in the prevous
    ## filled data
    ## and python dont add numm value in the database
    ## its non nullable
    ## so you need to provide a default data
    status = models.CharField(max_length=1,default='F',choices=GAME_STATUS_CHOICES)


    def __str__(self):
        return "{} vs {}".format(self.first_player,self.second_player)






class Move(models.Model):


    ## this is the coordinate 
    ## of the tictac toe game
    x = models.IntegerField()
    y = models.IntegerField()


    ## this is the comment when they play the game
    comment = models.CharField(max_length=300,blank=True)
    #who started the game
    ## this will be boolian value
    by_first_player = models.BooleanField()
    ## so the move table is the game activity table
    ## and we will add all the information of the Game player in this
    ## activity table
    ## this is many to one relationship
    ## because many pair of user can be in the game
    game = models.ForeignKey(Game,on_delete=models.CASCADE)



