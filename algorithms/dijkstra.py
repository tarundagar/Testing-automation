"""
Dijkstra's Shortest Path Algorithm
Time Complexity: O((V + E) log V) with priority queue
Space Complexity: O(V)
"""

import heapq

def dijkstra(graph, start):
    """
    Finds shortest paths from start vertex to all other vertices.
    
    Args:
        graph: Dictionary where graph[u] = [(v, weight), ...]
        start: Starting vertex
    
    Returns:
        Dictionary of shortest distances from start to each vertex
    """
    # Initialize distances with infinity
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Priority queue: (distance, vertex)
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        # Skip if already visited
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        # Check all neighbors
        for neighbor, weight in graph.get(current_vertex, []):
            distance = current_distance + weight
            
            # Update distance if shorter path found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances


def dijkstra_with_path(graph, start, end):
    """
    Finds shortest path and distance from start to end vertex.
    
    Args:
        graph: Dictionary where graph[u] = [(v, weight), ...]
        start: Starting vertex
        end: Ending vertex
    
    Returns:
        Tuple of (shortest_distance, path)
    """
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    previous = {vertex: None for vertex in graph}
    
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_vertex == end:
            break
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        for neighbor, weight in graph.get(current_vertex, []):
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))
    
    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    return distances[end], path if path and path[0] == start else None


if __name__ == "__main__":
    # Test Dijkstra's algorithm
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2)],
        'E': [('C', 10), ('D', 2)]
    }
    
    print("Graph (weighted):")
    for vertex, edges in graph.items():
        print(f"  {vertex}: {edges}")
    
    start_vertex = 'A'
    print(f"\nShortest distances from '{start_vertex}':")
    distances = dijkstra(graph, start_vertex)
    for vertex, distance in sorted(distances.items()):
        print(f"  {vertex}: {distance}")
    
    end_vertex = 'E'
    distance, path = dijkstra_with_path(graph, start_vertex, end_vertex)
    print(f"\nShortest path from '{start_vertex}' to '{end_vertex}':")
    print(f"  Distance: {distance}")
    print(f"  Path: {' -> '.join(path)}")
