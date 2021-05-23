# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:24:46 2021

@author: susan333
"""

import pygame


class Ship():
    
    def __init__(self,screen):
        
        self.screen=screen
        
        # 加载飞船图像，获取外接矩形
        
        self.image=pygame.image.load('ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        
        self.rect.centerx=self.screen_rect.centerx 
        self.rect.bottom=self.screen_rect.bottom
        
    def blitme(self):
        
        self.screen.blit(self.image,self.rect)
        