class SergioRNS():
    
    def __init__(self):
        x_max = 0
        y_max = 0
        z_max = 0
        depht_image = []
        map_3d = []
        map_2d = []
        map_2d_bool = []
        map_2d_points = []
        map_path = []
        ghost_value = -1
        too_high_value = -2
        too_high_k = 4
        target = [0, 0]
        position = [0, 0, 0]

    class point():
        value = 0
        dist2target = 0
        inequality = 0
        obstacle_prox = 0
            
            
    def build_new_map(self, fill_value):
        map_3d = [[[fill_value for x in range(self.x_max)] for y in range(self.y_max)] for z in range(self.z_max)]
        map_2d = [[fill_value for x in range(self.x_max)] for y in range(self.y_max)]
        map_path = map_2d
        map_2d_points = [[point() for x in range(self.x_max)] for y in range(self.y_max)]
        
    def update_dimensions(self):
        self.x_max = len(map_2d)
        self.y_max = len(map_2d[0])
        self.z_max = len(map_3d[0][0])
        
    def iterator2d(self):
        for x in range(self.x_max):
            for y in range(self.y_max):
                yield x, y

    def iterator3d(self):
        for x, y in iterator2d():
            for z in range(self.z_max):
                yield x, y, z
                
    def iterator_near(self, Px, Py, r_min, r_max):
        for x, y in iterator2d():
            if r_min < distance(Px-x, Py-y) < r_max:
                yield x, y

    def convert_to_2d(self):
        a = False
        for x, y, z in iterator3d():
            a |= self.map_3d[x][y][z]
            if(self.map_3d[x][y][z] == 1):
                self.map_2d[x][y] = z
            if(z == (x_max-1)):
                if(a == False):
                    self.map_2d[x][y] = self.ghost_value
                a = False
            
    def distance(self, x, y):
        return math.sqrt(x**2 + y**2)

    def distance_rel(self, x1, y1, x2, y2):
        return distance_abs(x1-x2, y1-y2)

    def check_diff(self, px, py):
        difference = 0
        center_value = self.map_2d[px][py]
        for x, y in iterator_near(px, py, 0, 1.5):
            difference = self.map_2d[x][y] - center_value)
            if(difference > self.too_high_k):
                return True
        return False
    
    def remove_too_high(self):
        self.map_2d_bool = [[0 for x in range(self.x_max)] for y in range(self.y_max)]
        for x, y in iterator2d():
            self.map_2d_bool[x][y] = check_diff(x, y, map_2d)

    def add_distance_weights(self):
        for x, y in iterator2d():
            map_2d_points[x][y].distance = distance_rel(target[0],
                                                        target[1],
                                                        x, y)
    def add_proximity_weights(self):
        proximity_k = 10
        for x, y in iterator2d():
            for x1, y1 in iterator_near(x, y, 0, 2):
                if(map_2d_bool[x1][y1] == True):
                    map_2d_weights[x][y].ostacle_prox =
                     distance_rel(x, y, x1, y1) * proximity_k
            for x1, y1 in iterator2d():
                map_2d_bool[x][y].obstacle_prox += map_2d[x][y] * (1/distance_rel(x, y, x1,y1)+1000)
                
        
                    
            
            
            
    
