#!/usr/bin/ipython3
"""
takes list of houses jQuery got us, cleans & filters our output down to the ones we want.

hopefully.
"""
houses = ["Stark of Winterfell",
          "Tully of Riverrun",
          "Arryn of the Eyrie",
          "Lannister of Casterly Rock",
          "Baratheon of Storm's End",
          "Tyrell of Highgarden",
          "Martell of Sunspear",
          "Targaryen of King's Landing"]

with open('full_list.txt', 'r') as infile:
  with open('main_houses.txt', 'w') as outfile:
    for n, hname in enumerate(infile):
      n += 1
      print(n)
      for housestring in houses:
        name, locate = housestring.split(" of ")
        if (name in hname) and (locate in hname):
          outfile.write("\n")
          outfile.write(hname)
          outfile.write(" : ")
          outfile.write("https://anapioficeandfire.com/api/houses/{}/".format(str(n)))
        
