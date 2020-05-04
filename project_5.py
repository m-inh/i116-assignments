import math
import numpy as np
import matplotlib.pyplot as plt

upper_case_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case_alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

mini_dict = ["go", "python", "javascript"]

char_maps = [upper_case_alphabet, lower_case_alphabet, numbers]


class Character:
  def __init__(self, char):
    self.char = char
    self.code = -1
    self.map_index = -1
    for i in range(len(char_maps)):
      for c in char_maps[i]:
        if (c == char):
          self.map_index = i
          self.code = char_maps[i].index(c)
          break

  def shift(self, n):
    assert -9 <= n <= 9

    if (self.map_index == -1):
      return self

    char_map = char_maps[self.map_index]
    map_size = len(char_map)
    new_index = n + self.code
    
    if (new_index >= map_size):
      new_index = new_index - map_size
    elif (new_index < 0):
      new_index = new_index + map_size
    
    new_char = char_maps[self.map_index][new_index]
    
    return Character(new_char)

  def __str__(self):
    return self.char

def have_meaning(w, dict):
  try:
    return dict.index(w) != -1
  except:
    return False


def encode(word, delta):
  # Tokenize word into letters
  letters = list(word)
  en_word = []

  for l in letters:
    c = Character(l)
    e = c.shift(delta)
    en_word.append(e.char)

  return "".join(en_word)


def decode(word, dict):
  for delta in range(-9, 9):
    tmp = encode(word, delta)
    if (have_meaning(tmp, dict)):
      return (tmp, delta)

  return -1

# Test
c1 = Character("a")
c2 = Character("A")
c3 = Character("0")
c4 = Character("@")

assert c1.char == "a"
assert c2.char == "A"
assert c3.char == "0"
assert c4.char == "@"
assert c1.map_index == 1
assert c2.map_index == 0
assert c3.map_index == 2
assert c4.map_index == -1
assert c1.code == 0
assert c2.code == 0
assert c3.code == 0
assert c4.code == -1

c1_2 = c1.shift(2)
c1_3 = c1.shift(-3)

assert c1_2.char == "c"
assert c1_2.code == 2
assert c1_2.map_index == 1
assert c1_3.char == "x"

c2_2 = c2.shift(-3)

assert c2_2.char == "X"

c3_2 = c3.shift(-3)

assert c3_2.char == "7"

assert have_meaning("javascript", mini_dict) == True
assert have_meaning("@", mini_dict) == False

print("All test are passed! 🎉")

plain_txt = "python"
delta = 6

en_txt = encode(plain_txt, delta)
de_txt, de_delta = decode(en_txt, mini_dict)

predict_delta = -de_delta

assert plain_txt == de_txt
assert delta == predict_delta

print("plain_txt:", plain_txt)
print("en_txt:   ", en_txt)
print("de_txt:   ", de_txt)
print("predict_delta:   ", predict_delta)

print("All test are passed! 🎉")