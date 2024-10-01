def linear_search(haystack: list[int], needle: int) -> bool: 
    for item in haystack:
        if item == needle:
            return True
            
    return False