import pygame
import os

from pygame.locals import *

from locals import *

import data

from frame import Frame

class Animation:

  def __init__(self, object, anim_name):
    try:
      conffile = open(data.animpath(object, anim_name))
    except:
      conffile = open(data.animpath("default", "static"))
    tiley = 0
    values = []
    self.frames = []
    self.repeat_times = -1
    for line in conffile.readlines():
      if line.strip() != "":
        values = line.split()
        if values[0] == "repeat_times":
          self.repeat_times = int(values[1])
        if values[0] == "frame":
          self.frames.append(Frame(object, anim_name, len(self.frames), int(values[2])))
    self.reset()
    return

  def reset(self):
    self.c = 0
    self.i = 0
    self.repeated = 0
    self.finished = False
    self.image = self.frames[self.i].get_image()
    self.rect = self.image.get_rect()
    return

  def get_rect(self):
    return self.rect

  def update_and_get_image(self):
    if (not self.finished):
      self.c += 1
      if (self.c > int(self.frames[self.i].get_time())):
        self.c = 0
        self.i += 1
        if (self.i == len(self.frames)):
          self.repeated += 1
          if (self.repeated == self.repeat_times):
            self.i -= 1
            self.finished = True
          else:
            self.i = 0
      self.image = (self.frames[self.i]).get_image()
    return self.image