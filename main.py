import pygame
import os
from Xlib import display, Xatom, X

# Initialize Pygame
pygame.init()

# Get screen dimensions (your desktop resolution)
screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h

# Create a Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)  # No window border

# Get the X11 window ID from Pygame
window_id = pygame.display.get_wm_info()["window"]

# Connect to the X server
dpy = display.Display()
xwindow = dpy.create_resource_object("window", window_id)

# Set the window type to "_NET_WM_WINDOW_TYPE_DESKTOP"
# This tells the window manager to treat it as a desktop background
atom = dpy.intern_atom("_NET_WM_WINDOW_TYPE")
desktop_atom = dpy.intern_atom("_NET_WM_WINDOW_TYPE_DESKTOP")
xwindow.change_property(atom, Xatom.ATOM, 32, [desktop_atom], mode=X.PropModeReplace)

# Lower the window to the bottom of the stack
xwindow.configure(stack_mode=X.Below)

# Sync changes with the X server
dpy.sync()

# Example: Fill the screen with a color or animation
running = True
clock = pygame.time.Clock()
i = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # Example: Draw something (e.g., a moving rectangle)
    screen.fill((0, 0, 50))  # Dark blue background
    pygame.draw.rect(screen, (i, 0, 0), (WIDTH // 2 - 50, HEIGHT // 2 - 50, 100, 100))  # Red square

    pygame.display.flip()
    clock.tick(60)  # 60 FPS
    
    i += 1
    i = i % 255

pygame.quit()
dpy.close()
