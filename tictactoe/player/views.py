from django.shortcuts import render

from gameplay.models import Game


## this will render html
def home(request):
    #return render(request,"player/home.html",{
    #    'ngames':Game.objects.count()
    #})
    ## the request objects we pass has a user attribute
    ## that checks what user is current logged in
    
    ## this will fetch all the logged user who started the game
    # game_first_player = Game.objects.filter(
    #     first_player=request.user,
    #     status='F'
    # )

    # ## this will return all the second player who started the game
    # game_second_player = Game.objects.filter(
    #     second_player = request.user,
    #     status='S'
    # )

    # ## this will return all the first and second player
    # ## list
    # all_games = list(game_first_player) + list(game_second_player)
    # print(all_games)

    # return render(request,"player/home.html",{
    #     "game":all_games
    # })

    ## django already made avilabe the user directly in the template

    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()
    return render(request,"player/home.html",{
         "game":active_games
     })
