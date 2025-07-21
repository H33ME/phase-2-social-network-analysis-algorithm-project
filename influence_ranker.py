import heapq
from typing import List, Tuple

def rank_users_by_influence(scores: dict, top_n: int = 5) -> List[Tuple]:
    """
    Returns the top N users with highest influence scores using a max-heap.
    
    Args:
        scores: Dictionary of {user: influence_score}
        top_n: Number of top users to return
        
    Returns:
        List of (user, score) tuples sorted descending by score
    """
    if not scores:
        return []
    
    # Using heapq's nlargest for O(n log k) performance
    return heapq.nlargest(top_n, scores.items(), key=lambda x: x[1])

def rank_users_by_influence_threshold(scores: dict, min_score: int) -> List[Tuple]:
    """
    Returns all users with influence scores >= min_score.
    
    Args:
        scores: Dictionary of {user: influence_score}
        min_score: Minimum influence score threshold
        
    Returns:
        List of (user, score) tuples sorted descending by score
    """
    filtered = [(user, score) for user, score in scores.items() if score >= min_score]
    return sorted(filtered, key=lambda x: -x[1])