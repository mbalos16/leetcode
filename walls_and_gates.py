'''
286. Walls and Gates
Solved
Medium
Topics
Companies

You are given an m x n grid rooms initialized with these three possible values.
    -1 A wall or an obstacle.
    0 A gate.
    INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.


Example 1:
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Example 2:
Input: rooms = [[-1]]
Output: [[-1]]
 

Constraints:
    m == rooms.length
    n == rooms[i].length
    1 <= m, n <= 250
    rooms[i][j] is -1, 0, or 231 - 1.
'''

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Define a list-like container with fast appends and pops on either end
        queue = deque([])

        # Define the distance step as 1.
        step_from_gate = 1
        
        # Define the matrix shape
        rooms_rows = len(rooms)
        rooms_cols = len(rooms[0])

        # Define what an empty room looks like
        empty_room = (2**31) -1

        # Define the four possible directions
        possible_directions = [(-1,0), (1,0), (0,1), (0,-1)]
        
        # Record the coordinates of the gates to the queue.
        for row in range(rooms_rows):
            for column in range(rooms_cols):
                if rooms[row][column] == 0:
                    queue.append([row, column])
        print(f"The gates are located at these coordinates: {queue}")


        while queue:
            # Number of nodes in the current iteration to be processed
            nodes_to_be_processed = len(queue)

            # For each node in the current nodes list
            for _ in range(nodes_to_be_processed):

                # Retrieves the nodes to be processed and remove them from the queue list
                node_1, node_2 = queue.popleft()

                for coord_x, coord_y in possible_directions:
                    # Boundary and condition check
                    # Ensuring the new coord are in the grid bounds 
                    if node_1 + coord_x >= 0:
                        if node_1 + coord_x < rooms_rows:
                            if node_2 + coord_y >= 0:
                                if node_2 + coord_y < rooms_cols:

                                    # Check if the new position is an empty room
                                    if rooms[ node_1 + coord_x ][ node_2 + coord_y ] == empty_room:

                                        # Fill the cell with its distance from the gate
                                        rooms[node_1 + coord_x][node_2 + coord_y] = step_from_gate

                                        # Add the new node to the queue for the next iteration
                                        queue.append((node_1 +coord_x, node_2 +coord_y))

            # Increment the distance from the gate by 1 any time.
            step_from_gate += 1