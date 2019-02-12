import matplotlib.pyplot as plt
import numpy as np

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


class PlotGrid:
    def __init__(self,dimension_x,dimension_y):
        self.dimension_x = dimension_x
        self.dimension_y = dimension_y
        self.total_length = dimension_x*dimension_y
        

    def drawGrid(self,grid,title):
        size_l = int(np.sqrt(len(grid)))
        plt.figure(figsize=(4,4))
        plt.ylim(0,self.dimension_x)
        plt.xlim(0,self.dimension_y)
        plt.xticks(range(size_l))
        plt.yticks(range(size_l))
        plt.rc('grid', linestyle="-", color='black')
        plt.title(title)
        for x in range(self.dimension_x):
            for y in range(self.dimension_y):
                temp_val = grid[x + self.dimension_x *y]
                plt.text((x)+0.5,(self.dimension_y-1-y)+0.5,"{0:.2f}".format(temp_val) if type(temp_val) == "float" else temp_val, ha="center", va="center")

        plt.grid(True)
        plt.savefig("img/cuadricula/{}".format(title.replace(" ","_").replace("ó","o").lower()))
        plt.show()
        
    def printActionValue(self,action_value, number = 0):
        simbols = list(range(self.total_length))
        for x,value in enumerate(action_value):
            simbols[x] = ""
            if((x != 0) & (x!= len(action_value) -1 ) ):
                max_p = max(action_value[x].values())
                if(action_value[x]["arriba"] == max_p):
                    simbols[x]= simbols[x]+"↑"
                if(action_value[x]["abajo"] == max_p):
                    simbols[x]= simbols[x]+"↓"
                if(action_value[x]["izquierda"] == max_p):
                    simbols[x]= simbols[x]+"←"
                if(action_value[x]["derecha"] == max_p):
                    simbols[x]= simbols[x]+"→"
        self.drawGrid(simbols,"Mejor acción en {}".format(number))