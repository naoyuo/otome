import pygame
from os import listdir
from os.path import isfile, join

pygame.init()

font = pygame.font.Font(None,30)
player_name = 'name'
current_scene = 0

print('jivnskvpsoiv')
a = False




#Character names & images
with open('Information/characters_speak.txt', encoding='utf-8') as f:
    lines = f.read()
character_names = lines.split('\n')


mypath = 'Images/Characters'
character_list = [f for f in listdir(mypath) if isfile(join(mypath, f))]

name_to_image = {}
for name in character_names:
    for image in character_list:
        if name.replace(':','') in image:
            name_to_image[name] = image









#Backgrounds
mypath = 'Images/Backgrounds'
backgrounds_list = [f for f in listdir(mypath) if isfile(join(mypath, f))]



#Functions


class Dialogue:
    #common variables
    hi = 'yes'

    def __init__(self, path_text):
        #object variables
        self.path = path_text
        self.my_text = []
        self.current_line = 0 
        self.current_background = 0
        self.change_background = False
        self.backgrounds_ord = []
        self.backgrounds_index = []
        self.names_in_dialogue =[]
        self.lines_of_names = []
        #Usable text
        with open(self.path, encoding='utf-8') as f:
            lines = f.read()
        self.my_text = lines.split('\n')
        for l in self.my_text:
            if '' in self.my_text:
                self.my_text.remove('')
            elif ' ' in self.my_text:
                self.my_text.remove(' ')
            else:
                None
        #Background name order
        text = self.my_text
        for i in text:
            for j in backgrounds_list:
                if j in i:
                    self.backgrounds_ord.append(j)
        #Background index order
        text = self.my_text
        counter = 0
        for i in text:
            for j in backgrounds_list:
                if j in i:
                    self.backgrounds_index.append(text.index(i) - counter)
                    counter += 1



        
  
    
    def only_dialogue(self):
        text = self.my_text
        dialogue = []
        for i in text:
            for image in backgrounds_list:
                if image in text:
                    text.remove(image)
                else:
                    None
            string = i
            for j in character_names:
                if j in i:
                    string = i.replace(j, '')
            dialogue.append(string)
        return dialogue
    
    def background_now(self):
        x = self.backgrounds_index
        if self.change_background == True:
            for i in x:
                    if self.current_line == i:
                        self.current_background += 1
        self.change_background = False
    
    def print_dialogue(self):
        text = self.only_dialogue()
        line = text[self.current_line]
        #display who's talking
        whole_text = self.my_text
        whole_line = whole_text[self.current_line]
        for name in character_names:
                if name in whole_line:
                    text_showing = font.render(name,True, 'Black')
                    screen.blit(text_showing, (80, 500))
        #display dialogue in several lines
        line = line.split(' ')
        words = ''
        x = 60
        y = 540
        counter = 0
        for i in range(len(line)):
            words += line[i] + ' '
            counter += len(line[i]) + 1
            if counter > 110:
                text_showing = font.render(words,True, 'Black')
                screen.blit(text_showing, (x,y))
                x = 60
                y += 25
                counter = 0
                words = ''
        text_showing = font.render(words,True, 'Black')
        screen.blit(text_showing, (x,y))
    def show_character(self):
        whole_text = self.my_text
        whole_line = whole_text[self.current_line]
        for name in character_names:
                if name in whole_line:
                    image = name_to_image[name] 
                    character = pygame.image.load('Images/Characters/'+image)
                    character = pygame.transform.scale(character,(1366,768))
                    character_rect = character.get_rect(midbottom = (683,768))
                    screen.blit(character, character_rect) 

        






#Texts
mypath = 'Texts/'
texts_list = [f for f in listdir(mypath) if isfile(join(mypath, f))]


#Scenes objects
list_obj_scenes = []
for x in range(len(texts_list)):
    a = Dialogue('Texts/'+texts_list[x])
    list_obj_scenes.append(a)



#Window
pygame.init()
screen = pygame.display.set_mode((1366,768))



#Title
basics_txt = open('Information/basics.txt', encoding='utf-8')
basic_dic = {'name':'',
            'player_name':'',
            'state':''}

basic_dic['name'] = basics_txt.readline()
basic_dic['player_name'] = basics_txt.readline()
pygame.display.set_caption(basic_dic['name'])








#Cptions & order
mypath = 'Images/Captions'
caption_list = [f for f in listdir(mypath) if isfile(join(mypath, f))]

with open('Information/caption_order.txt', encoding='utf-8') as f:
    lines = f.read()
caption_ord = lines.split('\n')
caption_num = 0




running = True
while running:
    pygame.event.pump()
    event = pygame.event.wait()
    screen.fill('BLACK')

    if event.type == pygame.QUIT:
        running = False

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            list_obj_scenes[current_scene].current_line += 1
            list_obj_scenes[current_scene].change_background = True
            list_obj_scenes[current_scene].background_now()


            

            
    background = pygame.image.load('Images/Backgrounds/'+list_obj_scenes[current_scene].backgrounds_ord[list_obj_scenes[current_scene].current_background])  
    background = pygame.transform.scale(background,(1366,768))
    screen.blit(background,(0,0))

    list_obj_scenes[current_scene].show_character()

    caption = pygame.image.load('Images/Captions/'+caption_ord[caption_num])
    caption = pygame.transform.scale(caption,(1366,768))
    screen.blit(caption,(0,0))

    list_obj_scenes[current_scene].print_dialogue()

    pygame.display.update()