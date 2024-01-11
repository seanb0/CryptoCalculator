###Developer Note: This program took inspiration from the coinstats.app page for crpyto calculation


import pygame
import sys

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def calculate_profit(buy_price, sell_price, investment, invest_fee, exit_fee):
    try:
        buy_price = float(buy_price)
        sell_price = float(sell_price)
        investment = float(investment)
        invest_fee = float(invest_fee)
        exit_fee = float(exit_fee)

        if buy_price == 0:
            raise ValueError("Buy price cannot be zero")

        coins_bought = investment / buy_price
        total_investment = investment + invest_fee
        total_exit_value = coins_bought * sell_price - exit_fee
        profit = total_exit_value - total_investment

        return f"Profit: {profit:.2f}" if profit >= 0 else f"Loss: {profit:.2f}"
    except ValueError as e:
        return f"Error: {str(e)}"



def calculate_Total_Investment_Amount(investment):
    try:
        investment = float(investment)

        return f"Total Investment Amount: {investment:.2f}"
    except ValueError:
        return "Total Investment Amount: Error"

def calculate_Total_Exit_Amount(buy_price, sell_price, investment, invest_fee, exit_fee):
    try:
        buy_price = float(buy_price)
        sell_price = float(sell_price)
        investment = float(investment)
        invest_fee = float(invest_fee)
        exit_fee = float(exit_fee)

        if buy_price == 0:
            raise ValueError("Buy price cannot be zero")

        total_investment = investment - invest_fee
        coins_bought = investment / buy_price
        total_exit_value = (coins_bought * sell_price) - exit_fee

        return f"Total Exit Amount: {total_exit_value:.2f}"
    except ValueError as e:
        return f"Total Exit Amount: Error"


####INIT STUFF AND VARIABLES####
pygame.init()
clock = pygame.time.Clock()
title_font = pygame.font.SysFont(None, 98, bold=True, italic=False)
base_font = pygame.font.SysFont("Arial", 30)
SCREEN_WIDTH = 800
SCREEN_LENGTH = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))

user_text1 = ''#Coint
user_text2 = ''#Invest
user_text3 = ''#Buy
user_text4 = ''#Sell
user_text5 = ''#Invest
user_text6 = ''#Exit

input_rect1 = pygame.Rect(50, 200, 140, 38)
input_rect2 = pygame.Rect(50, 308, 140, 38)
input_rect3 = pygame.Rect(200, 200, 140, 38)
input_rect4 = pygame.Rect(200, 308, 140, 38)  
input_rect5 = pygame.Rect(50, 415, 140, 38)
input_rect6 = pygame.Rect(200, 415, 140, 38)

color_active = pygame.Color('Black')
color_passive = pygame.Color('Gray')
color = color_passive

active1 = False
active2 = False
active3 = False
active4 = False
active5 = False
active6 = False

run = True
####MAIN###
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
###CODE FOR HIGHTLIGHTING INPUT BOX#####
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect1.collidepoint(event.pos):
                active1 = True
                active2 = False
                active3 = False
                active4 = False
                active5 = False
                active6 = False
            elif input_rect2.collidepoint(event.pos):
                active1 = False
                active2 = True
                active3 = False
                active4 = False
                active5 = False
                active6 = False
            elif input_rect3.collidepoint(event.pos):
                active1 = False
                active2 = False
                active3 = True
                active4 = False
                active5 = False
                active6 = False
            elif input_rect4.collidepoint(event.pos):
                active1 = False
                active2 = False
                active3 = False
                active4 = True
                active5 = False
                active6 = False
            elif input_rect5.collidepoint(event.pos):
                active1 = False
                active2 = False
                active3 = False
                active4 = False
                active5 = True
                active6 = False
            elif input_rect6.collidepoint(event.pos):
                active1 = False
                active2 = False
                active3 = False
                active4 = False
                active5 = False
                active6 = True
            else:
                active1 = False
                active2 = False
                active3 = False
                active4 = False
                active5 = False
                active6 = False
####CODE FOR BACKSPACE#####
        if event.type == pygame.KEYDOWN:
            if active1:
                if event.key == pygame.K_BACKSPACE:
                    user_text1 = user_text1[:-1]
                else:
                    user_text1 += event.unicode
            elif active2:
                if event.key == pygame.K_BACKSPACE:
                    user_text2 = user_text2[:-1]
                else:
                    user_text2 += event.unicode
            elif active3:
                if event.key == pygame.K_BACKSPACE:
                    user_text3 = user_text3[:-1]
                else:
                    user_text3 += event.unicode
            elif active4:
                if event.key == pygame.K_BACKSPACE:
                    user_text4 = user_text4[:-1]
                else:
                    user_text4 += event.unicode
            elif active5:
                if event.key == pygame.K_BACKSPACE:
                    user_text5 = user_text5[:-1]
                else:
                    user_text5 += event.unicode
            elif active6:
                if event.key == pygame.K_BACKSPACE:
                    user_text6 = user_text6[:-1]
                else:
                    user_text6 += event.unicode

    screen.fill((255, 255, 255))

    draw_text("Crypto Profit Calculator", title_font, (0, 0, 0), 0, 0)
    draw_text("Coin", base_font, (0, 0, 0), 50, 160)
    draw_text("Buy Price", base_font, (0, 0, 0), 200, 160)
    draw_text("Investment", base_font, (0, 0, 0), 50, 270)
    draw_text("Sell Price", base_font, (0, 0, 0), 200, 270)
    draw_text("Invest Fee", base_font, (0, 0, 0), 50, 380)
    draw_text("Exit Fee", base_font, (0, 0, 0), 200, 380)


    ###TITLE BORDER###
    pygame.draw.rect(screen, (0,0,0), (0, 70, 900, 5), width = 0)

    ###RESULT DISPLAY BORDER###
    pygame.draw.rect(screen, (0,0,0), (350, 200, 425, 250), width = 2, border_radius=10)
    #pygame.draw.rect(screen, (0,0,0), (0, 450, 900, 5), width = 0) #Even line for Square and Input


    ###RESULT DISPLY####

    ##Profit and Loss Display##
    profit_loss = calculate_profit(user_text3, user_text4, user_text2, user_text5, user_text6)
    draw_text(profit_loss, base_font, (0, 0, 0), 360, 220)


    ##Total Investment Amount Display##
    invest = calculate_Total_Investment_Amount(user_text2)
    draw_text(invest, base_font, (0, 0, 0), 360, 260)    

    ##Total Exit Amount##
    total_exit_amount = calculate_Total_Exit_Amount(user_text3, user_text4, user_text2, user_text5, user_text6)
    draw_text(total_exit_amount, base_font, (0, 0, 0), 360, 300)

    for i, (input_rect, user_text) in enumerate(zip([input_rect1, input_rect2, input_rect3, input_rect4, input_rect5, input_rect6],
                                                    [user_text1, user_text2, user_text3, user_text4, user_text5, user_text6])):
        if locals()[f"active{i + 1}"]:
            color = color_active
        else:
            color = color_passive

        pygame.draw.rect(screen, color, input_rect, 2)
        text_surface = base_font.render(user_text, True, (0, 0, 0))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)

    pygame.display.flip()
    clock.tick(60)
