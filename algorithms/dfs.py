"""
Depth-First Search (DFS) Algorithm
Time Complexity: O(V + E) where V is vertices and E is edges
Space Complexity: O(V)
"""

def dfs(graph, start, visited=None):
    """
    Performs depth-first search on a graph (recursive).
    
    Args:
        graph: Dictionary representing adjacency list
        start: Starting vertex
        visited: Set of visited vertices (used in recursion)
    
    Returns:
        List of vertices in DFS traversal order
    """
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    # Visit all neighbors
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result


def dfs_iterative(graph, start):
    """
    Performs depth-first search on a graph (iterative).
    
    Args:
        graph: Dictionary representing adjacency list
        start: Starting vertex
    
    Returns:
        List of vertices in DFS traversal order
    """
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Add neighbors to stack in reverse order
            # to maintain left-to-right traversal
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result


def has_cycle(graph):
    """
    Detects if a directed graph has a cycle using DFS.
    
    Args:
        graph: Dictionary representing adjacency list
    
    Returns:
        True if cycle exists, False otherwise
    """
    visited = set()
    rec_stack = set()
    
    def dfs_cycle(vertex):
        visited.add(vertex)
        rec_stack.add(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                if dfs_cycle(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        
        rec_stack.remove(vertex)
        return False
    
    for vertex in graph:
        if vertex not in visited:
            if dfs_cycle(vertex):
                return True
    
    return False


if __name__ == "__main__":
    # Test DFS algorithm
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("Graph:", graph)
    print("\nDFS traversal (recursive) starting from 'A':")
    print(dfs(graph, 'A'))
    
    print("\nDFS traversal (iterative) starting from 'A':")
    print(dfs_iterative(graph, 'A'))
    
    # Test cycle detection
    cyclic_graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    print("\nCyclic graph:", cyclic_graph)
    print("Has cycle:", has_cycle(cyclic_graph))
