# ------
# Imports
# ------
import numpy as np
import pygame
import random
import sys
from pygame import mixer

# initializes pygame
pygame.init()
mixer.pre_init(44100, -16, 2, 512)

# ------
# Globals
# ------
row = "1"
col = "1"
player = 1
player_1 = ""
player_2 = ""
game_is_over = False
game_start = False
winner = 0
turn = 1
valid = False
alone = 0
running = True
title_screen = True
option_menu = False
difficulty = 0

# ----------
# CONSTANTS
# ----------
width = 800
height = width
line_width = 10
board_rows = 3
board_columns: int = 3
square_size = width // board_columns
circle_radius = square_size // 3
circle_width = 15
cross_width = 25
space = square_size // 4
# ------ COLORS ------
line_color = (23, 155, 150)
bg_color = (28, 170, 156)
circle_color = (240, 230, 203)
cross_color = (10, 30, 40)
bg_color_2 = (28, 170, 156)
white = (255, 255, 255)
black = (0, 0, 0)
color = ""
color_rect_active = pygame.Color("white")
color_rect_passive = pygame.Color("gray15")
color_rect_active_inside = (20, 165, 160)
color_rect_passive_inside = bg_color_2
color_rect_inside = color_rect_passive_inside
color_rect = color_rect_passive
color_submit = (108, 200, 186)
color_title_passive = bg_color_2
color_title_active = (20, 165, 160)
color_title = color_title_passive
transparent = (0, 0, 0, 0)

# ----- FONT -----
font_name = "timesnewromanitalic"
font_name_exodus_sharpen = "Interface/Exodus - Personal Use/ExodusDemo-Sharpen.otf"
font_name_exodus_striped = "Interface/Exodus - Personal Use/ExodusDemo-Striped.otf"
font_name_exodus_stencil = "Interface/Exodus - Personal Use/ExodusDemo-Stencil.otf"
font_name_exodus_regular = "Interface/Exodus - Personal Use/ExodusDemo-Regular.otf"
font = pygame.font.SysFont(font_name, int(square_size // 5.5))
font_score = pygame.font.SysFont(font_name, int(square_size // 8))
font_submit = pygame.font.SysFont(font_name, int(square_size // 10.5))
font_message = pygame.font.SysFont(font_name, int(square_size // 8.5))
font_winner = pygame.font.SysFont(font_name, int(square_size // 7))
font_winner.set_underline(True)
font_winner_message = pygame.font.SysFont(font_name, int(square_size // 7))
font_restart_message = pygame.font.SysFont(font_name, int(square_size // 7))
font_tie = pygame.font.SysFont(font_name, int(square_size // 7))
font_title = pygame.font.Font(font_name_exodus_sharpen, int(square_size // 4))
font_title_play = pygame.font.Font(font_name_exodus_sharpen, int(square_size // 7))
font_sign = pygame.font.Font(font_name_exodus_striped, int(square_size // 10))
font_sign.set_underline(True)
font_audio = pygame.font.Font(font_name_exodus_stencil, int(square_size // 7))
font_singleplayer = pygame.font.Font(font_name_exodus_sharpen, int(square_size // 5))
font_back = pygame.font.SysFont(font_name, int(square_size // 10))
font_exit = font_back
font_audio_button = pygame.font.SysFont(font_name, int(square_size // 7))
font_difficulty = pygame.font.Font(font_name_exodus_sharpen, int(square_size // 5))
# ----- SCORE -----
score_value_1 = 0
score_value_2 = 0

# ---------------
# music and sound
# ----------------
music_on = True
sound_on = True
mixer.music.load(
    "Interface/sound and music/Time to Spare - An Jone.mp3")
mixer.music.play(-1)
mark_sound = mixer.Sound("Interface/sound and music/woosh sound.mp3")
music_volume = 0.4
mixer.music.set_volume(music_volume)
game_over = mixer.Sound("Interface/sound and music/Deep-male-voice-game-over.wav")

# -------
# SCREEN
# -------
board = np.zeros((board_rows, board_columns))


def show_screen():
    global screen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("TicTacToe")
    screen.fill(bg_color)


# ------- TITLESCREEN -------
title_surface = font_title.render("TicTacToe", True, white)
sign_surface = font_sign.render("By Wotan", True, white)
play_surface = font_title.render("Play", True, white)
option_surface = font_title.render("Options", True, white)
exit_surface = font_title.render("Exit", True, white)
title_x = width // 2 - title_surface.get_width() // 2
title_y = height // 8
sign_x = width // 2 - sign_surface.get_width() // 2
sign_y = title_y * 1.8
play_x = width // 2 - play_surface.get_width() // 2
play_y = title_y + height // 4
option_x = width // 2 - option_surface.get_width() // 2
option_y = play_x + height // 6
exit_title_x = width // 2 - exit_surface.get_width() // 2
exit_title_y = option_y + height // 6
play_button = pygame.Rect(play_x, play_y, play_surface.get_width(), play_surface.get_height())
option_button = pygame.Rect(option_x, option_y, option_surface.get_width(), option_surface.get_height())
exit_title_button = pygame.Rect(exit_title_x, exit_title_y, exit_surface.get_width(), exit_surface.get_height())
arrow_image = pygame.image.load("Interface/images/white_arrow.png")
arrow_transform = width // 8
arrow_image = pygame.transform.flip(arrow_image, True, False)
arrow_image = pygame.transform.scale(arrow_image, (arrow_transform, arrow_transform))
arrow_rec = arrow_image.get_rect()
wait = 0
arrow_image_x = 0
arrow_image_y = 0
# ------- OPTION MENU -------
option_audio_surface = font_audio.render("Audio: ", True, white)
option_audio_x = width // 6 - option_audio_surface.get_width() // 2
option_audio_y = height // 4
louder_button_surface = font_audio_button.render(">>>", True, white)
quieter_button_surface = font_audio_button.render("<<<", True, white)
music_surface = font_audio_button.render(f"Volume: {music_volume}", True, white)
louder_button = pygame.Rect(0, 0, 0, 0)
quieter_button = pygame.Rect(0, 0, 0, 0)
louder_button_x = width - louder_button_surface.get_width() * 1.5
quieter_button_x = louder_button_x - music_surface.get_width() * 1.8
# ------- STARTSCREEN -------
player_1_surface = ""
player_2_surface = " "
message_player = font_message.render(f"Player{turn}, type in your name: ", True, white)
x_input = width // 2 - message_player.get_width() // 2
y_input = height // 2.5
input_rect = pygame.Rect(x_input + message_player.get_width() // 4, y_input, 180, 20)
active = False
submit_text = font_submit.render("Submit", True, white)
submit_x = int(input_rect.x + input_rect.width * 0.32)
submit_y = int(y_input + height / 13)
submit_rect = pygame.Rect(submit_x, submit_y, submit_text.get_width() + 6, submit_text.get_height() + 4)
delete_button_image = pygame.image.load(
    "Interface/images/delete_button.png")
delete_button_image = pygame.transform.scale(delete_button_image, (height // 16, height // 16))
delete_button = pygame.Rect(input_rect.x * 1.7 + 5, input_rect.y - 1, delete_button_image.get_width(),
                            delete_button_image.get_height())
exit_title_surface = font_exit.render("Exit", True, white)
exit_x = 0 + exit_title_surface.get_width() // 2
exit_y = height - exit_title_surface.get_height() * 2
exit_button = pygame.Rect(exit_x - exit_title_surface.get_width() // 8, exit_y - exit_title_surface.get_height() // 8,
                          exit_title_surface.get_width() + exit_title_surface.get_width() // 4,
                          exit_title_surface.get_height() + exit_title_surface.get_height() // 4)
back_surface = font_back.render("Back", True, white)
back_x = width - int(back_surface.get_width() * 1.5)
back_y = exit_y
back_button = pygame.Rect(back_x - back_surface.get_width() // 8, back_y - back_surface.get_height() // 8,
                          back_surface.get_width() + back_surface.get_width() // 4,
                          back_surface.get_height() + back_surface.get_height() // 4)
singleplayer_surface = font_singleplayer.render("Singleplayer", True, white)
multiplayer_surface = font_singleplayer.render("Multiplayer", True, white)
alone_x = 0
alone_y = 0
singleplayer_x = width // 2 - multiplayer_surface.get_width() // 2
singleplayer_y = height // 2 - height // 6
multiplayer_x = singleplayer_x
multiplayer_y = singleplayer_y + height // 6
singleplayer_button = pygame.Rect(singleplayer_x - singleplayer_surface.get_width() // 20,
                                  singleplayer_y - singleplayer_surface.get_height() // 15,
                                  singleplayer_surface.get_width() + singleplayer_surface.get_width() // 10,
                                  singleplayer_surface.get_height() + singleplayer_surface.get_height() // 8)
multiplayer_button = pygame.Rect(multiplayer_x - multiplayer_surface.get_width() // 20,
                                 multiplayer_y - multiplayer_surface.get_height() // 16,
                                 singleplayer_surface.get_width() + multiplayer_surface.get_width() // 10,
                                 singleplayer_surface.get_height() + multiplayer_surface.get_height() // 8)
# ------- DIFFICULTY -------
difficulty_message_surface = font_difficulty.render("Choose your difficulty", True, white)
difficulty_message_x = width // 2 - difficulty_message_surface.get_width() // 2
difficulty_message_y = height // 6
difficulty_easy_surface = font_difficulty.render("Easy", True, white)
easy_x = width // 2 - difficulty_easy_surface.get_width() // 2
easy_y = difficulty_message_y + height // 6
difficulty_middle_surface = font_difficulty.render("Middle", True, white)
middle_x = width // 2 - difficulty_middle_surface.get_width() // 2
middle_y = easy_y + height // 6
difficulty_hard_surface = font_difficulty.render("Hard", True, white)
hard_x = width // 2 - difficulty_hard_surface.get_width() // 2
hard_y = middle_y + height // 6
difficulty_easy_rect = pygame.Rect(easy_x - difficulty_easy_surface.get_width() // 20,
                                   easy_y - difficulty_easy_surface.get_height() // 10,
                                   difficulty_easy_surface.get_width() + difficulty_easy_surface.get_width() // 10,
                                   difficulty_easy_surface.get_height() + difficulty_easy_surface.get_height() // 5)
difficulty_middle_rect = pygame.Rect(middle_x - difficulty_middle_surface.get_width() // 20,
                                     middle_y - difficulty_middle_surface.get_height() // 10,
                                     difficulty_middle_surface.get_width() + difficulty_middle_surface.get_width() // 10,
                                     difficulty_middle_surface.get_height() + difficulty_middle_surface.get_height() // 5)
difficulty_hard_rect = pygame.Rect(hard_x - difficulty_hard_surface.get_width() // 20,
                                   hard_y - difficulty_hard_surface.get_height() // 10,
                                   difficulty_hard_surface.get_width() + difficulty_hard_surface.get_width() // 10,
                                   difficulty_hard_surface.get_height() + difficulty_hard_surface.get_height() // 5)
# ------- COUNTDOWN -------
clock = pygame.time.Clock()
current_time = 0
button_press_time = 0
counter = 0
# ------- ENDSCREEN -------
restart_message_surface = font_restart_message.render("To restart the game press 'R'!", True, white)
tie_message_1 = font_tie.render("Tie!", True, white)
tie_message_2 = font_tie.render("Nobody won!", True, white)


def draw_lines():
    # 1 horizontal
    pygame.draw.line(screen, line_color, (0, square_size), (width, square_size), line_width)
    # 2 horizontal
    pygame.draw.line(screen, line_color, (0, square_size * 2), (width, square_size * 2), line_width)

    # 1 vertical
    pygame.draw.line(screen, line_color, (square_size, 00), (square_size, height), line_width)
    # 2 vertical
    pygame.draw.line(screen, line_color, (square_size * 2, 00), (square_size * 2, height), line_width)


def draw_figures():
    for row in range(board_rows):
        for col in range(board_columns):
            if board[row][col] == 1:
                pygame.draw.circle(screen, circle_color, (
                    int(col * square_size + square_size // 2), int(row * square_size + square_size // 2)),
                                   circle_radius,
                                   circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, cross_color,
                                 (col * square_size + space, row * square_size + square_size - space),
                                 (col * square_size + square_size - space, row * square_size + space), cross_width)
                pygame.draw.line(screen, cross_color, (col * square_size + space, row * square_size + space),
                                 (col * square_size + square_size - space, row * square_size + square_size - space),
                                 cross_width)


def draw_vertical_winning_line(col, player):
    global color
    pos_x = col * square_size + square_size // 2

    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (pos_x, 15), (pos_x, height - 15), 15)


def draw_horizontal_winning_line(row, player):
    global color
    pos_y = row * square_size + square_size // 2

    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (15, pos_y), (width - 15, pos_y), 15)


def draw_desc_winning_line(player):
    global color
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (15, height - 15), (width - 15, 15), 15)


def draw_asc_winning_line(player):
    global color
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (15, 15), (width - 15, height - 15), 15)


def draw_start_player():
    pygame.draw.rect(screen, color_rect, input_rect, 2)
    pygame.draw.rect(screen, color_submit, submit_rect)
    screen.blit(submit_text, (submit_rect.x + 3, submit_rect.y + 2))
    screen.blit(message_player, (x_input, y_input - height // 16))
    screen.blit(title_surface, (title_x, title_y))
    screen.blit(sign_surface, (sign_x, sign_y))


def draw_music_button(x1, y1, x2, y2, surface):
    global quieter_button, louder_button
    center_x = (x1 + x2) // 2 - surface.get_width() // 3
    center_y = (y1 + y2) // 2

    quieter_button = pygame.Rect(x1, y1, quieter_button_surface.get_width(), quieter_button_surface.get_height())
    louder_button = pygame.Rect(x2, y2, louder_button_surface.get_width(), louder_button_surface.get_height())
    music_surface_rect = pygame.Rect(center_x, center_y, surface.get_width(), surface.get_height())
    pygame.draw.rect(screen, bg_color_2, music_surface_rect)
    pygame.draw.rect(screen, bg_color_2, quieter_button)
    pygame.draw.rect(screen, bg_color_2, louder_button)
    screen.blit(quieter_button_surface, (x1, y1))
    screen.blit(louder_button_surface, (x2, y2))
    screen.blit(surface, (center_x, center_y))


def restart():
    global player
    screen.fill(bg_color)
    draw_lines()
    player = 1
    for row in range(board_rows):
        for col in range(board_columns):
            board[row][col] = 0


def mark_square(row, col, player):
    board[row][col] = player
    mark_sound.play()


def available_square(row, col):
    return board[row][col] == 0


def grid_full():
    return 0 not in board


def check_win(player):
    # checks the columns
    for col in range(board_columns):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    # check the rows
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # check the diagonals
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_desc_winning_line(player)
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_asc_winning_line(player)
        return True
    return False


def define_pos(pos, player):
    global row, col
    if int(pos) == 1 or pos == "a1":
        row = 0
        col = 0
    elif int(pos) == 2 or pos == "a2":
        row = 1
        col = 0
    elif int(pos) == 3 or pos == "a3":
        row = 2
        col = 0
    elif int(pos) == 4 or pos == "b1":
        row = 0
        col = 1
    elif int(pos) == 5 or pos == "b2":
        row = 1
        col = 1
    elif int(pos) == 6 or pos == "b3":
        row = 2
        col = 1
    elif int(pos) == 7 or pos == "c1":
        row = 0
        col = 2
    elif int(pos) == 8 or pos == "c2":
        row = 1
        col = 2
    elif int(pos) == 9 or pos == "c3":
        row = 2
        col = 2
    if player == "X":
        return 1
    elif player == "O":
        return 2


def show_score(x1, y1, x2, y2):
    score_1_surface = font_score.render(f"{player_1}\'s wins: {str(score_value_1)}", True, white)
    screen.blit(score_1_surface, (x1, y1))
    score_2_surface = font_score.render(f"{player_2}\'s wins: {str(score_value_2)}", True, white)
    screen.blit(score_2_surface, (x2, y2))


def show_winning_message(x1, y1, x2, y2, font_winner_message_surface=None, font_winner_surface=None):
    screen.blit(font_winner_message_surface, (x1, y1))
    screen.blit(font_winner_surface, (x2, y2))
    screen.blit(restart_message_surface, (x2 // 2, y2 * 2))


def show_tie_message(x1, y1, x2, y2):
    screen.blit(tie_message_1, (x1, y1))
    screen.blit(tie_message_2, (x2, y2))
    screen.blit(restart_message_surface, (x2 // 2, y2 * 2))


def show_player_1():
    global player_1_surface
    player_1_surface = font_message.render(player_1, True, white)
    screen.blit(player_1_surface, (input_rect.x + 5, input_rect.y + 5))
    pygame.draw.rect(screen, bg_color_2, delete_button)
    screen.blit(delete_button_image, delete_button)


def show_player_2():
    global player_2_surface
    player_2_surface = font_message.render(player_2, True, white)
    screen.blit(player_2_surface, (input_rect.x + 5, input_rect.y + 5))
    pygame.draw.rect(screen, bg_color_2, delete_button)
    screen.blit(delete_button_image, delete_button)
    screen.blit(title_surface, (title_x, title_y))
    screen.blit(sign_surface, (sign_x, sign_y))


def scoreboard():
    global score_value_1, score_value_2, winner, player_1, player_2
    if winner == player_1:
        score_value_1 += 1
    elif winner == player_2:
        score_value_2 += 1
    return


def delete_last_chara(text):
    if len(list(text)) >= 1:
        text = list(text)
        text.pop()
        text = "".join(text)
        return text
    else:
        return text


def show_alone():
    pygame.draw.rect(screen, white, singleplayer_button, 2, 3)
    pygame.draw.rect(screen, white, multiplayer_button, 2, 3)
    screen.blit(singleplayer_surface, (singleplayer_x, singleplayer_y))
    screen.blit(multiplayer_surface, (multiplayer_x + multiplayer_surface.get_width() // 40, multiplayer_y))
    screen.blit(title_surface, (title_x, title_y))
    screen.blit(sign_surface, (sign_x, sign_y))


def show_back():
    pygame.draw.rect(screen, white, back_button, 2, 3)
    screen.blit(back_surface, (back_x, back_y))


def show_exit():
    pygame.draw.rect(screen, white, exit_button, 2, 3)
    screen.blit(exit_title_surface, (exit_x, exit_y))


def show_title_screen():
    screen.blit(title_surface, (title_x, title_y))
    screen.blit(sign_surface, (sign_x, sign_y))
    pygame.draw.rect(screen, color_title, play_button, 0, 3)
    screen.blit(play_surface, (play_x, play_y))
    pygame.draw.rect(screen, color_title, option_button, 0, 3)
    screen.blit(option_surface, (option_x, option_y))
    pygame.draw.rect(screen, color_title, exit_title_button, 0, 3)
    screen.blit(exit_surface, (exit_title_x, exit_title_y))


def show_option_menu():
    screen.blit(option_surface, (width // 2 - option_surface.get_width() // 2, height // 25))
    screen.blit(option_audio_surface, (option_audio_x, option_audio_y))


# todo: maybe make it more modable? (e.g. not only for the titlescreen) | IN PROGRESS
def show_arrows():
    global wait, arrow_image_x, arrow_image_y
    mouse_position_x, mouse_position_y = pygame.mouse.get_pos()

    # checks the position of the mouse and shows the arrow
    if play_x <= mouse_position_x <= play_x + play_surface.get_width() and play_y <= mouse_position_y <= play_y + play_surface.get_height():
        screen.blit(arrow_image, (play_x + play_surface.get_width() * 1.25, play_y))
        arrow_image_x, arrow_image_y = play_x + play_surface.get_width() * 1.25, play_y
        wait += 1
    elif option_x <= mouse_position_x <= option_x + option_surface.get_width() and option_y <= mouse_position_y <= option_y + option_surface.get_height():
        screen.blit(arrow_image, (option_x + option_surface.get_width() * 1.25, option_y))
        arrow_image_x, arrow_image_y = option_x + option_surface.get_width() * 1.25, option_y
        wait += 1
    elif exit_title_x <= mouse_position_x <= exit_title_x + exit_surface.get_width() and exit_title_y <= mouse_position_y <= exit_title_y + exit_surface.get_height():
        screen.blit(arrow_image, (exit_title_x + exit_surface.get_width() * 1.25, exit_title_y))
        arrow_image_x, arrow_image_y = exit_title_x + exit_surface.get_width() * 1.25, exit_title_y
        wait += 1
    else:
        if wait >= 1:
            # 'hides' the old arrows with a new rec
            pygame.draw.rect(screen, bg_color_2,
                             pygame.Rect(arrow_image_x, arrow_image_y, arrow_transform, arrow_transform))
            wait = 1


def show_difficulty_screen():
    pygame.draw.rect(screen, white, difficulty_easy_rect, 2, 3)
    pygame.draw.rect(screen, white, difficulty_middle_rect, 2, 3)
    pygame.draw.rect(screen, white, difficulty_hard_rect, 2, 3)
    screen.blit(difficulty_message_surface, (difficulty_message_x, difficulty_message_y))
    screen.blit(difficulty_easy_surface, (easy_x, easy_y))
    screen.blit(difficulty_middle_surface, (middle_x, middle_y))
    screen.blit(difficulty_hard_surface, (hard_x, hard_y))


# todo: place first mark in middle (board[1][1]) | DONE
# todo: different difficulties
#  (easy = only random pos or check general for two in a row , medium = check rows first to win, hard = medium + first mark in mid) | DONE (not perfect)
# todo: ai vs ai (could be funny to watch) as a little secret | IN PROGRESS
def ai(player, difficulty: int = None):
    if not game_is_over:
        valid = True
        # only if difficulty equals hard
        if difficulty >= 3:
            # sets the first mark to board[1][1]
            if board[1][1] == 0:
                board[1][1] = player
                valid = False

            # can the ai win?
            for row in range(board_rows):
                for col in range(board_columns):
                    # check rows
                    # first if he can win a match
                    if board[row][0] == board[row][1] == player != 0 or board[row][0] == board[row][2] == player != 0 \
                            or board[row][2] == board[row][1] == player != 0:
                        if board[row][col] == 0:
                            board[row][col] = player
                            valid = False
                            return
                    # columns
                    if board[0][col] == board[1][col] == player != 0 or board[0][col] == board[2][col] == player != 0 \
                            or board[2][col] == board[1][col] == player != 0:
                        if board[row][col] == 0:
                            board[row][col] = player
                            valid = False
                            return
            # diagonals
            if board[2][0] == board[1][1] == player != 0:
                if board[0][2] == 0:
                    board[0][2] = player
                    valid = False
                    return
            if board[0][2] == board[1][1] == player != 0:
                if board[1][1] == 0:
                    board[1][1] = player
                    valid = False
                    return
            if board[0][0] == board[1][1] == player != 0:
                if board[2][2] == 0:
                    board[2][2] = player
                    valid = False
                    return
            if board[2][2] == board[1][1] == player != 0:
                if board[0][0] == 0:
                    board[0][0] = player
                    valid = False
                    return
            if board[0][0] == board[2][2] == player != 0:
                if board[1][1] == 0:
                    board[1][1] = player
                    valid = False
                    return
        # only if difficulty equals hard or middle
        if difficulty >= 2:
            # can the other player win?
            for row in range(board_rows):
                for col in range(board_columns):
                    # then if he can prevent a win
                    # rows
                    if board[row][0] == board[row][1] != 0 or board[row][0] == board[row][2] != 0 or board[row][2] == \
                            board[row][1] != 0:
                        if board[row][col] == 0:
                            board[row][col] = player
                            valid = False
                            return
                    # check columns
                    if board[0][col] == board[1][col] != 0 or board[0][col] == board[2][col] != 0 or board[2][col] == \
                            board[1][col] != 0:
                        if board[row][col] == 0:
                            board[row][col] = player
                            valid = False
                            return
            # check diagonals
            if board[2][0] == board[1][1] != 0:
                if board[0][2] == 0:
                    board[0][2] = player
                    valid = False
                    return
            if board[0][2] == board[1][1] != 0:
                if board[2][0] == 0:
                    board[2][0] = player
                    valid = False
                    return
            if board[0][0] == board[1][1] != 0:
                if board[2][2] == 0:
                    board[2][2] = player
                    valid = False
                    return
            if board[2][2] == board[1][1] != 0:
                if board[0][0] == 0:
                    board[0][0] = player
                    valid = False
                    return
            if board[0][0] == board[2][2] != 0:
                if board[1][1] == 0:
                    board[1][1] = player
                    valid = False
                    return
        # only if difficulty equals easy, middle or hard
        if difficulty >= 1:
            while valid:
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                if board[row][col] == 0:
                    board[row][col] = player
                    valid = False
                    return


def pick_name():
    names = ["Miguel", "Diablo", "Tom", "Olaf", "Peter", "Sansa", "Diezel Ky", "Kal-El", "Satchel", "Buddy Bear",
             "Saint Lazslo", "EssEyePee", "David"]
    return names[random.randint(0, len(names) - 1)]


def main():
    global music_on, running, game_start, title_screen, music_volume, valid, turn, input_rect, player_1, player_2, \
        option_menu, alone, difficulty, active, game_is_over, player, current_time, button_press_time, counter, \
        winner, color_rect, score_value_1, score_value_2, music_surface, color_rect_inside, message_player
    # mainloop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # turn on/off the music with a button (m)
                if event.key == pygame.K_m and music_on:
                    mixer.music.fadeout(1000)
                    music_on = False
                elif event.key == pygame.K_m and not music_on:
                    mixer.music.play(-1)
                    music_on = True

            # todo: make the startscreen nice an clean, maybe using images? | DONE
            # todo: should look like Singleplayer \n Multiplayer etc | DONE
            # todo: maybe a "back"-button and "exit"-button | DONE
            # todo: tile screen with game title, 'Play', 'Options' (?) and 'Exit' | DONE
            #   Options: maybe audio on/off, colors, etc | DONE
            # todo: add music/sounds | DONE
            # todo: edit the sound/add more sound (winning sound, etc) | IN PROGRESS
            # todo: if you click on play, options, etc. this button should change color/arrow appears | DONE
            #   maybe in Startscreen too | DENIED
            if not game_start:
                # titlescreen
                if title_screen and not option_menu:
                    show_title_screen()
                    show_arrows()
                    if event.type == pygame.MOUSEBUTTONUP and exit_title_button.collidepoint(event.pos):
                        running = False
                    if event.type == pygame.MOUSEBUTTONUP and play_button.collidepoint(event.pos):
                        title_screen = False
                        screen.fill(bg_color_2)
                    if event.type == pygame.MOUSEBUTTONUP and option_button.collidepoint(event.pos):
                        option_menu = True
                        screen.fill(bg_color_2)

                # option menu
                elif title_screen and option_menu:
                    show_option_menu()
                    music_surface = font_audio_button.render(f"Volume: {music_volume}", True, white)
                    draw_music_button(quieter_button_x, option_audio_y, louder_button_x, option_audio_y, music_surface)
                    show_back()

                    if event.type == pygame.MOUSEBUTTONUP and back_button.collidepoint(event.pos):
                        option_menu = False
                        screen.fill(bg_color_2)
                    # todo: showing the Volume | DONE
                    if event.type == pygame.MOUSEBUTTONUP and quieter_button.collidepoint(
                            event.pos) and music_volume >= 0.1:
                        music_volume -= 0.1
                        music_volume = round(music_volume, 1)
                        draw_music_button(quieter_button_x, option_audio_y, louder_button_x, option_audio_y,
                                          music_surface)
                    if event.type == pygame.MOUSEBUTTONUP and louder_button.collidepoint(
                            event.pos) and music_volume <= 0.9:
                        music_volume += 0.1
                        music_volume = round(music_volume, 1)
                        draw_music_button(quieter_button_x, option_audio_y, louder_button_x, option_audio_y,
                                          music_surface)
                    mixer.music.set_volume(music_volume)

                # todo: replace images (single-/multiplayer, back, exit) with text | DONE
                # startscreen
                elif not title_screen:
                    # player wants to play alone?
                    if not valid:
                        show_alone()
                        show_exit()
                        if event.type == pygame.MOUSEBUTTONUP and exit_button.collidepoint(event.pos):
                            running = False
                        show_back()
                        if event.type == pygame.MOUSEBUTTONUP and back_button.collidepoint(event.pos):
                            title_screen = True
                            screen.fill(bg_color_2)
                            break
                        if event.type == pygame.MOUSEBUTTONUP and singleplayer_button.collidepoint(event.pos):
                            alone = 1
                            player_2 = pick_name()
                            valid = True
                            screen.fill(bg_color_2)
                        if event.type == pygame.MOUSEBUTTONUP and multiplayer_button.collidepoint(event.pos):
                            alone = 2
                            valid = True
                            screen.fill(bg_color_2)

                    if valid:
                        # Player 1
                        if turn == 1:
                            # selects the rect
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if input_rect.collidepoint(event.pos):
                                    active = True
                                else:
                                    active = False

                            # text input
                            if event.type == pygame.KEYDOWN and not game_start and active:
                                screen.fill(bg_color_2)
                                if event.type == pygame.K_ESCAPE:
                                    player_1 = player_1[0:-1]
                                else:
                                    # u can tip in the box
                                    player_1 += event.unicode

                            # color for the rect
                            if active:
                                color_rect = color_rect_active
                                color_rect_inside = color_rect_active_inside
                            else:
                                color_rect = color_rect_passive
                                color_rect_inside = color_rect_passive_inside
                            show_player_1()
                            message_player = font_message.render(f"Player{turn}, type in your name: ", True, white)
                            input_rect = pygame.Rect(x_input + message_player.get_width() // 4, y_input,
                                                     max(180, player_1_surface.get_width() + 10),
                                                     player_1_surface.get_height() + 10)

                            # deleting the last chara
                            if event.type == pygame.MOUSEBUTTONDOWN and delete_button.collidepoint(event.pos):
                                player_1 = delete_last_chara(player_1)
                                rect = pygame.Rect(x_input, y_input, input_rect.x - 2, input_rect.y - 2)
                                pygame.draw.rect(screen, color_rect_inside, rect)
                            draw_start_player()
                            show_exit()
                            if event.type == pygame.MOUSEBUTTONUP and exit_button.collidepoint(event.pos):
                                running = False
                            show_back()
                            if event.type == pygame.MOUSEBUTTONUP and back_button.collidepoint(event.pos):
                                valid = False
                                screen.fill(bg_color_2)
                                break
                            # submit button
                            if event.type == pygame.MOUSEBUTTONUP and submit_rect.collidepoint(event.pos):
                                screen.fill(bg_color)
                                turn = 2
                        # choose difficulty
                        elif turn == 2 and alone == 1:
                            show_difficulty_screen()
                            show_exit()
                            if event.type == pygame.MOUSEBUTTONUP and exit_button.collidepoint(event.pos):
                                running = False
                            show_back()
                            if event.type == pygame.MOUSEBUTTONUP and back_button.collidepoint(event.pos):
                                turn = 1
                                screen.fill(bg_color_2)
                                break
                            if event.type == pygame.MOUSEBUTTONUP and difficulty_easy_rect.collidepoint(event.pos):
                                difficulty = 1
                                game_start = True
                                screen.fill(bg_color)
                            if event.type == pygame.MOUSEBUTTONUP and difficulty_middle_rect.collidepoint(event.pos):
                                difficulty = 2
                                game_start = True
                                screen.fill(bg_color)
                            if event.type == pygame.MOUSEBUTTONUP and difficulty_hard_rect.collidepoint(event.pos):
                                difficulty = 3
                                game_start = True
                                screen.fill(bg_color)

                        # Player 2
                        elif turn == 2 and alone == 2:
                            # selects the rect
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if input_rect.collidepoint(event.pos):
                                    active = True
                                else:
                                    active = False

                            # text input
                            if event.type == pygame.KEYDOWN and not game_start and active:
                                screen.fill(bg_color_2)
                                if event.type == pygame.K_ESCAPE:
                                    player_2 = player_1[0:-1]
                                else:
                                    # u can tip in the box
                                    player_2 += event.unicode

                            # color for the rect
                            if active:
                                color_rect = color_rect_active
                                color_rect_inside = color_rect_active_inside
                            else:
                                color_rect = color_rect_passive
                                color_rect_inside = color_rect_passive_inside
                            show_player_2()
                            message_player = font_message.render(f"Player{turn}, type in your name: ", True, white)
                            # deleting the last chara
                            if event.type == pygame.MOUSEBUTTONDOWN and delete_button.collidepoint(event.pos):
                                player_2 = delete_last_chara(player_2)
                                rect = pygame.Rect(x_input, y_input, input_rect.x - 2, input_rect.y - 2)
                                pygame.draw.rect(screen, color_rect_inside, rect)
                            draw_start_player()
                            show_exit()
                            if event.type == pygame.MOUSEBUTTONUP and exit_button.collidepoint(event.pos):
                                running = False
                            show_back()
                            if event.type == pygame.MOUSEBUTTONUP and back_button.collidepoint(event.pos):
                                turn = 1
                                screen.fill(bg_color_2)
                                break

                            # submit button
                            if event.type == pygame.MOUSEBUTTONUP and submit_rect.collidepoint(event.pos):
                                screen.fill(bg_color)
                                game_start = True
                            pass
                        # todo: implement bot/playing alone | DONE
            # todo: maybe using sounds | DONE
            # the actual game
            if game_start:
                draw_lines()
                # the func for the clicking
                if event.type == pygame.MOUSEBUTTONDOWN and not game_is_over:
                    mouse_x = event.pos[0]
                    mouse_y = event.pos[1]
                    clicked_row = int(mouse_y // square_size)
                    clicked_col = int(mouse_x // square_size)
                    if available_square(clicked_row, clicked_col):
                        # simple for:
                        #  'if player == 1:mark_square(clicked_row, clicked_col, 1)if check_win(player) == True:...'
                        mark_square(clicked_row, clicked_col, player)
                        # checks if someone won or tie
                        # todo: after a win wait around 3s so everyone sees who/how someone won | DONE
                        if check_win(player):
                            game_is_over = True
                            game_over.play()
                            button_press_time = pygame.time.get_ticks()
                            if player == 1:
                                winner = player_1
                                scoreboard()
                            elif player == 2:
                                winner = player_2
                                scoreboard()
                        elif grid_full():
                            game_is_over = True
                            winner = None
                            game_over.play()
                            button_press_time = pygame.time.get_ticks()
                        # starts ai for TicTacToe
                        if alone == 1:
                            player = player
                            ai(2, difficulty)
                            draw_figures()
                            if check_win(2):
                                check_win(2)
                                game_is_over = True
                                game_over.play()
                                winner = player_2
                                scoreboard()
                                button_press_time = pygame.time.get_ticks()
                            if check_win(1):
                                game_is_over = True
                                check_win(1)
                                button_press_time = pygame.time.get_ticks()
                        elif alone == 2:
                            player = player % 2 + 1
                            draw_figures()

                    check_win(player % 2 + 1)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        restart()
                        counter = 0
                        current_time = 0
                        button_press_time = 0
                        game_is_over = False
                # todo: make endscreen more accurate | IN PROGRESS
        # timer (waits around 1.8s (ig))
        if 1800 < current_time - button_press_time < 1900:
            counter += 1
        # checks if timer is finished
        if counter > 1:
            # endscreen
            if game_is_over:
                screen.fill(bg_color_2)
                # makes the winning message
                font_winner_message_surface = font_winner_message.render("Congratulations! The winner is:", True, white)
                font_winner_surface = font_winner.render(winner, True, white)
                if winner is not None:
                    screen.fill(bg_color_2)
                    show_winning_message(width // 2 - font_winner_message_surface.get_width() // 2,
                                         height // 2 - height // 2.4,
                                         width // 2 - font_winner_surface.get_width() // 2, height // 2 - height // 2.8,
                                         font_winner_message_surface, font_winner_surface)
                elif winner is None:
                    show_tie_message(width // 2 - tie_message_1.get_width() // 2, height // 2 - height // 2.4,
                                     width // 2 - tie_message_2.get_width() // 2, height // 2 - height // 2.8)
                show_score(width // 2 - width // 2.05, height // 1.35, width // 2 - width // 2.05, height // 1.2)
                show_exit()
                # noinspection PyUnboundLocalVariable
                if event.type == pygame.MOUSEBUTTONUP and exit_button.collidepoint(event.pos):
                    running = False
                show_back()
                if event.type == pygame.MOUSEBUTTONUP and back_button.collidepoint(event.pos):
                    restart()
                    game_is_over, game_start, valid = False, False, False
                    title_screen = True
                    alone, turn, difficulty = 0, 1, 0
                    score_value_1, score_value_2 = 0, 0
                    counter = 0
                    screen.fill(bg_color_2)

        current_time = pygame.time.get_ticks()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    show_screen()
    main()
