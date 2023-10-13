import sys
from io import BytesIO
import os
import pygame
from random import randint
import base64
from pic2str import *
image_datas = []
byte_data = base64.b64decode(aa)
image_datas.append(BytesIO(byte_data))
byte_data = base64.b64decode(aaa)
image_datas.append(BytesIO(byte_data))
byte_data = base64.b64decode(aaaa)
image_datas.append(BytesIO(byte_data))
byte_data = base64.b64decode(aaaaa)
image_datas.append(BytesIO(byte_data))
byte_data = base64.b64decode(aaaaaa)
image_datas.append(BytesIO(byte_data))
byte_data = base64.b64decode(aaaaaaa)
image_datas.append(BytesIO(byte_data))
byte_data = base64.b64decode(aaaaaaaa)
image_datas.append(BytesIO(byte_data))
byte_data = base64.b64decode(aaaaaaaaa)
image_datas.append(BytesIO(byte_data))
byte_data = base64.b64decode(aaaaaaaaaa)
image_datas.append(BytesIO(byte_data))
byte_data = base64.b64decode(aaaaaaaaaa)
image_datas.append(BytesIO(byte_data))
byte_data = base64.b64decode(aaaaaaaaaaa)
image_datas.append(BytesIO(byte_data))
byte_data = base64.b64decode(aaaaaaaaaaaa)
image_datas.append(BytesIO(byte_data))
PERSON0 = pygame.image.load(image_datas[2])
PERSON1 = pygame.image.load(image_datas[3])
PERSON2 = pygame.image.load(image_datas[4])
PERSON3 = pygame.image.load(image_datas[5])
PERSON4 = pygame.image.load(image_datas[6])
PERSON5 = pygame.image.load(image_datas[7])
PERSON6 = pygame.image.load(image_datas[8])
PERSON7 = pygame.image.load(image_datas[9])
images = [PERSON0, PERSON1, PERSON2, PERSON3, PERSON4, PERSON5, PERSON6, PERSON7]
a_file = image_datas[11]
word_list = []
userGuesses = []
badGuesses = []
for line in a_file:
    stripped_line = line.strip()
    word_list.append(stripped_line)
pygame.init()
FONT = pygame.font.SysFont("timesnewroman", 25)
WORD_TEXT = pygame.font.SysFont("timesnewroman", 15)
WINNER_FONT = pygame.font.SysFont('timesnewroman', 100)
NEXT_GAME_FONT = pygame.font.SysFont('timesnewroman', 15)
pygame.display.set_caption("Hangman")
os.chdir(os.path.join(os.path.dirname(__file__), "Assets"))
PATH = os.getcwd()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND = pygame.transform.scale(pygame.image.load(image_datas[1]), (WIDTH//2, HEIGHT))
lives = 7
NEXT_GAME = "Thank you for playing. In 10 seconds the game will restart click the x icon on the window to close out of the game!"
class Underscore:
    def __init__(self, arr):
        self.arr = arr
    def word_with_space(self):
        return ' '.join(map(str, self.arr))
    def word_without_space(self):
        return ''.join(map(str, self.arr))
    def set_char(self, index: int, char: str):
        self.arr[index] = char
    def change(self, word: str):
        self.arr = list(word)

def choose_word():
    return word_list[randint(0, len(word_list) -1)].decode("utf-8")

def underscore(word: str):
    word_unguessed = []
    word_array = list(word)
    for i in range(len(word_array)):
        word_unguessed.append("_")
    return word_unguessed

def checker(guess: str, lives: int, word: int, unguessedWord: str):
    found = False
    if guess == "+": 
        unguessedWord.change(word)
        return lives
    word_list = list(word)
    for i in range(len(word_list)):
        if guess == word_list[i]:
            unguessedWord.set_char(i, guess)
            found = True
    if found:
        return lives
    else:
        badGuesses.append(guess)
        return lives - 1
def badGuessString(g: list):
    final = "Incorrect Guesses: "
    for i in range(len(g)):
        if i != len(g) - 1:
            final += g[i] + ", "
        else:
            final += g[i]
    return final
def draw_window(unguessed_word: str, user_text: str, lives: int, end: bool, winner_text: str, word: str):
    if end:
        WIN.fill(BLACK)
        end_game_text = WINNER_FONT.render(winner_text, 1, WHITE)
        next_game_text = NEXT_GAME_FONT.render(NEXT_GAME, 1, WHITE)
        word_text = NEXT_GAME_FONT.render(word, 1, WHITE)
        WIN.blit(word_text, (WIDTH//2 - next_game_text.get_width()/2, HEIGHT//2 + next_game_text.get_height()/2 + end_game_text.get_height() + word_text.get_height()))
        WIN.blit(end_game_text, (WIDTH//2 - end_game_text.get_width()/2, HEIGHT//2 - end_game_text.get_height()/2))
        WIN.blit(next_game_text, (WIDTH//2 - next_game_text.get_width()/2, HEIGHT//2 + next_game_text.get_height()/2 + end_game_text.get_height()))
        pygame.display.update()
        pygame.time.delay(10000)
        userGuesses.clear()
        badGuesses.clear()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        return
    WIN.fill(BLACK)
    WIN.blit(BACKGROUND, (WIDTH//2, 0))
    WIN.blit(images[7-lives],(WIDTH//2, 0))
    lives_text = FONT.render("Lives: " + str(lives), 1, WHITE)
    underscoreText = WORD_TEXT.render(unguessed_word.word_with_space(), 1, WHITE)
    text_surface = WORD_TEXT.render(user_text, 1, WHITE)
    badUserGuesses = WORD_TEXT.render(badGuessString(badGuesses), 1, WHITE)
    WIN.blit(text_surface, (0, 50))
    WIN.blit(lives_text, (0, 0))
    WIN.blit(underscoreText,(0, 30))
    WIN.blit(badUserGuesses,(0, 80))
    pygame.display.update()
def main():
    clock = pygame.time.Clock()
    run = True
    word = choose_word()
    unguessedWord = Underscore(underscore(word))
    user_text = ''
    lives = 7
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if (not (user_text.lower() in userGuesses)):
                        lives = checker(user_text.lower(), lives, word, unguessedWord)
                        userGuesses.append(user_text)
                        user_text = ''
                else:
                    if (not (len(user_text) == 1)):
                        user_text += event.unicode
        winner_text = ''
        end = False
        word_text = "Your word was " + word
        if list(word) == unguessedWord.arr:
            winner_text = "You won good job!"
            end = True
            draw_window(unguessedWord, user_text.lower(), lives, end, winner_text, word_text)
            break
        if lives == 0:
            winner_text = "Sadly you have lost."
            end = True
            draw_window(unguessedWord, user_text.lower(), lives, end, winner_text, word_text)
            break
        draw_window(unguessedWord, user_text.lower(), lives, end, winner_text, word_text)
    main()
if __name__ == "__main__":
    main()
