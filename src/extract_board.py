import numpy as np
import xml.etree.ElementTree as ET
import pickle

root = ET.parse("board.xml").getroot()
board = np.zeros((4,199,199))

print(len(root))
for elem in root:
    i = elem.get("id")
    for action in elem:
        transp = action[0].text
        j = action[1].text
        transp_id = ["taxi","bus","underground","boat"].index(transp)
        board[transp_id,int(i) - 1,int(j) - 1] = 1

with open("rides.pkl","wb") as file:
    pickle.dump(board,file)
