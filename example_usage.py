from social_graph import SocialGraph
from influence_ranker import rank_users_by_influence, rank_users_by_influence_threshold

def demonstrate_graph_operations():
    """Demonstrate core functionality of the SocialGraph class."""
    print("=== Social Network Analysis Proof of Concept ===")
    sg = SocialGraph()
    
    # Build the social graph (note: using follower -> followee order)
    relationships = [
        ('Bob', 'Alice'),    # Bob follows Alice
        ('Charlie', 'Alice'), # Charlie follows Alice
        ('Dave', 'Bob'),     # Dave follows Bob
        ('Eve', 'Charlie'),  # Eve follows Charlie
        ('Alice', 'Eve'),    # Alice follows Eve (creates cycle)
        ('Frank', 'Dave'),   # Frank follows Dave
        ('Alice', 'Frank')   # Alice follows Frank
    ]
    
    for follower, followee in relationships:
        sg.add_follow(follower, followee)
    
    # Demonstrate basic operations
    print("\n--- Graph Statistics ---")
    print(f"Total users: {len(sg.get_all_users())}")
    print(f"Alice's followers: {sg.get_followers('Alice')}")
    print(f"Alice follows: {sg.get_followees('Alice')}")
    print(f"Mutual follows: {sg.find_mutual_follows()}")
    
    # Compute and display influence
    print("\n--- Influence Analysis ---")
    scores = sg.compute_influence_scores()
    print("All Influence Scores:")
    for user, score in sorted(scores.items(), key=lambda x: -x[1]):
        print(f"{user}: {score}")
    
    # Show rankings
    print("\nTop 3 Influential Users:")
    top_users = rank_users_by_influence(scores, 3)
    for i, (user, score) in enumerate(top_users, 1):
        print(f"{i}. {user} (Score: {score})")
    
    # Threshold-based ranking
    print("\nUsers with Influence >= 2:")
    threshold_users = rank_users_by_influence_threshold(scores, 2)
    for user, score in threshold_users:
        print(f"- {user} ({score})")
    
    # Demonstrate dynamic updates
    print("\n--- Graph Modification ---")
    print("Adding mutual follow between Alice and Bob...")
    sg.add_follow('Alice', 'Bob')  # Now they follow each other
    print("New mutual follows:", sg.find_mutual_follows())
    print("Updated scores:", sg.compute_influence_scores())

if __name__ == "__main__":
    demonstrate_graph_operations()