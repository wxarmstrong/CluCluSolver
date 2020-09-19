class edge:
    def __init__(self, begin, end, direction):
        self.begin = begin
        self.end = end
        self.direction = direction
        self.out = []

class out:
    def __init__(self, target, weight):
        self.target = target
        self.weight = weight








#spade
grid = [
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,1,1,1,1,1,1,1,0,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],	
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,0,1,1,1,1,1,1,1,0,0],	
	[0,0,0,0,0,0,0,0,0,0,0],
]

#hawk
grid = [
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,1,1,1,1,1,1,1,0,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,2,1,2,1,1,1,0],
	[0,1,1,1,2,1,2,1,1,1,0],	
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,0,1,1,1,1,1,1,1,0,0],	
	[0,0,0,0,0,0,0,0,0,0,0],
]



#submarine
grid = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,0,0,1,1,1,0],
    [0,1,2,2,1,1,1,2,2,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,0,0,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0],
]

#bowtie (bounce)
grid = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,0,0,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,2,2,2,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,0,0,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0],
]

#bowtie (no bounce)
grid = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,0,0,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,0,0,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0],
]

#bear
grid = [
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,1,1,1,1,1,1,1,0,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,2,2,2,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],	
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,0,1,1,1,1,1,1,1,0,0],	
	[0,0,0,0,0,0,0,0,0,0,0],
]

#clown (no bounce)
grid = [
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,1,1,1,1,1,1,1,0,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],	
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,0,1,1,1,1,1,1,1,0,0],	
	[0,0,0,0,0,0,0,0,0,0,0],
]

#hawk (no bounce)
grid = [
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,1,1,1,1,1,1,1,0,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],	
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,0,1,1,1,1,1,1,1,0,0],	
	[0,0,0,0,0,0,0,0,0,0,0],
]

#hawk
grid = [
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,1,1,1,1,1,1,1,0,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,2,1,2,1,1,1,0],
	[0,1,1,1,2,1,2,1,1,1,0],	
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,0,1,1,1,1,1,1,1,0,0],	
	[0,0,0,0,0,0,0,0,0,0,0],
]

#spade
grid = [
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,1,1,1,1,1,1,1,0,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,2,1,1,1,1,0],
	[0,1,1,1,1,2,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],	
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,0,1,1,1,1,1,1,1,0,0],	
	[0,0,0,0,0,0,0,0,0,0,0],
]

#h
grid = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,0,1,1,1,1,0],
    [0,1,1,1,1,0,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,0,1,1,1,1,0],
    [0,1,1,1,1,0,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0],
]

#spider
grid = [
    [0,0,0,0,0, 0, 0,0,0,0,0],
    [0,1,1,1,1, 0, 1,1,1,1,0],
    [1,1,1,1,1, 1, 1,1,1,1,1],
    [1,1,1,1,1,1.5,1,1,1,2,2],
    [1,1,1,1,1,2.5,1,1,1,1,1],
    [1,1,1,1,1,2.5,1,1,1,1,1],
    [2,2,1,1,1,1.5,1,1,1,1,1],
    [1,1,2,2,1, 1, 1,2,2,1,1],
    [0,1,1,1,1, 0, 1,1,1,1,0],
    [0,0,0,0,0, 0, 0,0,0,0,0],
]

#circuit
grid = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,0,1,1,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,1,2,2,1,1,1,2,2,1,1],
    [1,2,1,1,1,1,1,1,1,2,1],
    [1,2,1,1,1,1,1,1,1,2,1],
    [1,1,2,2,1,1,1,2,2,1,1],
    [1,1,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,0,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0],
]



#nova
grid = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,0,1,1,1,1,0],
    [1,1,1,2,2,1,2,2,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,2,1,2,1,2,1,2,1,2,1],
    [1,2,1,2,1,2,1,2,1,2,1],
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,2,2,1,2,2,1,1,1],
    [0,1,1,1,1,0,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0],
]

#h
grid = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,0,1,1,1,1,0],
    [0,1,1,1,1,0,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1.5,2.5,1.5,1,1.5,2.5,1.5,1,0],
    [0,1,1,1,2.5,1,2.5,1,1,1,0],
    [0,1,2,2,1,1,1,2,2,1,0],
    [0,1,1,1,1,0,1,1,1,1,0],
    [0,1,1,1,1,0,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0],
]

#spider
grid = [
    [ 0,  0, 0,0,0, 0, 0,0,0,0,0],
    [ 0,  1, 1,1,1, 0, 1,1,1,1,0],
    [ 1,  1, 1,1,1, 1, 1,1,1,1,1],
    [ 1,  1, 1,1,1,1.5,1,1,1,2,2],
    [ 1, 1.5,1,1,1,2.5,1,1,1,1,1],
    [ 1, 2.5,1,1,1,2.5,1,1,1,2,1],
    [2.5,1.5,1,1,1,1.5,1,1,1,2,1],
    [ 1,  1, 2,2,1, 1, 1,2,2,1,1],
    [ 0,  1, 1,1,1, 0, 1,1,1,1,0],
    [ 0,  0, 0,0,0, 0, 0,0,0,0,0],
]

#2552
grid = [
    [0  ,0  ,0,0,  0,  0,0,  0,  0,0,  0  ],
    [0  ,1  ,1,1,  1,  0,1,  1,  1,1,  0  ],
    [1  ,1  ,1,1,  1,  1,1,  1,  1,1,  1  ],
    [1.5,2.5,1,1.5,2.5,1,2.5,1.5,1,1,  1  ],
    [1,  1.5,1,1.5,1,  1,1,  2.5,1,2.5,1  ],
    [1,  2.5,1,2.5,1,  1,1,  1.5,1,1.5,1  ],
    [1,  1,  1,1.5,2.5,1,1.5,2.5,1,2.5,1.5],
    [1,  1,  1,1,  1,  1,1,  1,  1,1,  1  ],
    [0,  1,  1,1,  1,  0,1,  1,  1,1,  0  ],
    [0,  0,  0,0,  0,  0,0,  0,  0,0,  0  ],
]

#clover 
grid = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,0,1,1,1,1,0],
    [0,1,1,1,1,0,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,2,1,1,2,1,1,2,1,0],
    [0,1,2,1,1,2,1,1,2,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,0,1,1,1,1,0],
    [0,1,1,1,1,0,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0],
]

#nova
grid = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,0,1,1,1,1,0],
    [1,1,1,2,2,1,2,2,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,2,1,2,1,2,1,2,1,2,1],
    [1,2,1,2,1,2,1,2,1,2,1],
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,2,2,1,2,2,1,1,1],
    [0,1,1,1,1,0,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0],
]

#clown
grid = [
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,1,1,1,1,1,1,1,0,0],
	[0,1,1,1,1,2,1,1,1,1,0],
	[0,1,1,1,1,2,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],	
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,2,2,1,2,2,1,1,0],
	[0,0,1,1,1,1,1,1,1,0,0],	
	[0,0,0,0,0,0,0,0,0,0,0],
]


#house
grid = [
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,1,1,1,1,1,1,1,0,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],	
	[0,1,1,2,2,1,2,2,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,0,1,1,1,1,1,1,1,0,0],	
	[0,0,0,0,0,0,0,0,0,0,0],
] 

blackholes = [60]

rows = len(grid)
cols = len(grid[0])

edges = []

#create all edges
for r in range(0,rows):
    for c in range(0,cols):
        if (grid[r][c] >=1):
            posNum = r*cols + c
            #straight
            #do not allow straight edges originating from black holes
            if not (posNum in blackholes):
                #straight up
                if (grid[r-1][c] >= 1 and grid[r][c]+grid[r-1][c]!=4):
                    edges.append( edge(posNum, posNum-cols, "straight") )
                #straight down
                if (grid[r+1][c] >= 1 and grid[r][c]+grid[r+1][c]!=4):
                    edges.append( edge(posNum, posNum+cols, "straight") )
                #straight left
                if (grid[r][(c-1)%cols] >= 1 and grid[r][c]+grid[r][abs((c-1)%cols)]!=4):
                    if (c==0):
                        edges.append( edge(posNum, posNum+cols-1, "straight") )
                    else:
                        edges.append( edge(posNum, posNum-1, "straight") )
                #straight right
                if (grid[r][(c+1)%cols] >= 1 and grid[r][c]+grid[r][(c+1)%cols]!=4):
                    if (c==cols-1):
                        edges.append( edge(posNum, posNum-cols+1, "straight") )
                    else:
                        edges.append ( edge(posNum, posNum+1, "straight") )
            #up-left
            if (grid[r+1][c] >=1 and grid[r][abs((c-1)%cols)] >= 1 and grid[r][c]+grid[r+1][c]!=4 and grid[r][c]+grid[r][abs((c-1)%cols)]!=4):
                if (c!=0):
                    edges.append( edge(posNum, posNum-1, "UL") )
            #up-right
            if (grid[r+1][c] >=1 and grid[r][(c+1)%cols] >= 1 and grid[r][c]+grid[r+1][c]!=4 and grid[r][c]+grid[r][(c+1)%cols]!=4):
                if (c!=cols-1):
                    edges.append( edge(posNum, posNum+1, "UR") )
            #down-left
            if (grid[r-1][c] >=1 and grid[r][abs((c-1)%cols)] >= 1 and grid[r][c]+grid[r-1][c]!=4 and grid[r][c]+grid[r][abs((c-1)%cols)]!=4):
                if (c!=0):
                    edges.append( edge(posNum, posNum-1, "DL") )
            #down-right
            if (grid[r-1][c] >=1 and grid[r][(c+1)%cols] >= 1 and grid[r][c]+grid[r-1][c]!=4 and grid[r][c]+grid[r][(c+1)%cols]!=4):
                if (c!=cols-1):
                    edges.append( edge(posNum, posNum+1, "DR" ) )
            #left-up
            if (grid[r][(c+1)%cols] >=1 and grid[r-1][c] >= 1 and grid[r][c]+grid[r][(c+1)%cols]!=4 and grid[r][c]+grid[r-1][c]!=4):
                edges.append( edge(posNum, posNum-cols, "LU") )
            #left-down
            if (grid[r][(c+1)%cols] >=1 and grid[r+1][c] >= 1 and grid[r][c]+grid[r][(c+1)%cols]!=4 and grid[r][c]+grid[r+1][c]!=4):   
                edges.append( edge(posNum, posNum+cols, "LD") )
            #right-up
            if (grid[r][abs((c-1)%cols)] >=1 and grid[r-1][c] >= 1 and grid[r][c]+grid[r][abs((c-1)%cols)]!=4 and grid[r][c]+grid[r-1][c]!=4):
                edges.append( edge(posNum, posNum-cols, "RU") )
            #right-down
            if (grid[r][abs((c-1)%cols)] >=1 and grid[r+1][c] >= 1 and grid[r][c]+grid[r][abs((c-1)%cols)]!=4 and grid[r][c]+grid[r+1][c]!=4):
                edges.append( edge(posNum, posNum+cols, "RD") )

#banned edges


#purple
banned = [
    [37, 38, "DR"],
    [39, 38, "DL"],
    [70, 71, "UR"],
    [72, 71, "UL"],
]

#brown
banned = [
    [44, 55, "LD"],
    [55, 44, "LU"],
    [46, 57, "RD"],
    [57, 46, "RU"],
    [55, 56, "DR"],
    [57, 56, "DL"],
    [44, 45, "UR"],
    [46, 45, "UL"],
    
    [52, 63, "LD"],
    [63, 52, "LU"],
    [54, 65, "RD"],
    [65, 54, "RU"],
    [63, 64, "DR"],
    [65, 64, "DL"],
    [52, 53, "UR"],
    [54, 53, "UL"],
]

banned = [
]

for b in banned:
    #print(b)
    for e in edges:
        #print(f"curEdge: {e.begin},{e.end}")
        if e.begin == b[0] and e.end == b[1] and e.direction == b[2]:
            #print(f"removing {b}")
            edges.remove(e)
        

# for each edge, determine which other edges are adjacent & their distance (# of frames)
# this includes wall bounces and rubber bounces
# disregard any impossible edges
# for now (to experiment):
# - only disregard the RD to DR moves

WALL_COST = 2
RUBBER_COST = 2
GENERIC_COST = 1

for e in range(0, len(edges) ):
    edge1 = edges[e]
    for f in range(0, len(edges) ):
        edge2 = edges[f]
        if (edge1.end == edge2.begin and e!=f):
            #bounce
            if (edge1.begin == edge2.end):
                if (edge2.direction == "straight"):
                    #check for wall
                    destination = 2*(edge1.end) - edge1.begin
                    d_row = destination // cols
                    d_col = destination % cols
                    if (grid[d_row][d_col]==0):
                        edge1.out.append( out(f, WALL_COST) )
                    #check for rubber
                    elif (grid[d_row][d_col]==2):
                        e2_row = edge1.end // cols
                        e2_col = edge1.end % cols
                        if (grid[e2_row][e2_col]==2):
                            edge1.out.append( out(f, RUBBER_COST) )
            else:
                if (edge1.direction == "straight" and edge2.direction == "straight" ):
                    if (edge1.end - edge1.begin == edge2.end - edge2.begin):
                        edge1.out.append( out(f, GENERIC_COST) )
                elif (edge1.direction == "straight"):
                    #left 
                    if edge1.end - edge1.begin == -1:
                        if (edge2.direction == "LU" or edge2.direction == "LD"):
                            edge1.out.append( out(f, GENERIC_COST) )
                    #right
                    elif edge1.end - edge1.begin == 1:
                        if (edge2.direction == "RU" or edge2.direction == "RD"):
                            edge1.out.append( out(f, GENERIC_COST) )
                    #up
                    elif edge1.end - edge1.begin == -1*cols:
                        if (edge2.direction == "UL" or edge2.direction == "UR"):
                            edge1.out.append( out(f, GENERIC_COST) )
                    #down
                    elif edge1.end - edge1.begin == cols:
                        if (edge2.direction == "DL" or edge2.direction == "DR"):
                            edge1.out.append( out(f, GENERIC_COST) )
           
                elif (edge2.direction == "straight"):
                    #left
                    if edge2.end - edge2.begin == -1:
                        if (edge1.direction == "UL" or edge1.direction == "DL"):
                            edge1.out.append( out(f, GENERIC_COST) )
                    #right
                    if edge2.end - edge2.begin == 1:
                        if (edge1.direction == "UR" or edge1.direction == "DR"):
                            edge1.out.append( out(f, GENERIC_COST) )
                    #up
                    if edge2.end - edge2.begin == -1*cols:
                        if (edge1.direction == "LU" or edge1.direction == "RU"):
                            edge1.out.append( out(f, GENERIC_COST) )
                    #down
                    if edge2.end - edge2.begin == cols:
                        if (edge1.direction == "LD" or edge1.direction == "RD"):
                            edge1.out.append( out(f, GENERIC_COST) )
                elif ( not (edge1.direction == "RD" and edge2.direction == "DR") and not (edge1.direction == "UR" and edge2.direction == "RU") ):           
                #else: 
                    #left
                    if (edge1.direction == "UL" or edge1.direction == "DL"):
                        if (edge2.direction == "LU" or edge2.direction == "LD"):
                            edge1.out.append( out(f, GENERIC_COST) )
                    #right
                    if (edge1.direction == "UR" or edge1.direction == "DR"):
                        if (edge2.direction == "RU" or edge2.direction == "RD"):
                            edge1.out.append( out(f, GENERIC_COST) )
                    #up
                    if (edge1.direction == "LU" or edge1.direction == "RU"):
                        if (edge2.direction == "UL" or edge2.direction == "UR"):
                            edge1.out.append( out(f, GENERIC_COST) )
                    #down
                    if (edge1.direction == "LD" or edge1.direction == "RD"):
                        if (edge2.direction == "DL" or edge2.direction == "DR"):
                            edge1.out.append( out(f, GENERIC_COST) )
INF = 999
adj_mat = [[INF for i in range(0,len(edges))] for j in range(0,len(edges))]

for i in range(0,len(edges)):
    curEdge = edges[i]
    print(curEdge.begin, curEdge.end, curEdge.direction)
    for j in range(0,len(curEdge.out)):
        curOut = curEdge.out[j]
        outNum = curOut.target
        outWeight = curOut.weight
        adj_mat[i][outNum] = outWeight

#print(adj_mat)
for i in range(0,len(adj_mat)):
    adj_mat[i][i] = 0

# Floyd Warshall Algorithm in python
# The number of vertices
nV = len(edges)

# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance

# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

distance = floyd_warshall(adj_mat)

#print_solution(distance)

# Trim the distance matrix to only include goals
#  Make note of which rows correspond to members of the same goal
# Add the dummy node & P1/P2 depot
# For each set, rotate the distance matrix rows and set 0 distance edges for sequence














#subtest
goals = [
    [37,38],
    [47,48],[49,50],[51,52],[52,53],
    [56,57],[62,63],
    [67,68],[72,73],[73,74],[74,75],
                    [41,52],
    [46,57],[47,58],[48,59],[49,60],[50,61],[51,62],[52,63],
    [68,79],[69,80],[70,81],[71,82],[72,83],[74,85],
]

#submarine
goals = [
    [37,38],
    [47,48],[49,50],[51,52],[52,53],
    [56,57],[62,63],
    [67,68],[72,73],[73,74],[74,75],
    
    [37,48],[38,49],[41,52],
    [46,57],[47,58],[48,59],[49,60],[50,61],[51,62],[52,63],
    [62,73],[63,74],
    [68,79],[69,80],[70,81],[71,82],[72,83],[74,85],
]

#bowtie
goals = [
    [34,35],[35,36],[40,41],[41,42],
    [45,46],[47,48],[50,51],[52,53],
    [56,57],[59,60],[60,61],[63,64],
    [67,68],[69,70],[70,71],[71,72],[72,73],[74,75],
    
    [24,35],[30,41],
    [36,47],[40,51],
    [48,59],[49,60],[50,61],
    [59,70],[61,72],
    [68,79],[69,80],[71,82],[73,84],[74,85]
]

#koala
goals = [
    [23,24],[24,25],[29,30],[30,31],
    [34,35],[41,42],
    [46,47],[51,52],
    [57,58],[62,63],
    [69,70],[70,71],[71,72],[72,73],
    
    [13,24],[19,30],
    [25,36],[26,37],[27,38],[28,39],[29,40],
    [35,46],[41,52],
    [58,69],[60,71],[62,73],
    [70,81],[71,82],[72,83],
]

#glasses
goals = [
    [23,24],                                [30,31],
    [34,35],                                [41,42],
    [45,46],[46,47],[48,49],[49,50],[51,52],[52,53],
            [57,58],[59,60],[60,61],[62,63],
            [68,69],[70,71],[71,72],[73,74],
            
            [36,47],[37,48],        [39,50],[40,51],
    [46,57],                [49,60],                [52,63],
            [69,80],[70,81],        [72,83],[73,84],
]

#bear
goals = [
    [24,25],[25,26],[28,29],[29,30],
    [36,37],[39,40],
    [46,47],[51,52],
    [57,58],[62,63],
    [69,70],[70,71],[71,72],[72,73],
    [81,82],[82,83],
    
    [14,25],[18,29],
    [25,36],[26,37],[27,38],[28,39],[29,40],
    [36,47],[40,51],
    [58,69],[60,71],[62,73],
    [70,81],[71,82],[72,83],
    [82,93],
]



#hawk
goals = [
    [26,27],[28,29],
    [37,38],[38,39],
    [45,46],[52,53],
    [57,58],[62,63],
    [70,71],[71,72],
    [80,81],[81,82],[82,83],[83,84],
    
    [16,27],[17,28],
    [28,39],
    [35,46],[36,47],[37,48],[39,50],[40,51],[41,52],
    [46,57],[52,63],
    [58,69],[59,70],[61,72],[62,73],
    [70,81],[71,82],[72,83],
    [81,92],[83,94],
]

#spade
goals = [
    [26,27],[27,28],
    [36,37],[39,40],
    [46,47],[51,52],
    [57,58],[59,60],[60,61],[62,63],
    [70,71],[71,72],
    [80,81],[83,84],
    
    [16,27],
    [26,37],[28,39],
    [36,47],[40,51],
    [49,60],
    [58,69],[59,70],[60,71],[61,72],[62,73],
    [70,81],[72,83],
    [81,92],[82,93],[83,94],
]

#h
goals = [
    [23,24],[25,26],[28,29],[30,31],
    [34,35],[36,37],[39,40],[41,42],
    [45,46],                [52,53],
    [56,57],                [63,64],
    [67,68],[69,70],[72,73],[74,75],
    [78,79],[80,81],[83,84],[85,86],
    
    [13,24],[14,25],[18,29],[19,30],
    [37,48],[38,49],[39,50],
    [59,70],[60,71],[61,72],
    [79,90],[80,91],[84,95],[85,96],
]

#yotsuba
goals = [
    [23,24],[24,25],[29,30],[30,31],
    [34,35],[36,37],[39,40],[41,42],
    [67,68],[69,70],[72,73],[74,75],
    [79,80],[80,81],[83,84],[84,85],
    
    [13,24],[19,30],
    [25,36],[29,40],
    [35,46],[36,47],[40,51],[41,52],
    [57,68],[58,69],[62,73],[63,74],
    [68,79],[74,85],
    [80,91],[84,95],
]

#stonehenge
goals = [
    [24,25],[25,26],[28,29],[29,30],
    [48,49],[49,50],
    [56,57],[57,58],[59,60],[60,61],[62,63],[63,64],
    [79,80],[80,81],[83,84],[84,85],
    
    [14,25],[18,29],
    [25,36],[29,40],
    [38,49],
    [46,57],[49,60],[52,63],
    [57,68],[60,71],[63,74],
    [69,80],[73,84],
    [80,91],[84,95],
]





#circuit
goals = [
    [33,34],[34,35],[36,37],[39,40],[41,42],[42,43],
    [66,67],[67,68],[69,70],[72,73],[74,75],[75,76],
    
    [13,24],[14,25],[18,29],[19,30],
    [26,37],[28,39],
    [70,81],[72,83],
    [79,90],[80,91],[84,95],[85,96],
]





#h
goals = [
    [23,24],[25,26],[28,29],[30,31],
    [34,35],[36,37],[39,40],[41,42],
    [45,46],                [52,53],
    [56,57],                [63,64],
    [67,68],[69,70],[72,73],[74,75],
    [78,79],[80,81],[83,84],[85,86],
    
    [13,24],[14,25],[18,29],[19,30],
    [37,48],[38,49],[39,50],
    [59,70],[60,71],[61,72],
    [79,90],[80,91],[84,95],[85,96],
]

#spider
goals = [
    [25,26],[28,29],
    [34,35],[41,42],
    [46,47],[51,52],
    [57,58],[62,63],
    [67,68],[74,75],
    [80,81],[83,84],
    
    [26,37],[27,38],[28,39],
    [35,46],[41,52],
    [49,60],
    [57,68],[63,74],
    [70,81],[71,82],[72,83],
]

#2552
goals = [
    [24,25],[29,30],
    [34,35],[41,42],
    [48,49],[49,50],
    [59,60],[60,61],
    [67,68],[74,75],
    [79,80],[84,85],
    
    [13,24],[19,30],
    [27,38],
    [35,46],[41,52],
    [57,68],[63,74],
    [71,82],
    [79,90],[85,96],
]

#clover
goals = [
    [34,35],[36,37],[39,40],[41,42],
    [47,48],[50,51],
    [58,59],[61,62],
    [67,68],[69,70],[72,73],[74,75],
    
    [24,35],[25,36],[29,40],[30,41],
    [35,46],[36,47],[37,48],[38,49],[39,50],[40,51],[41,52],
    [57,68],[58,69],[59,70],[60,71],[61,72],[62,73],[63,74],
    [68,79],[69,80],[73,84],[74,85],
]

#nova
goals = [
    [24,25],[29,30],
    [34,35],[41,42],
    [67,68],[74,75],
    [79,80],[84,85],
    
    [24,35],[27,38],[30,41],
    [34,45],[36,47],[38,49],[40,51],[42,53],
    [56,67],[58,69],[60,71],[62,73],[64,75],
    [68,79],[71,82],[74,85],
]

#clown
goals = [
    [35,36],[36,37],[39,40],[40,41],
    [45,46],[48,49],[49,50],[52,53],
    [57,58],[58,59],[61,62],[62,63],
    [70,71],[71,72],
    [81,82],[82,83],
    
    [25,36],[29,40],
    [35,46],[37,48],[39,50],[41,52],
    [46,57],[48,59],[50,61],[52,63],
    [58,69],[60,71],[62,73],
    [82,93],
]

#house
goals = [
	[25,26],[28,29],
	[35,36],[40,41],
	[45,46],[52,53],
	[57,58],[62,63],
	[68,69],[73,74],
	[79,80],[84,85],
	
	[15,26],[16,27],[17,28],
	[25,36],[29,40],
	[35,46],[41,52],
	[46,57],[47,58],[48,59],[49,60],[50,61],[51,62],[52,63],
	[80,91],[81,92],[82,93],[83,94],[84,95]
]


goalNums = []
eqClasses = []

# Note which of the edges represent goals,
#  and partition each version of the same goal.
for g in goals:
    g1 = g[0]
    g2 = g[1]
    curEqClass = []
    for e in range(0,len(edges)):
        curEdge = edges[e]
        e1 = curEdge.begin
        e2 = curEdge.end
        if ( (e1==g1 and e2==g2) or (e1==g2 and e2==g1) ):
            goalNums.append(e)
            curEqClass.append(e)
    eqClasses.append(curEqClass)
    
print("vector<vector<int>> startGoals = {")

for e in eqClasses:
    print("{")
    for q in e:
        print("f{q},")
    print("},")
#print(eqClasses)

#print ("lol")
#for e in range(0,len(edges)):
 #   if (e in goalNums):
  #      curEdge = edges[e]
   #     print(curEdge.begin, curEdge.end, curEdge.direction)
    
# For each member of each class, shift their corresponding
#  rows in the distance matrix to that of the previous member.
#  Then add a 0-distance edge from each of them to that of the following member.

#print(distance)

#bonus
P1_START = [1,2]
P2_START = [9,2]

P1_POS = P1_START[1]*cols+P1_START[0]
P2_POS = P2_START[1]*cols+P2_START[0]

dummy0 = [0,1,1]
for g in range(0,len(goalNums)):
    dummy0.append(999)
    
dummy1 = [999,0,999]
dummy2 = [999,999,0]
dummy1_edges = []
dummy2_edges = []

for e in range( 0,len(edges) ):
    curEdge = edges[e]
    if (curEdge.begin == P1_POS and curEdge.direction == "straight"):
        dummy1_edges.append(e)
    if (curEdge.begin == P2_POS and curEdge.direction == "straight"):
        dummy2_edges.append(e)

#print(P1_POS)
#print(P2_POS)
#print(len(edges))
for e in range(0, len(edges) ):
    if (e in goalNums):
        minDistance = INF
        for d1 in dummy1_edges:
            if (distance[d1][e]<minDistance):
                minDistance = distance[d1][e]
        #print("Distance from " + str(P1_POS) + " to " + str(edges[e].begin) + "->" + str(edges[e].end) + " (" + edges[e].direction + ") = " + str(minDistance) )
        dummy1.append(100+minDistance+1)
        minDistance = INF
        for d2 in dummy2_edges:
            if (distance[d2][e]<minDistance):
                minDistance = distance[d2][e]
        dummy2.append(100+minDistance+1)

new_adj = [dummy0,dummy1,dummy2]
#print(new_adj)


for p in range (0,len(eqClasses)):
    curClass = eqClasses[p]
    lowMax = 999
    mins = []
    changed = 0
    for c in range(0,len(curClass)):
        cEdge = curClass[c]
        curMin = 999
        curMax = 0
        for e in range(0,len(edges)):
            if not (e in curClass):
                edgeD = distance[e][cEdge] + distance[cEdge][e]
                if (edgeD < curMin):
                    curMin = edgeD
                if (edgeD > curMax):
                    curMax = edgeD
        if (curMax > lowMax):
            lowMax = curMax
        mins.append(curMin)
    for c in range(0,len(curClass)):
        cEdge = curClass[c]
        if (mins[c] >= lowMax and changed != len(curClass)-1):
            changed = changed + 1
            for v in range(0,len(distance[cEdge])):
                distance[cEdge][v] = 899

for p in range( 0,len(eqClasses) ):
    curClass = eqClasses[p]
    n = len(curClass)
    temp = []
    
    for i in range(1,n):
        curIdx = curClass[i]
        temp.append(distance[curIdx])
    temp.append( distance[curClass[0]] )
    
    lastRow = temp[n-1]
    firstIdx = curClass[0]
    lastRow[firstIdx] = 0
    
    for i in range(0,n-1):
        curRow = temp[i]
        idx = curClass[i+1]
        curRow[idx] = 0
       
    for i in range(0,n):
        curRow = temp[i]
        for j in range(0,len(curRow)):
            if curRow[j] == 0:
                temp[i][j] = 1
            else:
                temp[i][j] = temp[i][j] + 100
    
    for i in range(0,n):
        curIdx = curClass[i]
        distance[curIdx] = temp[i]

for e1 in range(0, len(edges) ):
	if (e1 in goalNums):
		curRow = [1,999,999]
		for e2 in range(0, len(edges) ):
			if (e2 in goalNums):
				curRow.append(distance[e1][e2])
		new_adj.append(curRow)
		
for i in range(0,len(new_adj)):
    new_adj[i][i] = 0
        
#print("test")
#print(new_adj)        
        
edgeNum = len(new_adj)

#for i in range(1,edgeNum):
#    for j in range(3,edgeNum):
#        if (i!=j and j>0 and new_adj[i][j]>0):
#            new_adj[i][j] += 100
#            #if (i==2):
#             #   new_adj[i][j] += 3*101
#        elif (i!=j and j>2 and new_adj[i][j]==0):
#            new_adj[i][j] = 1
			
#print(new_adj)

for e in range(0,len(edges)):
    if (e in goalNums):
        curEdge = edges[e]
        print(str(curEdge.begin) + "->" + str(curEdge.end) + " (" + curEdge.direction + ")")

for r in range(0,len(new_adj)):
	print(''.join(str(new_adj[r])))
    
print("    ", end=' ')
for r in range(1,len(new_adj)+1):
    temp = f"i{r}"
    print(f"{temp:>4}", end=' ')
print()

for r in range(0,len(new_adj)):
    #temp = f"i{r+1}"
    #print(f"{temp:!=4}", end=' ')
    for s in range(0, len(new_adj)):
        temp = f"{new_adj[r][s]}"
        #if (new_adj[r][s]==0 or new_adj[r][s]==999):
        #    temp = ""
        if (new_adj[r][s]>0):
            if (new_adj[r][s]==1):
                temp = "0"
            else:
                temp = str(new_adj[r][s])
        print(f"{temp:>3}", end=' ')
    print()
    
#print(adj_mat)