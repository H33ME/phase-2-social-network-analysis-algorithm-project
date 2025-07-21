class SocialGraph:
    def __init__(self):
        """Initialize an empty social graph using adjacency lists."""
        self.graph = {}  # {user: set(followees)}
        self.influence_cache = {}  # Cache for influence scores

    def add_user(self, user):
        """Add a user to the graph if they don't exist."""
        if user not in self.graph:
            self.graph[user] = set()
            self.invalidate_cache()

    def remove_user(self, user):
        """Remove a user and all their connections from the graph."""
        if user in self.graph:
            # Remove all follow relationships from this user
            del self.graph[user]
            # Remove all references to this user in other users' follow sets
            for followees in self.graph.values():
                followees.discard(user)
            self.invalidate_cache()

    def add_follow(self, follower, followee):
        """Add a follow relationship between users (follower -> followee)."""
        if follower == followee:
            raise ValueError("Users cannot follow themselves")
        self.add_user(follower)
        self.add_user(followee)
        self.graph[follower].add(followee)
        self.invalidate_cache()

    def remove_follow(self, follower, followee):
        """Remove a follow relationship between users."""
        if follower in self.graph and followee in self.graph[follower]:
            self.graph[follower].remove(followee)
            self.invalidate_cache()

    def get_followers(self, user):
        """Return all users who follow the given user."""
        return {u for u in self.graph if user in self.graph[u]}

    def get_followees(self, user):
        """Return all users that the given user follows."""
        return self.graph.get(user, set()).copy()

    def get_all_users(self):
        """Return all users in the graph."""
        return list(self.graph.keys())

    

    def compute_influence_scores(self, use_cache=True):
        """
        Compute influence scores for all users.
        Influence = direct followers + followers of followers (2-hop).
        """
        if use_cache and self.influence_cache:
            return self.influence_cache.copy()

        scores = {}
        for user in self.graph:
            # Get direct followers
            direct_followers = self.get_followers(user)
            # Get second-degree followers
            second_degree = set()
            for follower in direct_followers:
                # Get followers of this follower, excluding:
                # - The original user (no self-influence)
                # - Already counted direct followers
                second_degree.update(
                    f for f in self.get_followers(follower) 
                    if f != user and f not in direct_followers
                )
            scores[user] = len(direct_followers) + len(second_degree)

        self.influence_cache = scores.copy()
        return scores

    def invalidate_cache(self):
        """Clear cached influence scores when graph changes."""
        self.influence_cache = {}

    def find_mutual_follows(self):
        """Find all pairs of users who follow each other."""
        mutuals = set()
        users = self.get_all_users()
        for i, user1 in enumerate(users):
            for user2 in users[i+1:]:
                if user2 in self.graph[user1] and user1 in self.graph[user2]:
                    mutuals.add(frozenset({user1, user2}))
        return mutuals