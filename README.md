🔍 Uninformed (Blind) Search
No domain knowledge used.

BFS (Breadth-First Search): Explores level by level. ✅ Complete & optimal (if costs are equal).

DFS (Depth-First Search): Goes deep first. ❌ Not optimal.

DLS (Depth-Limited Search): DFS with depth limit.

IDS (Iterative Deepening Search): DFS + BFS benefits. ✅ Complete & optimal.

UCS (Uniform Cost Search): Expands node with lowest cost. ✅ Optimal.

🧠 Informed (Heuristic) Search
Uses domain knowledge.

Greedy Best-First Search: Picks node with lowest estimated cost to goal (h(n)). ❌ Not always optimal.

A*: Uses actual + estimated cost (f(n) = g(n) + h(n)). ✅ Complete & optimal (if heuristic is good).

IDA*: Memory-efficient version of A*.
