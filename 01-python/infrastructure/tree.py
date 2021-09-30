def draw_tree(height):

  leaves = """       _-_
    /~~   ~~\\
 /~~         ~~\\
{               }
 \  _-     -_  /
   ~  \\\\ //  ~
"""

  trunk = """      // \\\\"""

  wood = ""
  for i in range(height):
    wood += "  _ -  | |   -_\n"
    
  leaves += wood

  leaves += trunk

  print(leaves) 
  return

draw_tree(10)