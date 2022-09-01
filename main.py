from tkinter import W
import pygame
import sys

# Define the class
class StoryClass:
    #option1, option2 = NULL

    def __init__(self, storyID, storyText, option1Text, option2Text, option1 = None, option2 = None) -> None:
        self.storyID = storyID
        self.storyText = storyText
        self.option1Text = option1Text
        self.option2Text = option2Text
        self.option1 = option1
        self.option2 = option2

    def getStoryText(self):
        return self.storyText

    def getOption1Text(self):
        return self.option1Text

    def getOption2Text(self):
        return self.option2Text

    def getOption1(self):
        return self.option1

    def getOption2(self):
        return self.option2

    def assignOption1(self, option1):
        self.option1 = option1

    def assignOption2(self, option2):
        self.option2 = option2

    

# Create the Story objects
s0 = StoryClass(0, "You are a high school student in Canada: Name____", None, None)
s1 = StoryClass(1, "Join in some Clubs or not", "no", "yes")
s2 = StoryClass(2, "You feel a little bit lonely because you have no friends. You start playing computer games to ease your loneliness, but you found that computer games would occupy your many time, you will:", "less game, more study", "more game")

# Link the Story objects
s0.assignOption1(s1)
s1.assignOption1(s2)
s1.assignOption2(s2)
s2.assignOption1(s1)
s2.assignOption2(s1)

# Initiate game
pygame.init()

# Set variables
screen_size = width, height = 1000, 800
screen_color = 250, 250, 242
lightblue = pygame.Color('lightskyblue3')
darkblue = pygame.Color('dodgerblue2')
defaultColor = lightblue
black_color = 0, 0, 0
font = pygame.font.Font(None, 32)
default_text = "Hello there: "
is_input = True

# Rectangle Dimensions
button1_left = width * (1/6)
button1_top = height * (1/10) + height * (2/3) + 50
button1_width = width * (1/5)
button1_height = height * (1/10)
button2_left = width * (1/6) + width * (2/3) - width * (1/5)
button2_top = height * (1/10) + height * (2/3) + 50
button2_width = width * (1/5)
button2_height = height * (1/10)

# Create Rectangles
text_box = pygame.Rect(width * (1/6), height * (2/3), width * (2/3), height * (1/10))
button1 = pygame.Rect(button1_left, button1_top, button1_width, button1_height)
button2 = pygame.Rect(button2_left, button2_top, button2_width, button2_height)
selina = pygame.image.load("Selina_cropped3.gif")
selina = pygame.transform.scale(selina, (selina.get_width()/3, selina.get_height()/3))
selinarect = selina.get_rect()

# Display screen
screen = pygame.display.set_mode(screen_size)
story = s0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN and is_input:
            if event.key == pygame.K_RETURN:
                print(default_text)
                story = story.getOption1()
                #default_text = "Hello there: "
                is_input = False
            elif event.key == pygame.K_BACKSPACE:
                default_text = default_text[:-1]
            else:
                story.storyText += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    story = story.getOption1()

                if button2.collidepoint(event.pos):
                    story = story.getOption2()

    screen.fill(screen_color)
    
    # Get mouse position
    mouse = pygame.mouse.get_pos()

    # If mouse is hovering a button, it changes colour
    if button1.collidepoint(mouse):
        defaultColor = darkblue
    elif button2.collidepoint(mouse):
        defaultColor = darkblue
    else: 
        defaultColor = lightblue

    # Draw the rectangles
    pygame.draw.rect(screen, defaultColor, text_box, 2)
    pygame.draw.rect(screen, defaultColor, button1) if story.getOption2() != None else None
    pygame.draw.rect(screen, defaultColor, button2) if story.getOption2() != None else None
    screen.blit(selina, selinarect)

    # Render the text in the rectangles and center the text for buttons
    text_box_txt = font.render(story.getStoryText(), True, defaultColor)
    button1_txt = font.render(story.getOption1Text(), True, black_color)
    button2_txt = font.render(story.getOption2Text(), True, black_color)

    button1_txt_rect = button1_txt.get_rect(center=(button1.left+button1.width/2, button1.top+button1.height/2))
    button2_txt_rect = button2_txt.get_rect(center=(button2.left+button2.width/2, button2.top+button2.height/2))

    screen.blit(text_box_txt, (text_box.x+5, text_box.y+5))
    screen.blit(button1_txt, button1_txt_rect) if story.getOption2() != None else None  # If Option2 is None, then do not display the buttons. This occurs for leaf node stories
    screen.blit(button2_txt, button2_txt_rect) if story.getOption2() != None else None
    # Display the changes
    pygame.display.flip()