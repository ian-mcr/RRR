import pgzrun
import random
WIDTH=800
HEIGHT=800
TITLE="R.R.R"
levels=7
level=1
trash=["bottle","chips","plastic bag","battery"]
actors=[]
def draw():
    screen.blit("rbg", (0, 0))
    for actor in actors:
        actor.draw()
def update():
    pass
def make_actors():
    global actors 
    images=["paper"]
    for i in range(level):
        number=random.randint(0,3)
        images.append(trash[number])

    #creating actors
    for image in images:
        actor=Actor(image)
        actors.append(actor)
        
make_actors()
pgzrun.go()