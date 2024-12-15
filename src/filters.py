def filter_lines(lines: list, theme: str = None, dominant_whitelist: list = None) -> list:
    """
    Filter lines by the given criteria.
    
    Arguments:
        lines: A list of line dictionaries.
        theme: A theme string to filter lines by. If None, no theme-based filtering is applied.
        dominant_whitelist: A list of allowed dominant names. If None, no dominant filtering is applied.
        
    Returns:
        A list of filtered lines.
    """
    filtered = []
    for l in lines:
        # Filter by theme if specified
        if theme is not None:
            if l.get("theme") != theme:
                continue
        
        # Filter by dominant name if whitelist is provided
        if dominant_whitelist is not None:
            dominant = l.get("dominant")
            # If there's a dominant required and it's not in the whitelist, skip
            if dominant is not None and dominant not in dominant_whitelist:
                continue
        
        filtered.append(l)
    
    return filtered
