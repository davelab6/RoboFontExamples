from mojo.drawingTools import *
from mojo.events import addObserver

class DrawTest:
    def __init__(self):
        ## add an observer for the draw event
        addObserver(self, "drawSomething", "draw")

    def drawSomething(self, info):
        ## draw something the glyph view
        rect(100, 100, 100, 100)

DrawTest()