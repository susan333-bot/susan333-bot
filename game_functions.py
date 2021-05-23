# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:49:01 2021

@author: susan333
"""

import sys
import pygame 

def check_events(ship):
    for event in pygame.event.get():        
        
        if event.type == pygame.QUIT:
                sys.exit()
                
        elif event.type == pygame.KEYDOWN:
            if event.key== pygame.K_RIGHT:
                ship.rect.centerx += 1
                
                
def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme() 
    pygame.display.flip()