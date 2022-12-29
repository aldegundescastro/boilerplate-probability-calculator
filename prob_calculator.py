import copy
import random

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(int(value)):
        self.contents.append(key)
    #print(self.contents)

  def draw(self, balls_to_draw):
    #contents
    list_draw = []
    if balls_to_draw > len(self.contents):
      return self.contents
    else:
      # k = number of items to select
      #list_draw = random.choices(self.contents, k=balls_to_draw)
      for i in range(balls_to_draw):
        aux_index = random.randrange(len(self.contents))
        list_draw.append(self.contents[aux_index])
        self.contents.pop(aux_index)
      return list_draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  aux_dic = {}
  aux_cont = 0
  
  for i in range(num_experiments):
    aux  = 0
    copy_hat = copy.deepcopy(hat)
    aux_balls_drawn = copy_hat.draw(num_balls_drawn)
    
    for k, v in expected_balls.items():
      if aux_balls_drawn.count(k) >= v:
        aux += 1

    if aux == len(expected_balls):
      aux_cont += 1

    aux_dic.clear()

  probability = aux_cont / num_experiments
  return probability
