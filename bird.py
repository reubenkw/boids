import math
import random
import pygame as pg

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

# CONFIGURATION:
visualRange = 80
# Flying towards peers
centering_factor = 0.05
# Avoiding eachother
minDistance = 15
avoidFactor = 0.2
# Matching Velocity of peers
matchingFactor = 0.07
# Speed limiting
speedLimit = 10

class bird:
  def __init__(self, maxV, width, height):
    self.x = random.random() * width
    self.y = random.random() * height
    self.dx = random.random() * maxV * 2 - maxV
    self.dy = random.random() * maxV * 2 - maxV
    self.birds_in_range = []

  def distance(self, bird2):
    return math.sqrt((self.x - bird2.x) ** 2 + (self.y - bird2.y) ** 2)

  def nClosestBirds(self, birds, n: int):
    keys = [self.distance(brd) for brd in birds]
    sorted_birds = sorted(birds, key = lambda bird: self.distance(bird))

    # print("Sorted Birds")
    # for brd in sorted_birds:
    #   print("(x:{0:.1f}, y:{1:.1f}) | (dx:{2:.1f}, dy:{3:.1f})".format(brd.x, brd.y, brd.dx, brd.dy))

    return sorted_birds[1:n + 1]

  def keepWithinBounds(self, width, height):
    margin = 50
    turn_factor = 5

    if (self.x < margin):
      self.dx += turn_factor
    
    if (self.x > width - margin):
      self.dx -= turn_factor
    
    if (self.y < margin):
      self.dy += turn_factor
    
    if (self.y > height - margin):
      self.dy -= turn_factor

  def findBirdsInRange(self, birds):

    self.birds_in_range = []

    for brd in birds:
      if (self != brd):
        if (self.distance(brd) < visualRange):
          self.birds_in_range.append(brd)

  def flyTowardsCenter(self):

    centerX = 0
    centerY = 0

    for brd in self.birds_in_range:
      centerX += brd.x
      centerY += brd.y

    centerX /= len(self.birds_in_range)
    centerY /= len(self.birds_in_range)

    self.dx += (centerX - self.x) * centering_factor
    self.dy += (centerY - self.y) * centering_factor

  def avoidOthers(self):

    moveX = 0
    moveY = 0

    for brd in self.birds_in_range:
      if (self != brd):
        if (self.distance(brd) < minDistance):
          moveX += self.x - brd.x
          moveY += self.y - brd.y

    self.dx += moveX * avoidFactor
    self.dy += moveY * avoidFactor

  def matchVelocity(self):

    avgDX = 0
    avgDY = 0

    for brd in self.birds_in_range:
      avgDX += brd.dx
      avgDY += brd.dy

    avgDX /= len(self.birds_in_range)
    avgDY /= len(self.birds_in_range)

    self.dx += (avgDX - self.dx) * matchingFactor
    self.dy += (avgDY - self.dy) * matchingFactor
        
  
  def limitSpeed(self):

    speed = math.sqrt(self.dx ** 2 + self.dy ** 2)
    if (speed > speedLimit):
      self.dx = (self.dx / speed) * speedLimit
      self.dy = (self.dy / speed) * speedLimit

  def draw(self, win):
    draw_scale = 3
    angle = math.atan2(self.dx, self.dy)

    if len(self.birds_in_range) < 10:
      colour = RED
    elif len(self.birds_in_range) < 50:
      colour = GREEN
    else:
      print(len(self.birds_in_range))
      colour = BLUE

    pg.draw.polygon(win, colour, [
      [self.x - draw_scale * math.cos(angle), self.y + draw_scale * math.sin(angle)], 
      [self.x + 3 * draw_scale * math.sin(angle), self.y + 3 * draw_scale * math.cos(angle)], 
      [self.x + draw_scale * math.cos(angle), self.y - draw_scale * math.sin(angle)]], 1)
