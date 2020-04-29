from bird import bird

class flock:
  def __init__(self, numBirds, maxV, size):
    self.width, self.height = size

    self.birds = []
    for i in range(numBirds):
      self.birds.append(bird(maxV, self.width, self.height))

  def loop(self):
    for brd in self.birds:
      brd.findBirdsInRange(self.birds)

      if(brd.birds_in_range):
        brd.flyTowardsCenter()
        brd.avoidOthers()
        brd.matchVelocity()
      brd.limitSpeed()
      brd.keepWithinBounds(self.width, self.height)

      brd.x += brd.dx
      brd.y += brd.dy

  def draw(self, win):
    for brd in self.birds:
      brd.draw(win)

