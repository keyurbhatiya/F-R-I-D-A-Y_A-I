from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import pygame
from pygame import mixer

mixer.init()

root = Tk()
root.geometry("1000x500")

def play_video():
    root.lift()
    root.attributes("-topmost", True)

    # Load the video file
    video_path = "../Untitled video - Made with Clipchamp.mp4"  # Replace with the path to your video file
    pygame.mixer.quit()  # Quit the previous mixer to use pygame.mixer for video
    pygame.mixer.init()

    pygame.display.set_caption("Video Player")
    screen = pygame.display.set_mode((1000, 500))

    clock = pygame.time.Clock()
    movie = pygame.movie.Movie(video_path)
    movie.set_display(screen)

    movie.play()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(screen, (0, 0))
        pygame.display.flip()

        clock.tick(30)

    movie.stop()
    pygame.quit()
    root.destroy()

play_video()
root.mainloop()
