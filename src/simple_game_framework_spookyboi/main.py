# This file holds the main program for the game the Neural Network will be playing
import pygame
from apscheduler.schedulers.background import BackgroundScheduler
from threading import Event
from typing import List
import signal

class Game:
    def __init__(self):
        screen = pygame.display.set_mode((150, 600))
    
        running = Event()
        physicsLock = Event()
        renderLock = Event()
        
        physics_process = BackgroundScheduler()
        physics_process.start()
        physics_process.add_job(self.physicsLoop, "interval", seconds = 0.25, args=[physicsLock])
        
        render_process = BackgroundScheduler()
        render_process.start()
        render_process.add_job(self.renderLoop, "interval", seconds = 0.25, args=[renderLock])
        
        while not running.is_set():
            self.eventLoop(running)
            
        physics_process.shutdown()
        render_process.shutdown()
        
        while physicsLock.is_set() or renderLock.is_set():
            pass
        pygame.quit()
    
    def physicsLoop(self, lock: Event) -> None:
        if lock.is_set():
            print("Error: Render loop is still running! Aborting new loop...")
            pass
        else:
            lock.set()
            
            # Main Physics Loop
            
            lock = Event()

    def renderLoop(self, lock: Event) -> None:
        if lock.is_set():
            print("Error: Render loop is still running! Aborting new loop...")
            pass
        else:
            lock.set()
            
            # Main Render Loop
            
            lock = Event()

    def eventLoop(self, running: Event, debug: bool = False) -> None:
        events = pygame.event.get()
        for event in events:
            if debug: print(event.dict)
            
            match event.type:
                case pygame.KEYDOWN:
                    if event.dict.get("unicode") == '\x1b': running.set()
                case pygame.QUIT: running.set()