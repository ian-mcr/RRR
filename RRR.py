import pgzrun
import random
WIDTH=800
HEIGHT=800
TITLE="R.R.R"
levels=7
level=1
trash=["bottle","chips","plastic bag","battery"]
cats=[]
actors=[]
game_over=False
def draw():
    screen.blit("rbg", (0, 0))
    if game_over==False:
        for actor in actors:
            actor.draw()
    else:
        screen.draw.text("GAME OVER",(340,241),color="black",fontsize=90)

def update():
    pass
def make_actors():
    global actors 
    images=["paper"]
    actors.clear()
    for i in range(level):
        number=random.randint(0,3)
        images.append(trash[number])

    #creating actors
    for image in images:
        actor=Actor(image)
        actors.append(actor)
    #positioning the actor
    number_gappes=level+2
    size=WIDTH/number_gappes
    number=1
    random.shuffle(actors)
    for actor in actors:
        actor.pos=(size*number,50)
        number=number+1
    #animation
    for actor in actors:
        actor.anchor=("center","bottom")
        dance=animate(actor,duration=5,y=HEIGHT,on_finished=gameover)
        cats.append(dance)
def stop():
    for dance in cats:
        if dance.running:
            dance.stop()

def gameover():
    global game_over
    game_over=True

def on_mouse_down(pos):
    global level
    for actor in actors:
        if actor.collidepoint(pos):
            if actor.image in "paper":
                level=level+1
                stop()
                make_actors()
            else:
                gameover()


make_actors()
pgzrun.go()