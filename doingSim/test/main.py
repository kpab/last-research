# coding: UTF-8
from modules.Simulation import Simulation
from modules.Constants_morning import *


type_name = "test01"
sim_name = "test@" + type_name

# 繧ｷ繝溘Η繝ｬ繝ｼ繧ｷ繝ｧ繝ｳ縺ｮ險ｭ螳?
sim = Simulation(WIDTH, HEIGHT, sim_name, type_name)

# sim.add_wall(400, 340, 410, 350)
# 螢√?ｮ霑ｽ蜉?

sim.add_wall(0, 0, 30, 500) # 蟾ｦ
sim.add_wall(430, 360, 500, 500) # 蜿ｳ
sim.add_wall(0, 450, 290, 500) # 荳?
sim.add_wall(290, 480, 500, 500) # 荳?
sim.add_wall(0, 0, 500, 150) # 荳?
sim.add_wall(0, 0, 300, 300) # 蟾ｦ荳?
sim.add_wall(300, 150, 500, 180)
sim.add_wall(150, 300, 185, 350)

sim.add_wall(110, 420, 140, 450) # 繧ｨ繝ｬ繝吶?ｼ繧ｿ繝ｼ
sim.add_wall(375, 180, 400, 210) # 邊ｾ邂玲ｩ?

sim.add_wall(185, 300, 195, 340)
sim.add_wall(195, 300, 205, 330)
sim.add_wall(205, 300, 215, 320)
sim.add_wall(215, 300, 225, 310)

sim.add_wall(250, 370, 290, 450)
sim.add_wall(240, 380, 250, 450)
sim.add_wall(230, 390, 250, 450)
sim.add_wall(220, 400, 230, 450)
sim.add_wall(210, 410, 220, 450)
sim.add_wall(200, 420, 210, 450)
sim.add_wall(190, 430, 200, 450)
sim.add_wall(50, 300, 150, 350)
sim.add_wall(495, 0, 500, 500)

# 霑ｽ蜉?髫懷ｮｳ迚ｩ
sim.add_wall(395, 350, 405, 360)

# 繝輔ぉ繧､繧ｯ螢?
# sim.add_fake_wall(475, 0, 500, 500)
sim.add_fake_wall(30,300, 50, 450)
sim.add_fake_wall(290, 370, 300, 450)
sim.add_fake_wall(290, 450, 500, 480) # 荳?

# 繧ｹ繧ｿ繝ｼ繝井ｽ咲ｽｮ縺ｮ霑ｽ蜉?
### add_start_position(x, y, weight, futinobe, middle, middle_2)
# --- futinobe person ---
sim.add_start_position(490, 200, 1, True, False)
sim.add_start_position(490, 220, 1, True, False)
sim.add_start_position(490, 240, 1, True, False)

# --- futinobe worker ---
# 髫取ｮｵ(螂･)
sim.add_start_position(55, 440, 3, False, True)
sim.add_start_position(55, 430, 3, False, True)
sim.add_start_position(55, 420, 3, False, True) 
sim.add_start_position(55, 410, 3, False, True)

# 繧ｨ繧ｹ繧ｫ繝ｬ繝ｼ繧ｿ繝ｼ(荳翫ｊ)
sim.add_start_position(310, 440, 3, False) 
sim.add_start_position(310, 420, 3, False) 

# 髫取ｮｵ(謇句燕)
sim.add_start_position(420, 440, 1, False, middle_2=True)
sim.add_start_position(420, 430, 2, False, middle_2=True)
sim.add_start_position(420, 420, 2, False, middle_2=True) 
sim.add_start_position(420, 410, 2, False, middle_2=True) 
sim.add_start_position(420, 400, 2, False, middle_2=True) 
sim.add_start_position(420, 390, 2, False, middle_2=True) 
sim.add_start_position(420, 380, 1, False, middle_2=True) 

# ------------------------------
### add_goal(x, y, weight, futinobe, middle, middle_2)
# 逶ｮ逧?蝨ｰ(遒ｺ邇?縺ゅｊ?ｼ?
sim.add_goal(490, 260, 1, False)
sim.add_goal(490, 280, 1, False)
sim.add_goal(490, 300, 1, False)
sim.add_goal(490, 320, 1, False)
sim.add_goal(490, 340, 1, False) # 12/5 tuika

# 髫取ｮｵ(蜿ｳ)
sim.add_goal(420, 440, 1, True, False, True)
# sim.add_goal(420, 430, 1, True, False, True)
# sim.add_goal(420, 420, 1, True, False, True)
# sim.add_goal(420, 410, 1, True, False, True) 
# sim.add_goal(420, 400, 1, True, False, True) 
# sim.add_goal(420, 390, 1, True, False, True) 
# sim.add_goal(420, 380, 1, True, False, True) 

# 髫取ｮｵ(螂･)
sim.add_goal(55, 400, 2, True, True) 
sim.add_goal(55, 390, 2, True, True)
sim.add_goal(55, 380, 2, True, True)
sim.add_goal(55, 370, 2, True, True)

# 繧ｨ繧ｹ繧ｫ繝ｬ繝ｼ繧ｿ繝ｼ(荳九ｊ)
sim.add_goal(310, 400, 2, True) 
sim.add_goal(310, 380, 2, True) 

# ------------------------------
# 荳ｭ髢灘慍轤ｹ
## add_middle_position(x, y, Right=False)
sim.add_middle_position(300, 310)
sim.add_middle_position(300, 320)
sim.add_middle_position(300, 330)
sim.add_middle_position(300, 340)
sim.add_middle_position(300, 350)
# sim.add_middle_position(300, 360)


# sim.add_middle_position(420, 350, True)
# sim.add_middle_position(415, 350, True)
sim.add_middle_position(410, 350, True)
# 豸医＠縺?
# sim.add_middle_position(405, 350, True)
# sim.add_middle_position(400, 350, True)
# sim.add_middle_position(395, 350, True)
sim.add_middle_position(390, 350, True)
sim.add_middle_position(385, 350, True)

# 蛻晄悄繧ｨ繝ｼ繧ｸ繧ｧ繝ｳ繝医?ｮ逕滓??
for _ in range(START_HUMAN_COUNT):
    sim.born_agent()

# 繧｢繝九Γ繝ｼ繧ｷ繝ｧ繝ｳ縺ｮ螳溯｡?
sim.animate(FRAME_COUNT)

