import unittest
from social_graph import SocialGraph

class TestSocialGraph(unittest.TestCase):
    def setUp(self):
        self.sg = SocialGraph()
        # Note: Changed to followee-first notation to match implementation
        self.sg.add_follow('B', 'A')  # B follows A
        self.sg.add_follow('C', 'A')  # C follows A
        self.sg.add_follow('C', 'B')  # C follows B
        self.sg.add_follow('A', 'C')  # A follows C (creates cycle)

    def test_add_operations(self):
        self.assertEqual(len(self.sg.get_all_users()), 3)
        self.assertEqual(self.sg.get_followees('A'), {'C'})  # A follows C
        self.assertEqual(self.sg.get_followers('A'), {'B', 'C'})  # B and C follow A

    def test_influence_calculation(self):
        scores = self.sg.compute_influence_scores()
        # A's influence: B and C follow A (2)
        # B is followed by C (1), but C is already counted in direct followers
        # So total for A: 2 (direct) + 0 (no new in second degree) = 2
        self.assertEqual(scores['A'], 2)
        # B's influence: C follows B (1)
        # C is followed by A (1), but A isn't following B
        # So total for B: 1 (direct) + 1 (A via C) = 2
        self.assertEqual(scores['B'], 2)
        # C's influence: A follows C (1)
        # A is followed by B and C (2), but C is already following
        # So total for C: 1 (direct) + 1 (B via A) = 2
        self.assertEqual(scores['C'], 2)

    def test_remove_operations(self):
        self.sg.remove_follow('B', 'A')
        self.assertEqual(self.sg.get_followers('A'), {'C'})
        
        self.sg.remove_user('C')
        self.assertEqual(self.sg.get_followers('A'), set())
        self.assertEqual(len(self.sg.get_all_users()), 2)

    def test_mutual_follows(self):
        # Should detect A <-> C mutual follow
        followers = {user: self.sg.get_followers(user) for user in self.sg.get_all_users()}
        mutuals = set()
        for user in followers:
            for follower in followers[user]:
                if user in followers.get(follower, set()):
                    pair = frozenset({user, follower})
                    mutuals.add(pair)
        self.assertEqual(len(mutuals), 1)
        self.assertIn(frozenset({'A', 'C'}), mutuals)

    def test_cache_invalidation(self):
        scores1 = self.sg.compute_influence_scores()
        # Add a relationship that should change B's influence
        self.sg.add_follow('D', 'B')  # New user D follows B
        scores2 = self.sg.compute_influence_scores()
        # B's influence should increase by 1 (D is new direct follower)
        self.assertEqual(scores2['B'], scores1['B'] + 1)

if __name__ == '__main__':
    unittest.main()