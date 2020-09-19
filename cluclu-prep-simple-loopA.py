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
                #elif ( not (edge1.direction == "RD" and edge2.direction == "DR") and not (edge1.direction == "UR" and edge2.direction == "RU") ):           
                else: 
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
    #print(curEdge.begin, curEdge.end, curEdge.direction)
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
    
#print("vector<vector<int>> startGoals = {")
#
#for e in eqClasses:
#    print("{")
#    for q in e:
#        print(f"{q},")
#    print("},")
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
        dummy1.append(minDistance+1)
        minDistance = INF
        for d2 in dummy2_edges:
            if (distance[d2][e]<minDistance):
                minDistance = distance[d2][e]
        dummy2.append(minDistance+1)

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
                distance[cEdge][v] = 999

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
                temp[i][j] = temp[i][j]
    
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

num = 3
parallel = list(range(0,len(edges)))
for i in range (0,len(edges)):
    if i in goalNums:
        parallel[i] = num
        num = num+1
        
print("vector<vector<int>> startGoals = {")
remain = goalNums
while (len(remain) > 0):
     newRemain = []
     curEdge = edges[remain[0]]
     curGroup = [ remain[0] ]
     for e in range (1,len(remain)):
        nextEdge = edges[remain[e]]
        if ( (curEdge.begin == nextEdge.begin and curEdge.end == nextEdge.end) or (curEdge.begin == nextEdge.end and curEdge.end == nextEdge.begin) ):
            curGroup.append(remain[e])
        else:
            newRemain.append(remain[e])
     print("{", end=' ')
     for e in range(0, len(curGroup)):
        print(f"{parallel[curGroup[e]]:>3}", end=',')
     print("},")
     remain = newRemain
print("};")
        

#for r in range(0,len(new_adj)):
#	print(''.join(str(new_adj[r])))
    
#print("    ", end=' ')
#for r in range(1,len(new_adj)+1):
#    temp = f"i{r}"
#    print(f"{temp:>4}", end=' ')
#print()

for r in range(0,len(new_adj)):
    #temp = f"i{r+1}"
    #print(f"{temp:!=4}", end=' ')
    print("{",end=' ')
    for s in range(0, len(new_adj)):
        temp = f"{new_adj[r][s]}"
        #if (new_adj[r][s]==0 or new_adj[r][s]==999):
        #    temp = ""
        if (new_adj[r][s]>0):
            if (new_adj[r][s]==1):
                temp = "0"
            else:
                temp = str(new_adj[r][s])
        print(f"{temp:>3}", end=',')
    print(" },")
    
#print(adj_mat)