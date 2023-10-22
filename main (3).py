class player:
  def play(self):
    print("The player is playing cricket.")

class Batsman(player):
  def play(self):
    print("The Batsman is batting")
class Bowler(player):
  def play(self):
    print("The Bowler is bowling")
Batsman=Batsman()
Bowler=Bowler()

Batsman.play()
Bowler.play()
