from django.urls import path
from web.views import index, doc, exercises, games, community, tools, community_post, exercise, game, tool


app_name = "web"

urlpatterns = [
    path("",index, name="index"),
    path("documentation/", doc, name="documentation"),
    path("exercises/", exercises, name="exercises"),
    path('exercises/<str:about_text>/', exercise, name='exercise'),
    path("games/", games, name="games"),
    path('games/<str:name_text>/', game, name='game'),
    path("community/", community, name="community"),
    path("tools/", tools, name="tools"),
    path('tools/<str:name_text>/', tool, name='tool'),
    path("community_post/", community_post, name="community_post")
]