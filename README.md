# Sliding-Block-Puzzle-Solver
Solves the 8-Puzzle Problem in the AI textbook (Russell, Norvig) (Pg. 71) using different search algorithms

Implemented the following algorithms:
- Un-informed search
    - Depth First Search
    - Depth Limited Search
    - Iterative Deepening (internally calls Depth Limited Search)
- Informed Search
    - A-star with two heuristics
        - Manhattan Distance
        - Number of wrong tiles

# Running the code
To run with a specific initial state run: `python main.py 123456780`

Here the number 123456780 indicates the starting board position from left to right and top row to bottom row.

For example, this state corresponds to the board:

```
      -------------
      | 1 | 2 | 3 |
      ----+---+----
      | 4 | 5 | 6 |
      ----+---+----
      | 7 | 8 | 0 |
      -------------
```

The default *goal state* is 123804765 :
```
      -------------
      | 1 | 2 | 3 |
      ----+---+----
      | 8 | 0 | 4 |
      ----+---+----
      | 7 | 6 | 5 |
      -------------
```
