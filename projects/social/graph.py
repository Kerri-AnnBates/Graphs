"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}  # This is our adjacency list

    def add_vertex(self, vertex_id):
        """
                Add a vertex to the graph.
                """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
                Add a directed edge to the graph from v1 to v2
                """
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
                Get all neighbors (edges) of a vertex.
                """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
                Print each vertex in breadth-first order
                beginning from starting_vertex.
                """
        # Create a q and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dft(self, starting_vertex):
        """
                Print each vertex in depth-first order
                beginning from starting_vertex.
                """
        # Create a stack
        stk = Stack()
        stk.push([starting_vertex])
        visited = set()

        # Start at the starting vertex
        while stk.size() > 0:
            # Explore that vertex
            path = stk.pop()

            # has node been visited?
            if path[-1] not in visited:
                print(path[-1])
                visited.add(path[-1])

                # Is there a neighbor to this vertex that I can explore?
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    stk.push(new_path)

    def dft_recursive(self, starting_vertex, visited=None):
        """
                Print each vertex in depth-first order
                beginning from starting_vertex.

                This should be done using recursion.
                """

        if visited is None:
            visited = set()

        # Base Case: if vertex has already been visited
        if starting_vertex in visited:
            return

        # print the vertex
        print(starting_vertex)
        visited.add(starting_vertex)  # add to visited list

        # for each neighbor, run the function on it
        for vert in self.get_neighbors(starting_vertex):
            self.dft_recursive(vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
                Return a list containing the shortest path from
                starting_vertex to destination_vertex in
                breath-first order.
                """
        # Create a q and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                # Check if we have reached our destination and return path
                if path[-1] == destination_vertex:
                    return path

                # mark as visited
                visited.add(path[-1])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
                Return a list containing a path from
                starting_vertex to destination_vertex in
                depth-first order.
                """
        # Create a stack
        stk = Stack()
        stk.push([starting_vertex])
        visited = set()

        # Start at the starting vertex
        while stk.size() > 0:
            # Explore that vertex
            path = stk.pop()

            # has node been visited?
            if path[-1] not in visited:

                if path[-1] == destination_vertex:
                    return path

                visited.add(path[-1])

                # Is there a neighbor to this vertex that I can explore?
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    stk.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=[]):
        """
                Return a list containing a path from
                starting_vertex to destination_vertex in
                depth-first order.

                This should be done using recursion.
                """

        if visited is None:
            visited = set()

        # Add vertex to visited
        visited.add(starting_vertex)
        # make copy of path, add vertex to path
        path = path + [starting_vertex]

        # if the destination is reached, return the path
        if starting_vertex == destination_vertex:
            return path

        # Run dfs search function on neighbors
        for vert in self.get_neighbors(starting_vertex):
            if vert not in visited:
                new_path = self.dfs_recursive(
                    vert, destination_vertex, visited, path)
                if new_path:
                    return new_path


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    """
	Should print:
		{1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
	"""
    print(graph.vertices)

    """
	Valid BFT paths:
		1, 2, 3, 4, 5, 6, 7
		1, 2, 3, 4, 5, 7, 6
		1, 2, 3, 4, 6, 7, 5
		1, 2, 3, 4, 6, 5, 7
		1, 2, 3, 4, 7, 6, 5
		1, 2, 3, 4, 7, 5, 6
		1, 2, 4, 3, 5, 6, 7
		1, 2, 4, 3, 5, 7, 6
		1, 2, 4, 3, 6, 7, 5
		1, 2, 4, 3, 6, 5, 7
		1, 2, 4, 3, 7, 6, 5
		1, 2, 4, 3, 7, 5, 6
	"""
    graph.bft(1)

    """
	Valid DFT paths:
		1, 2, 3, 5, 4, 6, 7
		1, 2, 3, 5, 4, 7, 6
		1, 2, 4, 7, 6, 3, 5
		1, 2, 4, 6, 3, 5, 7
	"""
    graph.dft(1)
    graph.dft_recursive(1)

    """
	Valid BFS path:
		[1, 2, 4, 6]
	"""
    print(graph.bfs(1, 6))

    """
	Valid DFS paths:
		[1, 2, 4, 6]
		[1, 2, 4, 7, 6]
	"""
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
