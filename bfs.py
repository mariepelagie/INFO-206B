# Breadth-first-search using the Vertex class.

from collections import deque

# Run bfs and find the path from the Vertex start to the Vertex goal.
# Return that path as a list of Vertex objects.  If there is no path, return None.
def bfs(start, goal):
    frontier = deque()      # the queue of vertices we're going to visit next
    frontier.append(start)  # put the start vertex in our list of those to visit
    backpointer = {}
    backpointer[start] = None   # the start vertex has no backpointer
    backpointer_movie = {}
    backpointer_movie[start] = None
        
    # Keep going while there's at least one visited vertex that we have not
    # explored from yet.
    while len(frontier) > 0: 
        vertex = frontier.popleft()
        
        if vertex == goal: # If we're done, retrace the path from the goal to the start.
       
            path = []        
            while vertex != None: # only our start should have a None backpointer along our path
                if( backpointer_movie[vertex] != None ):
                    path.append(vertex.name + " (" + backpointer_movie[vertex] + ")")
                else:
                    path.append(vertex.name)
               
                vertex = backpointer[vertex]
                #print( vertex.name, backpointer_movie[vertex] )
            return path
        
        else: # keep exploring
            i = 0;
            for neighbor in vertex.adjacent:
                movie = vertex.edge[i]
                # Visit the vertex only if it hasn't been visited yet.  It has been
                # visited if and only if it has a backpointer.
                if not graph[neighbor] in backpointer:
                    # Set up the backpointer.  This will only happen once for each vertex,
                    # since a vertex is put in the frontier and visited only once.
                    backpointer[graph[neighbor]] = vertex
                    backpointer_movie[graph[neighbor]] = movie
                    frontier.append(graph[neighbor])
                i = i + 1
                    
    # If we get here, we've run out of vertices to explore before reaching the goal.
    return None
