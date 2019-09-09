def is_triangle(a, b, c):
    triangle = [a, b, c]
    longest = max(triangle)
    triangle.remove(longest)
    
    if sum(triangle) > longest:
        return True
    else:
        return False