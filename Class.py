import random
import pygame


class interactiveobject:
    def __init__(self, image, posx, posy, display, *selected):
        self.image = pygame.image.load(image + ".png")
        self.path = image
        self.posx = posx
        self.posy = posy
        self.display = display
        self.rect = pygame.Rect((self.posx, self.posy), (self.image.get_width(), self.image.get_height()))
        self.selected = selected

    def draw(self):
        self.display.blit(self.image, (self.posx, self.posy))


class Deck:
    def __init__(self):

        suits = ["clubs", "spades", "hearts", "diamonds"]
        self.deck = []
        self.removedCards = []

        for x in range(0, 4):
            for y in range(1, 14):

                if y == 1:
                    card = "ace_" + suits[x]
                elif y == 11:
                    card = "jack_" + suits[x]
                elif y == 12:
                    card = "queen_" + suits[x]
                elif y == 13:
                    card = "king_" + suits[x]
                else:
                    card = str(y) + "_" + suits[x]

                self.deck.append(card)

    def printCards(self):
        print(self.deck)

    def randomCard(self):
        if len(self.deck) > 5:
            card = random.randint(0, len(self.deck) - 1)
            print(card)
            returnvar = self.deck[card]
            del self.deck[card]
            self.removedCards.append(card)
            return returnvar
        else:
            print("There are no more cards in the deck")


class card(interactiveobject): # inherit from interactive object

    def select(self): # define how a selected card would look, called when it is clicked on
        if self.selected == False: #checks to see if the card is selected
            self.image = pygame.image.load(self.path + "_white.png") # if the card is not selected then it
            #will graphically display it as a selected card
            self.selected = True # changes it to selected
        else:
            self.image = pygame.image.load(self.path + ".png") #does the opposite
            self.selected = False

    def checkSelect(self): #getters to obtain information
        return self.selected

    def getPosx(self):
        return self.posx

    def getPosy(self):
        return self.posy

    def event_handler(self, event): # event handler
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.select()


class button(interactiveobject): # inherits attributes from interactive object
    def event_handler(self, event, function): # defines handler to detect interatctions
        if event.type == pygame.MOUSEBUTTONDOWN: # checks to see for any and all clicks
            if event.button == 1: # checks to see if it is a left click
                if self.rect.collidepoint(event.pos): # checks if the click is on the button
                    function() # runs a function


class money:
    def __init__(self, cash):
        self.cash = cash

    def increase(self, amount):
        self.cash += amount

    def decrease(self, amount):
        self.cash -= amount

    def display(self, xpos, ypos, text, font, size):
        font = pygame.font.Font(font, size)
        text = font.render(text, True, )


class player(money, Deck):
    def __init__(self, cash, display, path):
        self.diction = {}
        self.cash = cash
        self.display = display
        self.path = path
        money.__init__(self, self.cash)
        Deck.__init__(self)

    def newhand(self):
        done = True
        while done:
            if len(self.diction) == 0:
                positions = [(320, 540), (480, 540), (640, 540), (800, 540), (960, 540)]
                for x in range(0, 5):
                    self.diction["card{0}".format(x)] = card(self.path + self.randomCard(), positions[x][0],
                                                             positions[x][1], self.display, False)
                done = False
            else:
                self.diction.clear()

    def drawhand(self):
        for x in self.diction:
            self.diction[x].draw()

    def event_handler(self, event):
        for x in self.diction:
            self.diction[x].event_handler(event)

    def drawcards(self):
        for x in self.diction:
            if self.diction[x].checkSelect() == True:
                self.diction[x] = card(self.path + self.randomCard(), self.diction[x].getPosx(),
                                       self.diction[x].getPosy(), self.display, False)