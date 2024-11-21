# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lou", who_color="#a38a71", image="lou")
define m = Character("Morale", who_color="#e6c0a8", image="morale")

# The game starts here.

label start:

    scene bg meadow

    "Wow, a lovely day. I'm the narrator. "

    show lou at center
    with easeinbottom

    l "Howdy there! I'm Lou! The best owl husband"

    show lou sad at center

    l "Holy shit I wish I had a cool wife"

    show lou at right
    with ease

    pause 0.2

    show morale at left
    with easeinleft

    m "Well would you look at that, a fuckin' owl"
    pause 1.0

    show morale inquisitive
    m "Hey, what are you all about?"

    pause 0.2
    m "..."
    pause 1.0

    show morale blush
    m "You're some hot shit, gamer boi"
    show morale inquisitive
    m "Looking to have a nice, friendly date? Maybe with flowers?"

    menu: 
        "Woah. Oh hellyeah":
            jump hellyeah
        
        "Oh... well, fuckin' absolutely let's do it":
            jump wellfuckinabsolutelyletsdoit

label hellyeah:
    l "..."
    pause 1.0
    
    show lou blush
    l "...ye ://3"

    show morale sunglasses
    m "... Nice B)"
    jump date

label wellfuckinabsolutelyletsdoit:
    l "..."
    pause 0.5
    l "..."
    pause 1.0
    l "FUCK YES LET'S DO IT GAMER ABSOLUTELY"

    show morale letsfuckinggo
    m "LET'S FUCKING GOOO"
    jump date

label date:

    hide lou
    with easeoutright

    hide morale
    with easeoutleft

    "And then they had a date :)"