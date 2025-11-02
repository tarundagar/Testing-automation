"""
Breadth-First Search (BFS) Algorithm
Time Complexity: O(V + E) where V is vertices and E is edges
Space Complexity: O(V)
"""

from collections import deque

def bfs(graph, start):
    """
    Performs breadth-first search on a graph.
    
    Args:
        graph: Dictionary representing adjacency list
        start: Starting vertex
    
    Returns:
        List of vertices in BFS traversal order
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        # Visit all neighbors
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


def bfs_shortest_path(graph, start, end):
    """
    Finds shortest path between two vertices using BFS.
    
    Args:
        graph: Dictionary representing adjacency list
        start: Starting vertex
        end: Ending vertex
    
    Returns:
        Shortest path as list of vertices, or None if no path exists
    """
    if start == end:
        return [start]
    
    visited = {start}
    queue = deque([(start, [start])])
    
    while queue:
        vertex, path = queue.popleft()
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                
                if neighbor == end:
                    return new_path
                
                queue.append((neighbor, new_path))
    
    return None


if __name__ == "__main__":
    # Test BFS algorithm
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("Graph:", graph)
    print("\nBFS traversal starting from 'A':")
    print(bfs(graph, 'A'))
    
    print("\nShortest path from 'A' to 'F':")
    print(bfs_shortest_path(graph, 'A', 'F'))
