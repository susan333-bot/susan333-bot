# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:49:01 2021

@author: susan333
"""

import sys
from typing import Tuple
import pygame 

def check_events(ship):
    for event in pygame.event.get():        
        
        if event.type == pygame.QUIT:
                sys.exit()
                
        elif event.type == pygame.KEYDOWN:
            if event.key== pygame.K_RIGHT:
                ship.moving_right=True
            if event.key== pygame.K_LEFT:
                ship.moving_left=True


        elif event.type==pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right= False
            if event.key == pygame.K_LEFT:
                ship.moving_left= False   
                
def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme() 
    pygame.display.flip()