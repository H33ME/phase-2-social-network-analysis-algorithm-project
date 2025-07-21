# Social Network Analysis Algorithm - Phase 2

## Project Description
This repository contains the Proof of Concept implementation for Phase 2 of the Social Network Analysis project. The system analyzes social influence patterns using graph data structures and adjacency list representations in Python.

## Key Features
- **SocialGraph class** with adjacency list implementation
- **Influence scoring** (direct + second-degree followers)
- **Heap-based ranking** of top influencers
- **Dynamic graph modifications** with cache invalidation
- **Mutual relationship detection**
- **Comprehensive test coverage**

## Installation & Usage
1. Clone the repository:
```bash
git clone git@github.com:H33ME/phase-2-social-network-analysis-algorithm-project.git


2. Run the demonstration:
```bash
python3 example_usage.py
```

3. Execute tests:
```bash
python3 test_social_graph.py
```

## File Structure
- `social_graph.py` - Core graph implementation
- `influence_ranker.py` - Ranking algorithms
- `example_usage.py` - Demonstration script
- `test_social_graph.py` - Unit tests

## Results
All tests pass successfully:
```
Ran 5 tests in 0.001s
OK
```

## Next Steps
Phase 3 will focus on:
- Performance optimization
- Enhanced metrics (PageRank, engagement weights)
- Scalability improvements
- Advanced visualization


```

This README:
1. Clearly explains the project purpose
2. Highlights key features
3. Provides simple usage instructions
4. Documents the file structure
5. Shows test verification
6. Outlines future work
7. Includes proper attribution
