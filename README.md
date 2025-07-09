# Foxhole - front visualisator

Foxhole is a game. People are fighting as a fraction with other fractions. The key is the communication, logistics and teamwork.

I created that visualisator just for fun. I haven't even played the game.
It has public API that provides data about current (in-game) war, and I wanted to mess around with
quick FastAPI and JS.

# Stack

The stack I used:

- FastAPI to call Foxhole API (I used it on purpose, to be able to easy save the data into db)
- Vanilla JS to simplify creating front view

# How to run it

Pls, don't :(. Knowing me, I will abandon that project. For now - it's using `python3 -m http.server 8080` to serve static frontend website.
I don't reccomend using that anywhere except for just messing around and checking how it works.


# TODOS

- add grid lines
- add segments
- add icons to objects so they would be more recognicable by players
- add automatic api shoot
- store results in mongoDB
- apply animations for latest data, so the user would instantly know how front is moving
- add some kind of control over which map we are currently looking at (I HAVE TO PLAY THE GAME FIRST :P )
- containerize whole thing
- host it

# Screenshoot

<div align="center">
    <img width=500 src=".readme/images/foxhole-screen-1.png"></img/>
</div>



