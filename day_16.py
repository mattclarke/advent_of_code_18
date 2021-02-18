import re


samples = """
Before: [1, 1, 1, 0]
4 1 0 0
After:  [1, 1, 1, 0]

Before: [1, 1, 0, 1]
5 1 3 3
After:  [1, 1, 0, 1]

Before: [3, 2, 3, 1]
14 2 1 3
After:  [3, 2, 3, 2]

Before: [0, 1, 2, 1]
5 1 3 0
After:  [1, 1, 2, 1]

Before: [2, 1, 2, 3]
1 3 3 2
After:  [2, 1, 3, 3]

Before: [1, 0, 2, 0]
11 0 2 1
After:  [1, 2, 2, 0]

Before: [1, 2, 1, 1]
8 2 3 0
After:  [1, 2, 1, 1]

Before: [1, 0, 3, 2]
10 0 3 3
After:  [1, 0, 3, 3]

Before: [0, 1, 3, 1]
3 0 0 0
After:  [0, 1, 3, 1]

Before: [2, 1, 3, 2]
15 0 1 2
After:  [2, 1, 3, 2]

Before: [2, 1, 2, 1]
1 2 0 2
After:  [2, 1, 2, 1]

Before: [0, 0, 2, 0]
3 0 0 2
After:  [0, 0, 0, 0]

Before: [1, 1, 3, 2]
10 0 3 3
After:  [1, 1, 3, 3]

Before: [2, 3, 2, 3]
14 3 2 3
After:  [2, 3, 2, 2]

Before: [0, 1, 3, 2]
10 1 3 0
After:  [3, 1, 3, 2]

Before: [1, 1, 1, 0]
4 1 0 2
After:  [1, 1, 1, 0]

Before: [1, 2, 3, 2]
12 2 2 3
After:  [1, 2, 3, 2]

Before: [3, 2, 1, 1]
8 2 3 3
After:  [3, 2, 1, 1]

Before: [0, 1, 3, 2]
10 1 3 2
After:  [0, 1, 3, 2]

Before: [0, 3, 3, 0]
12 2 2 3
After:  [0, 3, 3, 2]

Before: [2, 2, 2, 0]
1 2 0 0
After:  [2, 2, 2, 0]

Before: [0, 2, 0, 3]
11 3 3 2
After:  [0, 2, 9, 3]

Before: [0, 1, 3, 2]
6 3 1 1
After:  [0, 3, 3, 2]

Before: [1, 0, 2, 0]
2 2 3 0
After:  [3, 0, 2, 0]

Before: [3, 3, 1, 1]
8 2 3 1
After:  [3, 1, 1, 1]

Before: [0, 1, 0, 2]
3 0 0 0
After:  [0, 1, 0, 2]

Before: [1, 1, 3, 2]
10 0 3 0
After:  [3, 1, 3, 2]

Before: [0, 0, 1, 1]
3 0 0 2
After:  [0, 0, 0, 1]

Before: [0, 1, 1, 2]
3 0 0 2
After:  [0, 1, 0, 2]

Before: [0, 1, 1, 1]
3 0 0 3
After:  [0, 1, 1, 0]

Before: [1, 1, 1, 1]
5 1 3 1
After:  [1, 1, 1, 1]

Before: [1, 1, 3, 3]
4 1 0 3
After:  [1, 1, 3, 1]

Before: [3, 3, 1, 1]
13 2 3 3
After:  [3, 3, 1, 3]

Before: [3, 1, 1, 3]
9 2 3 0
After:  [3, 1, 1, 3]

Before: [1, 1, 2, 0]
11 1 2 1
After:  [1, 2, 2, 0]

Before: [2, 3, 2, 2]
1 2 0 2
After:  [2, 3, 2, 2]

Before: [0, 3, 2, 3]
1 2 0 1
After:  [0, 2, 2, 3]

Before: [1, 1, 2, 0]
15 1 2 1
After:  [1, 3, 2, 0]

Before: [0, 3, 1, 3]
9 2 3 1
After:  [0, 3, 1, 3]

Before: [3, 1, 2, 0]
1 2 2 3
After:  [3, 1, 2, 2]

Before: [0, 2, 1, 3]
9 2 3 0
After:  [3, 2, 1, 3]

Before: [0, 1, 0, 1]
13 1 3 3
After:  [0, 1, 0, 3]

Before: [1, 1, 1, 2]
4 1 0 0
After:  [1, 1, 1, 2]

Before: [2, 2, 3, 1]
6 3 2 0
After:  [3, 2, 3, 1]

Before: [3, 3, 1, 2]
10 2 3 1
After:  [3, 3, 1, 2]

Before: [3, 2, 3, 3]
11 3 3 1
After:  [3, 9, 3, 3]

Before: [0, 0, 2, 3]
11 3 3 3
After:  [0, 0, 2, 9]

Before: [0, 1, 0, 0]
0 3 1 3
After:  [0, 1, 0, 1]

Before: [3, 3, 0, 3]
11 0 3 0
After:  [9, 3, 0, 3]

Before: [2, 1, 3, 1]
5 1 3 1
After:  [2, 1, 3, 1]

Before: [1, 1, 2, 3]
4 1 0 1
After:  [1, 1, 2, 3]

Before: [2, 3, 3, 3]
11 0 3 0
After:  [6, 3, 3, 3]

Before: [1, 2, 2, 1]
13 0 3 2
After:  [1, 2, 3, 1]

Before: [0, 1, 3, 2]
3 0 0 3
After:  [0, 1, 3, 0]

Before: [3, 2, 3, 2]
14 2 3 3
After:  [3, 2, 3, 2]

Before: [1, 1, 2, 2]
6 3 1 2
After:  [1, 1, 3, 2]

Before: [0, 2, 3, 2]
3 0 0 1
After:  [0, 0, 3, 2]

Before: [3, 2, 2, 3]
14 3 2 2
After:  [3, 2, 2, 3]

Before: [2, 1, 1, 2]
15 0 1 1
After:  [2, 3, 1, 2]

Before: [1, 1, 1, 3]
4 1 0 3
After:  [1, 1, 1, 1]

Before: [1, 3, 2, 3]
1 2 2 0
After:  [2, 3, 2, 3]

Before: [1, 1, 2, 1]
4 1 0 0
After:  [1, 1, 2, 1]

Before: [1, 1, 3, 1]
13 0 3 1
After:  [1, 3, 3, 1]

Before: [1, 0, 2, 1]
8 3 3 1
After:  [1, 1, 2, 1]

Before: [3, 3, 2, 1]
6 3 2 1
After:  [3, 3, 2, 1]

Before: [3, 3, 2, 3]
14 0 2 2
After:  [3, 3, 2, 3]

Before: [1, 1, 1, 1]
5 1 3 0
After:  [1, 1, 1, 1]

Before: [0, 1, 2, 0]
2 2 3 0
After:  [3, 1, 2, 0]

Before: [0, 2, 1, 3]
7 0 3 2
After:  [0, 2, 0, 3]

Before: [2, 1, 0, 0]
13 1 3 1
After:  [2, 3, 0, 0]

Before: [0, 2, 2, 1]
15 0 2 1
After:  [0, 2, 2, 1]

Before: [2, 2, 3, 0]
14 2 0 3
After:  [2, 2, 3, 2]

Before: [0, 1, 3, 1]
5 1 3 0
After:  [1, 1, 3, 1]

Before: [1, 1, 3, 1]
5 1 3 0
After:  [1, 1, 3, 1]

Before: [0, 1, 3, 1]
12 2 2 1
After:  [0, 2, 3, 1]

Before: [1, 3, 2, 1]
11 1 2 2
After:  [1, 3, 6, 1]

Before: [3, 2, 3, 0]
2 1 3 3
After:  [3, 2, 3, 3]

Before: [0, 1, 3, 1]
5 1 3 1
After:  [0, 1, 3, 1]

Before: [1, 2, 2, 2]
11 0 2 1
After:  [1, 2, 2, 2]

Before: [3, 0, 2, 1]
6 3 2 1
After:  [3, 3, 2, 1]

Before: [1, 1, 2, 0]
4 1 0 0
After:  [1, 1, 2, 0]

Before: [0, 2, 1, 0]
3 0 0 1
After:  [0, 0, 1, 0]

Before: [0, 2, 0, 0]
2 1 3 3
After:  [0, 2, 0, 3]

Before: [1, 1, 1, 0]
4 1 0 3
After:  [1, 1, 1, 1]

Before: [1, 0, 2, 2]
15 0 2 2
After:  [1, 0, 3, 2]

Before: [0, 0, 2, 1]
3 0 0 1
After:  [0, 0, 2, 1]

Before: [2, 1, 0, 3]
0 2 1 2
After:  [2, 1, 1, 3]

Before: [1, 0, 2, 0]
13 0 3 1
After:  [1, 3, 2, 0]

Before: [0, 0, 3, 3]
12 2 2 1
After:  [0, 2, 3, 3]

Before: [2, 1, 3, 1]
5 1 3 0
After:  [1, 1, 3, 1]

Before: [0, 1, 0, 3]
7 0 2 2
After:  [0, 1, 0, 3]

Before: [3, 0, 2, 0]
1 2 2 2
After:  [3, 0, 2, 0]

Before: [2, 1, 1, 1]
5 1 3 3
After:  [2, 1, 1, 1]

Before: [3, 1, 0, 2]
10 1 3 0
After:  [3, 1, 0, 2]

Before: [3, 1, 2, 0]
0 3 1 2
After:  [3, 1, 1, 0]

Before: [3, 1, 2, 1]
5 1 3 1
After:  [3, 1, 2, 1]

Before: [2, 2, 3, 1]
6 3 2 2
After:  [2, 2, 3, 1]

Before: [0, 1, 2, 1]
5 1 3 1
After:  [0, 1, 2, 1]

Before: [2, 2, 2, 3]
11 3 3 1
After:  [2, 9, 2, 3]

Before: [2, 1, 1, 2]
2 0 3 0
After:  [3, 1, 1, 2]

Before: [1, 1, 0, 2]
10 1 3 0
After:  [3, 1, 0, 2]

Before: [1, 1, 3, 1]
4 1 0 3
After:  [1, 1, 3, 1]

Before: [0, 2, 2, 1]
3 0 0 2
After:  [0, 2, 0, 1]

Before: [1, 1, 0, 2]
6 3 1 0
After:  [3, 1, 0, 2]

Before: [0, 0, 0, 3]
7 0 3 1
After:  [0, 0, 0, 3]

Before: [2, 1, 2, 2]
6 3 1 1
After:  [2, 3, 2, 2]

Before: [0, 1, 2, 1]
5 1 3 2
After:  [0, 1, 1, 1]

Before: [2, 0, 3, 3]
11 0 3 2
After:  [2, 0, 6, 3]

Before: [0, 3, 0, 0]
3 0 0 2
After:  [0, 3, 0, 0]

Before: [3, 3, 1, 2]
10 2 3 2
After:  [3, 3, 3, 2]

Before: [1, 1, 3, 0]
13 1 3 3
After:  [1, 1, 3, 3]

Before: [2, 1, 0, 1]
0 2 1 1
After:  [2, 1, 0, 1]

Before: [2, 2, 2, 1]
6 3 2 1
After:  [2, 3, 2, 1]

Before: [2, 1, 2, 0]
2 0 3 1
After:  [2, 3, 2, 0]

Before: [1, 2, 3, 3]
11 2 3 1
After:  [1, 9, 3, 3]

Before: [0, 1, 1, 0]
7 0 3 2
After:  [0, 1, 0, 0]

Before: [0, 2, 1, 1]
3 0 0 1
After:  [0, 0, 1, 1]

Before: [1, 1, 2, 3]
9 1 3 3
After:  [1, 1, 2, 3]

Before: [3, 0, 1, 3]
1 3 0 3
After:  [3, 0, 1, 3]

Before: [0, 3, 1, 2]
10 2 3 0
After:  [3, 3, 1, 2]

Before: [2, 2, 1, 3]
1 3 3 2
After:  [2, 2, 3, 3]

Before: [2, 2, 2, 1]
6 3 2 3
After:  [2, 2, 2, 3]

Before: [0, 2, 2, 2]
1 2 0 0
After:  [2, 2, 2, 2]

Before: [0, 1, 3, 2]
12 2 2 0
After:  [2, 1, 3, 2]

Before: [0, 2, 1, 0]
3 0 0 3
After:  [0, 2, 1, 0]

Before: [1, 1, 3, 1]
4 1 0 2
After:  [1, 1, 1, 1]

Before: [2, 2, 2, 1]
8 3 3 0
After:  [1, 2, 2, 1]

Before: [1, 1, 3, 1]
12 2 2 3
After:  [1, 1, 3, 2]

Before: [3, 3, 3, 1]
6 3 2 3
After:  [3, 3, 3, 3]

Before: [2, 0, 3, 2]
14 2 3 0
After:  [2, 0, 3, 2]

Before: [2, 1, 3, 2]
12 2 2 2
After:  [2, 1, 2, 2]

Before: [1, 0, 1, 1]
8 2 3 2
After:  [1, 0, 1, 1]

Before: [0, 2, 0, 2]
7 0 3 3
After:  [0, 2, 0, 0]

Before: [1, 1, 2, 3]
9 1 3 0
After:  [3, 1, 2, 3]

Before: [1, 2, 2, 1]
15 1 2 0
After:  [4, 2, 2, 1]

Before: [1, 1, 3, 3]
9 0 3 3
After:  [1, 1, 3, 3]

Before: [2, 3, 0, 3]
15 2 3 0
After:  [3, 3, 0, 3]

Before: [1, 1, 3, 3]
1 3 3 0
After:  [3, 1, 3, 3]

Before: [0, 2, 3, 2]
7 0 1 0
After:  [0, 2, 3, 2]

Before: [3, 1, 1, 0]
0 3 1 0
After:  [1, 1, 1, 0]

Before: [0, 3, 2, 0]
1 2 2 3
After:  [0, 3, 2, 2]

Before: [0, 0, 1, 1]
8 2 3 1
After:  [0, 1, 1, 1]

Before: [0, 1, 3, 0]
12 2 2 3
After:  [0, 1, 3, 2]

Before: [3, 0, 1, 2]
10 2 3 3
After:  [3, 0, 1, 3]

Before: [1, 1, 0, 0]
4 1 0 0
After:  [1, 1, 0, 0]

Before: [0, 3, 2, 3]
7 0 3 0
After:  [0, 3, 2, 3]

Before: [0, 2, 3, 0]
3 0 0 0
After:  [0, 2, 3, 0]

Before: [0, 2, 0, 3]
1 3 0 0
After:  [3, 2, 0, 3]

Before: [3, 3, 1, 2]
10 2 3 3
After:  [3, 3, 1, 3]

Before: [1, 1, 2, 2]
6 3 1 3
After:  [1, 1, 2, 3]

Before: [0, 1, 1, 2]
6 3 1 3
After:  [0, 1, 1, 3]

Before: [0, 0, 2, 3]
15 0 2 0
After:  [2, 0, 2, 3]

Before: [1, 1, 3, 2]
14 2 3 1
After:  [1, 2, 3, 2]

Before: [0, 2, 0, 1]
7 0 1 1
After:  [0, 0, 0, 1]

Before: [0, 1, 2, 1]
6 3 2 2
After:  [0, 1, 3, 1]

Before: [2, 1, 0, 0]
2 0 3 3
After:  [2, 1, 0, 3]

Before: [3, 1, 3, 1]
5 1 3 0
After:  [1, 1, 3, 1]

Before: [2, 1, 3, 1]
6 3 2 2
After:  [2, 1, 3, 1]

Before: [3, 0, 3, 1]
12 2 2 0
After:  [2, 0, 3, 1]

Before: [0, 2, 2, 3]
3 0 0 0
After:  [0, 2, 2, 3]

Before: [1, 1, 3, 2]
6 3 1 3
After:  [1, 1, 3, 3]

Before: [3, 1, 1, 2]
10 1 3 1
After:  [3, 3, 1, 2]

Before: [1, 1, 2, 3]
15 2 1 0
After:  [3, 1, 2, 3]

Before: [2, 0, 3, 3]
14 2 0 2
After:  [2, 0, 2, 3]

Before: [1, 1, 1, 2]
4 1 0 1
After:  [1, 1, 1, 2]

Before: [0, 1, 2, 0]
7 0 2 2
After:  [0, 1, 0, 0]

Before: [0, 3, 0, 3]
3 0 0 0
After:  [0, 3, 0, 3]

Before: [3, 1, 0, 0]
0 2 1 0
After:  [1, 1, 0, 0]

Before: [1, 1, 2, 0]
4 1 0 1
After:  [1, 1, 2, 0]

Before: [1, 1, 2, 0]
4 1 0 2
After:  [1, 1, 1, 0]

Before: [1, 1, 0, 2]
0 2 1 3
After:  [1, 1, 0, 1]

Before: [1, 1, 1, 2]
6 3 1 3
After:  [1, 1, 1, 3]

Before: [0, 3, 0, 2]
3 0 0 0
After:  [0, 3, 0, 2]

Before: [0, 0, 3, 2]
7 0 1 2
After:  [0, 0, 0, 2]

Before: [1, 3, 3, 2]
12 2 2 3
After:  [1, 3, 3, 2]

Before: [0, 3, 3, 2]
3 0 0 2
After:  [0, 3, 0, 2]

Before: [0, 1, 0, 3]
1 3 0 3
After:  [0, 1, 0, 3]

Before: [0, 0, 2, 3]
3 0 0 2
After:  [0, 0, 0, 3]

Before: [2, 1, 0, 2]
2 0 3 2
After:  [2, 1, 3, 2]

Before: [1, 2, 1, 3]
1 3 0 2
After:  [1, 2, 3, 3]

Before: [1, 0, 0, 3]
15 2 3 1
After:  [1, 3, 0, 3]

Before: [3, 1, 0, 3]
9 1 3 2
After:  [3, 1, 3, 3]

Before: [0, 0, 0, 0]
7 0 1 2
After:  [0, 0, 0, 0]

Before: [0, 2, 3, 0]
14 2 1 1
After:  [0, 2, 3, 0]

Before: [2, 0, 2, 1]
6 3 2 2
After:  [2, 0, 3, 1]

Before: [2, 1, 1, 1]
8 2 3 0
After:  [1, 1, 1, 1]

Before: [1, 0, 3, 3]
12 2 2 1
After:  [1, 2, 3, 3]

Before: [0, 0, 3, 1]
3 0 0 1
After:  [0, 0, 3, 1]

Before: [1, 1, 3, 1]
4 1 0 0
After:  [1, 1, 3, 1]

Before: [1, 3, 2, 1]
14 1 2 3
After:  [1, 3, 2, 2]

Before: [2, 1, 2, 3]
9 1 3 1
After:  [2, 3, 2, 3]

Before: [2, 1, 0, 0]
0 2 1 0
After:  [1, 1, 0, 0]

Before: [3, 1, 0, 1]
5 1 3 2
After:  [3, 1, 1, 1]

Before: [1, 2, 3, 3]
12 2 2 0
After:  [2, 2, 3, 3]

Before: [1, 3, 2, 1]
1 2 2 3
After:  [1, 3, 2, 2]

Before: [0, 2, 2, 3]
1 3 0 2
After:  [0, 2, 3, 3]

Before: [2, 0, 3, 1]
8 3 3 3
After:  [2, 0, 3, 1]

Before: [1, 3, 1, 2]
10 2 3 2
After:  [1, 3, 3, 2]

Before: [1, 1, 2, 1]
5 1 3 1
After:  [1, 1, 2, 1]

Before: [2, 0, 1, 3]
9 2 3 0
After:  [3, 0, 1, 3]

Before: [0, 3, 1, 0]
13 2 3 3
After:  [0, 3, 1, 3]

Before: [1, 2, 0, 1]
8 3 3 1
After:  [1, 1, 0, 1]

Before: [2, 1, 2, 3]
15 0 2 1
After:  [2, 4, 2, 3]

Before: [3, 3, 2, 3]
11 0 2 2
After:  [3, 3, 6, 3]

Before: [0, 0, 0, 2]
7 0 1 0
After:  [0, 0, 0, 2]

Before: [0, 1, 3, 1]
12 2 2 2
After:  [0, 1, 2, 1]

Before: [3, 2, 2, 3]
11 3 3 1
After:  [3, 9, 2, 3]

Before: [2, 3, 1, 0]
2 0 3 3
After:  [2, 3, 1, 3]

Before: [3, 3, 1, 2]
10 2 3 0
After:  [3, 3, 1, 2]

Before: [1, 0, 1, 0]
13 0 3 3
After:  [1, 0, 1, 3]

Before: [1, 1, 3, 3]
9 0 3 2
After:  [1, 1, 3, 3]

Before: [2, 2, 2, 2]
2 0 3 1
After:  [2, 3, 2, 2]

Before: [0, 1, 1, 3]
9 2 3 0
After:  [3, 1, 1, 3]

Before: [0, 1, 3, 1]
6 3 2 0
After:  [3, 1, 3, 1]

Before: [1, 2, 3, 3]
11 1 3 1
After:  [1, 6, 3, 3]

Before: [1, 2, 1, 3]
1 3 3 0
After:  [3, 2, 1, 3]

Before: [0, 3, 2, 0]
2 2 3 2
After:  [0, 3, 3, 0]

Before: [2, 1, 0, 1]
5 1 3 1
After:  [2, 1, 0, 1]

Before: [2, 0, 3, 0]
14 2 0 3
After:  [2, 0, 3, 2]

Before: [1, 1, 1, 3]
9 0 3 2
After:  [1, 1, 3, 3]

Before: [2, 1, 2, 1]
15 1 2 0
After:  [3, 1, 2, 1]

Before: [2, 1, 3, 1]
6 3 2 0
After:  [3, 1, 3, 1]

Before: [1, 1, 3, 2]
4 1 0 2
After:  [1, 1, 1, 2]

Before: [1, 1, 1, 0]
13 2 3 0
After:  [3, 1, 1, 0]

Before: [0, 2, 3, 0]
2 1 3 3
After:  [0, 2, 3, 3]

Before: [2, 1, 0, 3]
15 0 1 1
After:  [2, 3, 0, 3]

Before: [1, 1, 2, 0]
13 0 3 2
After:  [1, 1, 3, 0]

Before: [2, 2, 2, 2]
2 2 3 0
After:  [3, 2, 2, 2]

Before: [0, 0, 1, 0]
7 0 2 1
After:  [0, 0, 1, 0]

Before: [0, 0, 2, 3]
3 0 0 3
After:  [0, 0, 2, 0]

Before: [3, 1, 1, 3]
9 1 3 3
After:  [3, 1, 1, 3]

Before: [2, 1, 0, 3]
0 2 1 1
After:  [2, 1, 0, 3]

Before: [2, 0, 2, 2]
2 2 3 0
After:  [3, 0, 2, 2]

Before: [1, 2, 2, 3]
14 3 2 3
After:  [1, 2, 2, 2]

Before: [0, 0, 2, 3]
3 0 0 0
After:  [0, 0, 2, 3]

Before: [1, 0, 1, 0]
13 2 3 2
After:  [1, 0, 3, 0]

Before: [3, 3, 1, 1]
13 2 3 0
After:  [3, 3, 1, 1]

Before: [1, 1, 1, 3]
11 3 3 3
After:  [1, 1, 1, 9]

Before: [0, 3, 3, 3]
12 2 2 3
After:  [0, 3, 3, 2]

Before: [0, 2, 1, 3]
3 0 0 1
After:  [0, 0, 1, 3]

Before: [1, 0, 2, 3]
9 0 3 1
After:  [1, 3, 2, 3]

Before: [2, 3, 2, 1]
6 3 2 0
After:  [3, 3, 2, 1]

Before: [1, 3, 1, 3]
9 2 3 0
After:  [3, 3, 1, 3]

Before: [0, 1, 0, 0]
3 0 0 1
After:  [0, 0, 0, 0]

Before: [1, 0, 0, 0]
13 0 3 3
After:  [1, 0, 0, 3]

Before: [1, 3, 3, 2]
10 0 3 3
After:  [1, 3, 3, 3]

Before: [2, 0, 1, 2]
10 2 3 0
After:  [3, 0, 1, 2]

Before: [1, 1, 0, 1]
5 1 3 1
After:  [1, 1, 0, 1]

Before: [2, 2, 0, 0]
2 1 3 3
After:  [2, 2, 0, 3]

Before: [2, 2, 3, 2]
14 2 3 3
After:  [2, 2, 3, 2]

Before: [3, 3, 2, 3]
14 3 2 3
After:  [3, 3, 2, 2]

Before: [0, 1, 2, 2]
10 1 3 3
After:  [0, 1, 2, 3]

Before: [1, 0, 3, 2]
12 2 2 2
After:  [1, 0, 2, 2]

Before: [0, 2, 0, 2]
7 0 2 2
After:  [0, 2, 0, 2]

Before: [0, 0, 2, 0]
7 0 3 2
After:  [0, 0, 0, 0]

Before: [1, 1, 0, 0]
0 2 1 1
After:  [1, 1, 0, 0]

Before: [3, 1, 0, 1]
0 2 1 0
After:  [1, 1, 0, 1]

Before: [1, 1, 3, 1]
5 1 3 3
After:  [1, 1, 3, 1]

Before: [1, 1, 3, 3]
4 1 0 1
After:  [1, 1, 3, 3]

Before: [1, 1, 3, 0]
0 3 1 0
After:  [1, 1, 3, 0]

Before: [2, 1, 0, 3]
15 2 3 2
After:  [2, 1, 3, 3]

Before: [1, 0, 2, 2]
15 1 2 0
After:  [2, 0, 2, 2]

Before: [0, 3, 0, 1]
8 3 3 2
After:  [0, 3, 1, 1]

Before: [3, 1, 0, 1]
5 1 3 1
After:  [3, 1, 0, 1]

Before: [0, 2, 3, 2]
12 2 2 2
After:  [0, 2, 2, 2]

Before: [2, 1, 0, 3]
11 0 3 1
After:  [2, 6, 0, 3]

Before: [3, 1, 2, 0]
2 2 3 1
After:  [3, 3, 2, 0]

Before: [1, 2, 2, 1]
13 0 3 0
After:  [3, 2, 2, 1]

Before: [2, 3, 3, 2]
14 2 0 0
After:  [2, 3, 3, 2]

Before: [2, 1, 0, 0]
0 2 1 2
After:  [2, 1, 1, 0]

Before: [0, 0, 0, 1]
3 0 0 1
After:  [0, 0, 0, 1]

Before: [2, 2, 2, 3]
11 0 3 1
After:  [2, 6, 2, 3]

Before: [2, 2, 3, 0]
12 2 2 3
After:  [2, 2, 3, 2]

Before: [2, 3, 3, 1]
8 3 3 0
After:  [1, 3, 3, 1]

Before: [2, 1, 2, 2]
2 2 3 3
After:  [2, 1, 2, 3]

Before: [0, 0, 1, 1]
8 3 3 1
After:  [0, 1, 1, 1]

Before: [1, 1, 3, 1]
6 3 2 3
After:  [1, 1, 3, 3]

Before: [1, 1, 2, 2]
6 3 1 1
After:  [1, 3, 2, 2]

Before: [0, 0, 3, 2]
14 2 3 3
After:  [0, 0, 3, 2]

Before: [3, 1, 2, 2]
6 3 1 0
After:  [3, 1, 2, 2]

Before: [1, 0, 1, 2]
10 0 3 0
After:  [3, 0, 1, 2]

Before: [0, 2, 2, 0]
3 0 0 3
After:  [0, 2, 2, 0]

Before: [2, 1, 0, 0]
0 3 1 2
After:  [2, 1, 1, 0]

Before: [2, 1, 3, 2]
12 2 2 1
After:  [2, 2, 3, 2]

Before: [1, 1, 0, 2]
4 1 0 3
After:  [1, 1, 0, 1]

Before: [3, 1, 1, 1]
5 1 3 2
After:  [3, 1, 1, 1]

Before: [3, 0, 2, 0]
15 2 2 1
After:  [3, 4, 2, 0]

Before: [0, 2, 3, 1]
14 2 1 2
After:  [0, 2, 2, 1]

Before: [3, 2, 2, 3]
14 0 2 2
After:  [3, 2, 2, 3]

Before: [1, 1, 2, 1]
4 1 0 2
After:  [1, 1, 1, 1]

Before: [1, 3, 3, 1]
6 3 2 1
After:  [1, 3, 3, 1]

Before: [0, 0, 0, 0]
7 0 1 3
After:  [0, 0, 0, 0]

Before: [0, 3, 1, 3]
3 0 0 1
After:  [0, 0, 1, 3]

Before: [0, 1, 0, 0]
0 3 1 0
After:  [1, 1, 0, 0]

Before: [0, 0, 3, 1]
12 2 2 1
After:  [0, 2, 3, 1]

Before: [0, 0, 1, 1]
8 3 3 3
After:  [0, 0, 1, 1]

Before: [1, 3, 3, 1]
6 3 2 3
After:  [1, 3, 3, 3]

Before: [1, 1, 1, 3]
4 1 0 2
After:  [1, 1, 1, 3]

Before: [0, 3, 0, 2]
3 0 0 1
After:  [0, 0, 0, 2]

Before: [0, 1, 3, 1]
12 2 2 0
After:  [2, 1, 3, 1]

Before: [2, 1, 2, 1]
5 1 3 1
After:  [2, 1, 2, 1]

Before: [3, 0, 1, 2]
10 2 3 1
After:  [3, 3, 1, 2]

Before: [0, 3, 2, 3]
15 0 3 3
After:  [0, 3, 2, 3]

Before: [1, 1, 2, 2]
4 1 0 1
After:  [1, 1, 2, 2]

Before: [2, 1, 0, 2]
10 1 3 1
After:  [2, 3, 0, 2]

Before: [1, 1, 2, 2]
4 1 0 2
After:  [1, 1, 1, 2]

Before: [3, 0, 1, 3]
15 1 3 1
After:  [3, 3, 1, 3]

Before: [1, 3, 0, 1]
8 3 3 0
After:  [1, 3, 0, 1]

Before: [2, 2, 3, 2]
14 2 0 2
After:  [2, 2, 2, 2]

Before: [0, 3, 2, 1]
11 3 2 3
After:  [0, 3, 2, 2]

Before: [3, 2, 3, 2]
2 1 3 3
After:  [3, 2, 3, 3]

Before: [1, 1, 2, 3]
1 2 2 0
After:  [2, 1, 2, 3]

Before: [3, 1, 1, 0]
13 2 3 3
After:  [3, 1, 1, 3]

Before: [0, 3, 0, 2]
3 0 0 2
After:  [0, 3, 0, 2]

Before: [3, 2, 2, 3]
11 0 3 0
After:  [9, 2, 2, 3]

Before: [0, 1, 0, 3]
7 0 1 3
After:  [0, 1, 0, 0]

Before: [0, 1, 0, 2]
3 0 0 3
After:  [0, 1, 0, 0]

Before: [3, 1, 0, 3]
1 3 1 3
After:  [3, 1, 0, 3]

Before: [2, 1, 0, 0]
15 0 1 0
After:  [3, 1, 0, 0]

Before: [2, 1, 3, 0]
0 3 1 0
After:  [1, 1, 3, 0]

Before: [1, 2, 3, 1]
13 0 3 0
After:  [3, 2, 3, 1]

Before: [1, 0, 3, 1]
8 3 3 0
After:  [1, 0, 3, 1]

Before: [1, 0, 3, 1]
8 3 3 1
After:  [1, 1, 3, 1]

Before: [1, 2, 3, 1]
12 2 2 2
After:  [1, 2, 2, 1]

Before: [3, 0, 1, 1]
8 2 3 0
After:  [1, 0, 1, 1]

Before: [0, 1, 2, 2]
3 0 0 3
After:  [0, 1, 2, 0]

Before: [0, 1, 1, 3]
3 0 0 2
After:  [0, 1, 0, 3]

Before: [2, 1, 2, 1]
5 1 3 2
After:  [2, 1, 1, 1]

Before: [1, 0, 3, 3]
9 0 3 3
After:  [1, 0, 3, 3]

Before: [1, 0, 2, 3]
15 2 2 3
After:  [1, 0, 2, 4]

Before: [1, 2, 3, 2]
15 0 2 2
After:  [1, 2, 3, 2]

Before: [3, 1, 2, 3]
15 2 2 0
After:  [4, 1, 2, 3]

Before: [1, 0, 3, 2]
10 0 3 1
After:  [1, 3, 3, 2]

Before: [3, 1, 2, 3]
14 0 2 2
After:  [3, 1, 2, 3]

Before: [3, 0, 2, 2]
15 1 2 0
After:  [2, 0, 2, 2]

Before: [2, 3, 2, 3]
11 2 3 2
After:  [2, 3, 6, 3]

Before: [2, 1, 1, 0]
13 2 3 1
After:  [2, 3, 1, 0]

Before: [2, 0, 1, 2]
10 2 3 2
After:  [2, 0, 3, 2]

Before: [1, 2, 2, 1]
8 3 3 2
After:  [1, 2, 1, 1]

Before: [3, 2, 2, 1]
14 0 2 3
After:  [3, 2, 2, 2]

Before: [3, 1, 2, 2]
11 1 2 0
After:  [2, 1, 2, 2]

Before: [0, 3, 0, 3]
7 0 1 1
After:  [0, 0, 0, 3]

Before: [2, 1, 2, 0]
2 0 3 0
After:  [3, 1, 2, 0]

Before: [1, 1, 1, 2]
10 1 3 0
After:  [3, 1, 1, 2]

Before: [2, 1, 3, 3]
9 1 3 2
After:  [2, 1, 3, 3]

Before: [3, 0, 1, 3]
11 0 3 2
After:  [3, 0, 9, 3]

Before: [0, 1, 0, 1]
5 1 3 0
After:  [1, 1, 0, 1]

Before: [1, 1, 3, 1]
5 1 3 1
After:  [1, 1, 3, 1]

Before: [1, 1, 3, 1]
8 3 3 1
After:  [1, 1, 3, 1]

Before: [1, 1, 1, 2]
10 0 3 1
After:  [1, 3, 1, 2]

Before: [3, 2, 3, 1]
14 2 1 1
After:  [3, 2, 3, 1]

Before: [1, 2, 1, 1]
8 2 3 3
After:  [1, 2, 1, 1]

Before: [3, 3, 2, 1]
8 3 3 2
After:  [3, 3, 1, 1]

Before: [1, 1, 1, 2]
4 1 0 2
After:  [1, 1, 1, 2]

Before: [2, 3, 3, 1]
14 2 0 0
After:  [2, 3, 3, 1]

Before: [2, 0, 1, 3]
9 2 3 1
After:  [2, 3, 1, 3]

Before: [1, 1, 0, 1]
5 1 3 2
After:  [1, 1, 1, 1]

Before: [0, 1, 0, 2]
10 1 3 3
After:  [0, 1, 0, 3]

Before: [3, 1, 0, 1]
8 3 3 1
After:  [3, 1, 0, 1]

Before: [1, 1, 3, 2]
4 1 0 0
After:  [1, 1, 3, 2]

Before: [0, 3, 1, 0]
3 0 0 2
After:  [0, 3, 0, 0]

Before: [3, 1, 1, 0]
0 3 1 3
After:  [3, 1, 1, 1]

Before: [1, 0, 2, 2]
10 0 3 0
After:  [3, 0, 2, 2]

Before: [0, 1, 3, 1]
3 0 0 3
After:  [0, 1, 3, 0]

Before: [2, 3, 2, 0]
1 2 0 1
After:  [2, 2, 2, 0]

Before: [1, 1, 3, 0]
0 3 1 1
After:  [1, 1, 3, 0]

Before: [2, 0, 1, 3]
15 1 3 0
After:  [3, 0, 1, 3]

Before: [2, 0, 3, 1]
8 3 3 2
After:  [2, 0, 1, 1]

Before: [0, 2, 3, 2]
7 0 2 3
After:  [0, 2, 3, 0]

Before: [1, 3, 3, 3]
9 0 3 1
After:  [1, 3, 3, 3]

Before: [3, 1, 2, 3]
1 3 3 1
After:  [3, 3, 2, 3]

Before: [0, 0, 3, 0]
3 0 0 3
After:  [0, 0, 3, 0]

Before: [2, 3, 2, 3]
11 1 2 3
After:  [2, 3, 2, 6]

Before: [2, 1, 0, 1]
8 3 3 1
After:  [2, 1, 0, 1]

Before: [2, 1, 1, 0]
0 3 1 2
After:  [2, 1, 1, 0]

Before: [0, 0, 3, 2]
12 2 2 2
After:  [0, 0, 2, 2]

Before: [3, 2, 3, 3]
11 1 3 0
After:  [6, 2, 3, 3]

Before: [3, 1, 0, 0]
0 2 1 3
After:  [3, 1, 0, 1]

Before: [1, 3, 2, 3]
9 0 3 0
After:  [3, 3, 2, 3]

Before: [0, 0, 0, 0]
3 0 0 3
After:  [0, 0, 0, 0]

Before: [0, 1, 1, 2]
3 0 0 1
After:  [0, 0, 1, 2]

Before: [1, 2, 2, 2]
10 0 3 0
After:  [3, 2, 2, 2]

Before: [2, 1, 2, 0]
0 3 1 2
After:  [2, 1, 1, 0]

Before: [2, 3, 0, 3]
11 1 3 0
After:  [9, 3, 0, 3]

Before: [1, 2, 3, 1]
13 0 3 1
After:  [1, 3, 3, 1]

Before: [0, 2, 0, 3]
1 3 3 0
After:  [3, 2, 0, 3]

Before: [1, 1, 0, 3]
1 3 1 2
After:  [1, 1, 3, 3]

Before: [3, 1, 3, 0]
13 1 3 3
After:  [3, 1, 3, 3]

Before: [3, 2, 2, 2]
2 2 3 0
After:  [3, 2, 2, 2]

Before: [0, 0, 3, 1]
12 2 2 2
After:  [0, 0, 2, 1]

Before: [0, 1, 3, 1]
5 1 3 2
After:  [0, 1, 1, 1]

Before: [0, 1, 1, 1]
7 0 1 1
After:  [0, 0, 1, 1]

Before: [3, 1, 3, 0]
0 3 1 0
After:  [1, 1, 3, 0]

Before: [0, 2, 2, 3]
11 1 3 0
After:  [6, 2, 2, 3]

Before: [0, 3, 0, 3]
11 1 3 0
After:  [9, 3, 0, 3]

Before: [0, 1, 3, 1]
7 0 1 2
After:  [0, 1, 0, 1]

Before: [2, 1, 2, 3]
15 2 2 1
After:  [2, 4, 2, 3]

Before: [2, 1, 2, 3]
9 1 3 3
After:  [2, 1, 2, 3]

Before: [0, 0, 3, 0]
12 2 2 1
After:  [0, 2, 3, 0]

Before: [1, 2, 3, 3]
14 2 1 3
After:  [1, 2, 3, 2]

Before: [0, 1, 2, 0]
0 3 1 1
After:  [0, 1, 2, 0]

Before: [2, 3, 1, 2]
10 2 3 0
After:  [3, 3, 1, 2]

Before: [3, 1, 3, 1]
5 1 3 3
After:  [3, 1, 3, 1]

Before: [0, 1, 3, 3]
1 3 1 1
After:  [0, 3, 3, 3]

Before: [0, 2, 1, 3]
7 0 2 2
After:  [0, 2, 0, 3]

Before: [1, 2, 3, 3]
11 1 3 0
After:  [6, 2, 3, 3]

Before: [2, 1, 1, 0]
0 3 1 1
After:  [2, 1, 1, 0]

Before: [2, 1, 2, 2]
2 2 3 0
After:  [3, 1, 2, 2]

Before: [1, 2, 3, 3]
9 0 3 2
After:  [1, 2, 3, 3]

Before: [1, 2, 2, 0]
2 2 3 1
After:  [1, 3, 2, 0]

Before: [3, 2, 2, 0]
15 2 2 3
After:  [3, 2, 2, 4]

Before: [3, 1, 3, 1]
6 3 2 2
After:  [3, 1, 3, 1]

Before: [0, 3, 2, 2]
15 3 2 0
After:  [4, 3, 2, 2]

Before: [1, 1, 3, 2]
12 2 2 0
After:  [2, 1, 3, 2]

Before: [3, 3, 1, 1]
8 2 3 0
After:  [1, 3, 1, 1]

Before: [0, 3, 0, 2]
3 0 0 3
After:  [0, 3, 0, 0]

Before: [0, 1, 2, 1]
15 1 2 1
After:  [0, 3, 2, 1]

Before: [3, 3, 2, 1]
8 3 3 0
After:  [1, 3, 2, 1]

Before: [0, 0, 2, 1]
8 3 3 2
After:  [0, 0, 1, 1]

Before: [1, 0, 3, 1]
13 0 3 2
After:  [1, 0, 3, 1]

Before: [3, 3, 3, 3]
12 2 2 1
After:  [3, 2, 3, 3]

Before: [0, 1, 1, 0]
0 3 1 3
After:  [0, 1, 1, 1]

Before: [2, 1, 0, 1]
5 1 3 2
After:  [2, 1, 1, 1]

Before: [1, 0, 0, 1]
8 3 3 0
After:  [1, 0, 0, 1]

Before: [0, 3, 0, 2]
7 0 2 3
After:  [0, 3, 0, 0]

Before: [0, 3, 3, 3]
3 0 0 0
After:  [0, 3, 3, 3]

Before: [3, 2, 3, 1]
6 3 2 2
After:  [3, 2, 3, 1]

Before: [1, 1, 2, 0]
0 3 1 1
After:  [1, 1, 2, 0]

Before: [1, 0, 1, 1]
8 3 3 1
After:  [1, 1, 1, 1]

Before: [3, 1, 3, 2]
10 1 3 2
After:  [3, 1, 3, 2]

Before: [2, 1, 0, 0]
0 2 1 3
After:  [2, 1, 0, 1]

Before: [0, 0, 0, 2]
7 0 3 1
After:  [0, 0, 0, 2]

Before: [1, 1, 2, 2]
15 1 2 1
After:  [1, 3, 2, 2]

Before: [1, 0, 2, 3]
14 3 2 1
After:  [1, 2, 2, 3]

Before: [1, 1, 3, 3]
4 1 0 2
After:  [1, 1, 1, 3]

Before: [0, 1, 0, 2]
0 2 1 2
After:  [0, 1, 1, 2]

Before: [1, 3, 3, 1]
8 3 3 2
After:  [1, 3, 1, 1]

Before: [2, 1, 3, 3]
9 1 3 1
After:  [2, 3, 3, 3]

Before: [0, 3, 1, 2]
3 0 0 3
After:  [0, 3, 1, 0]

Before: [0, 1, 3, 3]
3 0 0 0
After:  [0, 1, 3, 3]

Before: [2, 1, 1, 1]
5 1 3 0
After:  [1, 1, 1, 1]

Before: [3, 3, 3, 2]
14 2 3 2
After:  [3, 3, 2, 2]

Before: [3, 3, 3, 3]
12 2 2 2
After:  [3, 3, 2, 3]

Before: [0, 2, 2, 2]
1 2 2 2
After:  [0, 2, 2, 2]

Before: [0, 2, 1, 0]
2 1 3 0
After:  [3, 2, 1, 0]

Before: [0, 0, 3, 1]
6 3 2 0
After:  [3, 0, 3, 1]

Before: [1, 1, 2, 2]
1 2 2 3
After:  [1, 1, 2, 2]

Before: [3, 1, 0, 0]
0 2 1 1
After:  [3, 1, 0, 0]

Before: [1, 1, 0, 3]
9 0 3 0
After:  [3, 1, 0, 3]

Before: [3, 2, 2, 2]
2 1 3 3
After:  [3, 2, 2, 3]

Before: [2, 3, 2, 2]
2 2 3 1
After:  [2, 3, 2, 2]

Before: [1, 1, 1, 1]
4 1 0 3
After:  [1, 1, 1, 1]

Before: [1, 2, 1, 3]
9 0 3 3
After:  [1, 2, 1, 3]

Before: [1, 2, 0, 1]
13 0 3 3
After:  [1, 2, 0, 3]

Before: [0, 2, 2, 3]
3 0 0 3
After:  [0, 2, 2, 0]

Before: [0, 2, 3, 2]
14 2 1 2
After:  [0, 2, 2, 2]

Before: [1, 1, 3, 0]
4 1 0 1
After:  [1, 1, 3, 0]

Before: [1, 1, 0, 2]
4 1 0 1
After:  [1, 1, 0, 2]

Before: [1, 1, 0, 3]
9 1 3 1
After:  [1, 3, 0, 3]

Before: [0, 3, 0, 3]
3 0 0 3
After:  [0, 3, 0, 0]

Before: [1, 0, 3, 0]
13 0 3 1
After:  [1, 3, 3, 0]

Before: [2, 0, 2, 0]
15 1 2 3
After:  [2, 0, 2, 2]

Before: [1, 1, 3, 2]
6 3 1 2
After:  [1, 1, 3, 2]

Before: [1, 0, 2, 3]
9 0 3 2
After:  [1, 0, 3, 3]

Before: [0, 2, 3, 0]
14 2 1 0
After:  [2, 2, 3, 0]

Before: [0, 1, 2, 3]
15 2 1 1
After:  [0, 3, 2, 3]

Before: [0, 3, 3, 1]
12 2 2 3
After:  [0, 3, 3, 2]

Before: [0, 1, 0, 0]
7 0 2 1
After:  [0, 0, 0, 0]

Before: [0, 2, 1, 1]
7 0 2 2
After:  [0, 2, 0, 1]

Before: [1, 3, 1, 0]
13 0 3 1
After:  [1, 3, 1, 0]

Before: [1, 1, 0, 3]
9 0 3 1
After:  [1, 3, 0, 3]

Before: [2, 1, 1, 3]
1 3 1 0
After:  [3, 1, 1, 3]

Before: [0, 1, 1, 3]
7 0 1 1
After:  [0, 0, 1, 3]

Before: [0, 1, 0, 1]
5 1 3 1
After:  [0, 1, 0, 1]

Before: [0, 3, 2, 0]
3 0 0 0
After:  [0, 3, 2, 0]

Before: [3, 1, 3, 2]
10 1 3 0
After:  [3, 1, 3, 2]

Before: [3, 1, 2, 2]
6 3 1 2
After:  [3, 1, 3, 2]

Before: [1, 1, 2, 1]
5 1 3 0
After:  [1, 1, 2, 1]

Before: [0, 1, 0, 0]
3 0 0 0
After:  [0, 1, 0, 0]

Before: [2, 3, 0, 3]
11 0 3 2
After:  [2, 3, 6, 3]

Before: [0, 1, 2, 0]
7 0 2 1
After:  [0, 0, 2, 0]

Before: [3, 1, 2, 1]
5 1 3 3
After:  [3, 1, 2, 1]

Before: [1, 1, 0, 3]
0 2 1 2
After:  [1, 1, 1, 3]

Before: [3, 1, 1, 1]
8 3 3 0
After:  [1, 1, 1, 1]

Before: [2, 1, 3, 1]
8 3 3 1
After:  [2, 1, 3, 1]

Before: [1, 0, 3, 2]
10 0 3 2
After:  [1, 0, 3, 2]

Before: [1, 1, 1, 2]
4 1 0 3
After:  [1, 1, 1, 1]

Before: [3, 3, 3, 2]
12 2 2 3
After:  [3, 3, 3, 2]

Before: [2, 2, 3, 1]
6 3 2 1
After:  [2, 3, 3, 1]

Before: [2, 3, 2, 1]
11 1 2 1
After:  [2, 6, 2, 1]

Before: [1, 1, 3, 0]
0 3 1 3
After:  [1, 1, 3, 1]

Before: [1, 3, 1, 1]
8 3 3 1
After:  [1, 1, 1, 1]

Before: [2, 3, 1, 3]
9 2 3 2
After:  [2, 3, 3, 3]

Before: [3, 0, 2, 1]
6 3 2 0
After:  [3, 0, 2, 1]

Before: [0, 1, 3, 0]
3 0 0 3
After:  [0, 1, 3, 0]

Before: [1, 0, 2, 1]
6 3 2 2
After:  [1, 0, 3, 1]

Before: [0, 1, 0, 1]
7 0 2 2
After:  [0, 1, 0, 1]

Before: [0, 1, 3, 1]
13 1 3 1
After:  [0, 3, 3, 1]

Before: [0, 1, 0, 1]
5 1 3 3
After:  [0, 1, 0, 1]

Before: [1, 1, 1, 3]
9 1 3 2
After:  [1, 1, 3, 3]

Before: [0, 0, 0, 0]
3 0 0 2
After:  [0, 0, 0, 0]

Before: [0, 2, 0, 1]
3 0 0 0
After:  [0, 2, 0, 1]

Before: [3, 1, 0, 3]
0 2 1 0
After:  [1, 1, 0, 3]

Before: [2, 0, 2, 0]
2 0 3 1
After:  [2, 3, 2, 0]

Before: [2, 1, 1, 3]
9 2 3 3
After:  [2, 1, 1, 3]

Before: [0, 1, 0, 3]
15 0 3 3
After:  [0, 1, 0, 3]

Before: [2, 0, 2, 1]
15 1 2 3
After:  [2, 0, 2, 2]

Before: [2, 1, 1, 3]
9 1 3 3
After:  [2, 1, 1, 3]

Before: [1, 2, 1, 0]
13 2 3 3
After:  [1, 2, 1, 3]

Before: [0, 1, 0, 3]
9 1 3 1
After:  [0, 3, 0, 3]

Before: [0, 3, 2, 1]
3 0 0 2
After:  [0, 3, 0, 1]

Before: [1, 2, 3, 3]
11 1 3 3
After:  [1, 2, 3, 6]

Before: [1, 1, 0, 3]
4 1 0 3
After:  [1, 1, 0, 1]

Before: [1, 0, 0, 3]
9 0 3 3
After:  [1, 0, 0, 3]

Before: [1, 3, 1, 1]
13 0 3 2
After:  [1, 3, 3, 1]

Before: [1, 1, 0, 1]
0 2 1 1
After:  [1, 1, 0, 1]

Before: [1, 1, 0, 2]
4 1 0 2
After:  [1, 1, 1, 2]

Before: [0, 1, 3, 2]
15 1 2 1
After:  [0, 3, 3, 2]

Before: [1, 1, 3, 2]
12 2 2 2
After:  [1, 1, 2, 2]

Before: [3, 1, 3, 2]
6 3 1 1
After:  [3, 3, 3, 2]

Before: [0, 1, 0, 3]
9 1 3 3
After:  [0, 1, 0, 3]

Before: [1, 0, 1, 2]
10 2 3 1
After:  [1, 3, 1, 2]

Before: [2, 1, 2, 2]
10 1 3 1
After:  [2, 3, 2, 2]

Before: [3, 1, 2, 1]
5 1 3 2
After:  [3, 1, 1, 1]

Before: [3, 1, 0, 2]
0 2 1 0
After:  [1, 1, 0, 2]

Before: [2, 1, 3, 1]
12 2 2 3
After:  [2, 1, 3, 2]

Before: [1, 0, 1, 1]
13 2 3 2
After:  [1, 0, 3, 1]

Before: [2, 1, 1, 3]
9 2 3 0
After:  [3, 1, 1, 3]

Before: [1, 1, 2, 0]
0 3 1 3
After:  [1, 1, 2, 1]

Before: [0, 2, 2, 0]
2 2 3 3
After:  [0, 2, 2, 3]

Before: [0, 2, 2, 0]
7 0 1 2
After:  [0, 2, 0, 0]

Before: [1, 2, 3, 3]
11 3 3 0
After:  [9, 2, 3, 3]

Before: [0, 2, 3, 1]
8 3 3 0
After:  [1, 2, 3, 1]

Before: [3, 2, 2, 0]
2 1 3 2
After:  [3, 2, 3, 0]

Before: [3, 1, 3, 1]
13 1 3 0
After:  [3, 1, 3, 1]

Before: [1, 2, 1, 1]
13 2 3 2
After:  [1, 2, 3, 1]

Before: [3, 1, 0, 1]
5 1 3 0
After:  [1, 1, 0, 1]

Before: [1, 0, 1, 3]
9 2 3 2
After:  [1, 0, 3, 3]

Before: [3, 1, 1, 2]
10 2 3 1
After:  [3, 3, 1, 2]

Before: [3, 1, 3, 1]
5 1 3 1
After:  [3, 1, 3, 1]

Before: [2, 1, 1, 0]
13 1 3 3
After:  [2, 1, 1, 3]

Before: [1, 1, 0, 2]
0 2 1 1
After:  [1, 1, 0, 2]

Before: [1, 2, 3, 2]
10 0 3 1
After:  [1, 3, 3, 2]

Before: [1, 0, 1, 3]
1 3 0 0
After:  [3, 0, 1, 3]

Before: [0, 2, 0, 3]
3 0 0 0
After:  [0, 2, 0, 3]

Before: [2, 1, 3, 2]
10 1 3 0
After:  [3, 1, 3, 2]

Before: [1, 1, 2, 3]
1 3 0 0
After:  [3, 1, 2, 3]

Before: [0, 0, 1, 1]
13 2 3 0
After:  [3, 0, 1, 1]

Before: [2, 2, 1, 2]
2 1 3 1
After:  [2, 3, 1, 2]

Before: [0, 3, 3, 2]
12 2 2 3
After:  [0, 3, 3, 2]

Before: [0, 0, 2, 3]
14 3 2 2
After:  [0, 0, 2, 3]

Before: [2, 0, 1, 0]
2 0 3 0
After:  [3, 0, 1, 0]

Before: [1, 1, 1, 2]
10 0 3 3
After:  [1, 1, 1, 3]

Before: [2, 3, 2, 1]
1 2 2 1
After:  [2, 2, 2, 1]

Before: [0, 3, 0, 3]
1 3 1 3
After:  [0, 3, 0, 3]

Before: [1, 2, 3, 3]
14 2 1 0
After:  [2, 2, 3, 3]

Before: [3, 1, 0, 1]
0 2 1 3
After:  [3, 1, 0, 1]

Before: [1, 0, 1, 2]
10 0 3 1
After:  [1, 3, 1, 2]

Before: [3, 3, 2, 3]
1 3 0 2
After:  [3, 3, 3, 3]

Before: [3, 0, 3, 3]
11 3 3 3
After:  [3, 0, 3, 9]

Before: [2, 0, 2, 3]
14 3 2 0
After:  [2, 0, 2, 3]

Before: [3, 3, 2, 3]
11 3 3 2
After:  [3, 3, 9, 3]

Before: [2, 0, 3, 2]
12 2 2 2
After:  [2, 0, 2, 2]

Before: [0, 1, 1, 3]
9 2 3 2
After:  [0, 1, 3, 3]

Before: [1, 2, 1, 1]
8 2 3 2
After:  [1, 2, 1, 1]

Before: [1, 3, 3, 0]
12 2 2 0
After:  [2, 3, 3, 0]

Before: [2, 2, 3, 1]
14 2 1 0
After:  [2, 2, 3, 1]

Before: [1, 3, 2, 0]
2 2 3 3
After:  [1, 3, 2, 3]

Before: [1, 2, 0, 1]
13 0 3 1
After:  [1, 3, 0, 1]

Before: [1, 1, 3, 3]
4 1 0 0
After:  [1, 1, 3, 3]

Before: [1, 1, 3, 2]
15 0 2 2
After:  [1, 1, 3, 2]

Before: [2, 1, 2, 1]
5 1 3 3
After:  [2, 1, 2, 1]

Before: [3, 0, 3, 3]
15 1 3 1
After:  [3, 3, 3, 3]

Before: [3, 0, 3, 3]
11 0 3 1
After:  [3, 9, 3, 3]

Before: [3, 3, 2, 3]
14 0 2 0
After:  [2, 3, 2, 3]

Before: [1, 1, 3, 1]
6 3 2 0
After:  [3, 1, 3, 1]

Before: [2, 0, 2, 2]
2 2 3 3
After:  [2, 0, 2, 3]

Before: [0, 2, 0, 3]
15 2 3 3
After:  [0, 2, 0, 3]

Before: [1, 3, 2, 0]
11 1 2 3
After:  [1, 3, 2, 6]

Before: [1, 1, 0, 0]
0 2 1 2
After:  [1, 1, 1, 0]

Before: [1, 2, 0, 1]
8 3 3 2
After:  [1, 2, 1, 1]

Before: [0, 3, 2, 1]
1 2 2 1
After:  [0, 2, 2, 1]

Before: [2, 0, 0, 3]
1 3 3 0
After:  [3, 0, 0, 3]

Before: [3, 2, 3, 1]
12 2 2 0
After:  [2, 2, 3, 1]

Before: [0, 1, 0, 2]
6 3 1 3
After:  [0, 1, 0, 3]

Before: [3, 2, 2, 0]
14 0 2 3
After:  [3, 2, 2, 2]

Before: [2, 1, 3, 3]
11 2 3 3
After:  [2, 1, 3, 9]

Before: [2, 2, 1, 3]
9 2 3 2
After:  [2, 2, 3, 3]

Before: [3, 0, 0, 1]
8 3 3 2
After:  [3, 0, 1, 1]

Before: [1, 2, 1, 0]
2 1 3 3
After:  [1, 2, 1, 3]

Before: [1, 3, 3, 3]
12 2 2 3
After:  [1, 3, 3, 2]

Before: [0, 1, 1, 1]
5 1 3 2
After:  [0, 1, 1, 1]

Before: [1, 0, 0, 1]
8 3 3 3
After:  [1, 0, 0, 1]

Before: [1, 1, 2, 1]
5 1 3 2
After:  [1, 1, 1, 1]

Before: [2, 2, 2, 3]
15 2 2 0
After:  [4, 2, 2, 3]

Before: [2, 2, 2, 1]
8 3 3 2
After:  [2, 2, 1, 1]

Before: [3, 0, 2, 3]
11 0 3 0
After:  [9, 0, 2, 3]

Before: [3, 0, 3, 1]
6 3 2 1
After:  [3, 3, 3, 1]

Before: [3, 0, 3, 3]
1 3 1 1
After:  [3, 3, 3, 3]

Before: [0, 1, 0, 1]
0 2 1 1
After:  [0, 1, 0, 1]

Before: [2, 1, 0, 1]
5 1 3 3
After:  [2, 1, 0, 1]

Before: [1, 0, 1, 3]
1 3 0 2
After:  [1, 0, 3, 3]

Before: [2, 0, 2, 1]
15 1 2 2
After:  [2, 0, 2, 1]

Before: [0, 0, 2, 2]
7 0 1 0
After:  [0, 0, 2, 2]

Before: [2, 1, 1, 2]
10 1 3 2
After:  [2, 1, 3, 2]

Before: [2, 3, 2, 3]
11 3 3 2
After:  [2, 3, 9, 3]

Before: [0, 3, 3, 2]
7 0 3 0
After:  [0, 3, 3, 2]

Before: [3, 1, 3, 0]
0 3 1 2
After:  [3, 1, 1, 0]

Before: [1, 0, 1, 3]
9 0 3 0
After:  [3, 0, 1, 3]

Before: [2, 1, 2, 2]
1 2 0 1
After:  [2, 2, 2, 2]

Before: [3, 1, 0, 3]
0 2 1 1
After:  [3, 1, 0, 3]

Before: [2, 1, 3, 2]
6 3 1 2
After:  [2, 1, 3, 2]

Before: [0, 0, 1, 3]
9 2 3 1
After:  [0, 3, 1, 3]

Before: [2, 2, 2, 2]
2 1 3 0
After:  [3, 2, 2, 2]

Before: [3, 1, 1, 1]
5 1 3 3
After:  [3, 1, 1, 1]

Before: [1, 1, 2, 1]
11 0 2 3
After:  [1, 1, 2, 2]

Before: [1, 0, 2, 3]
15 0 2 2
After:  [1, 0, 3, 3]

Before: [1, 3, 3, 1]
13 0 3 3
After:  [1, 3, 3, 3]

Before: [2, 1, 3, 2]
6 3 1 0
After:  [3, 1, 3, 2]

Before: [0, 1, 1, 2]
6 3 1 2
After:  [0, 1, 3, 2]

Before: [3, 1, 2, 2]
11 0 2 2
After:  [3, 1, 6, 2]

Before: [2, 3, 2, 0]
2 2 3 1
After:  [2, 3, 2, 0]

Before: [3, 1, 1, 0]
13 1 3 3
After:  [3, 1, 1, 3]

Before: [2, 0, 2, 3]
11 3 3 1
After:  [2, 9, 2, 3]

Before: [1, 3, 3, 1]
12 2 2 1
After:  [1, 2, 3, 1]

Before: [0, 0, 0, 1]
3 0 0 3
After:  [0, 0, 0, 0]

Before: [1, 1, 0, 1]
5 1 3 0
After:  [1, 1, 0, 1]

Before: [1, 1, 0, 3]
4 1 0 0
After:  [1, 1, 0, 3]

Before: [2, 3, 2, 0]
15 0 2 2
After:  [2, 3, 4, 0]

Before: [2, 1, 0, 1]
5 1 3 0
After:  [1, 1, 0, 1]

Before: [1, 2, 3, 3]
1 3 0 0
After:  [3, 2, 3, 3]

Before: [3, 1, 1, 1]
5 1 3 0
After:  [1, 1, 1, 1]

Before: [1, 2, 1, 3]
11 1 3 2
After:  [1, 2, 6, 3]

Before: [1, 1, 0, 2]
10 0 3 2
After:  [1, 1, 3, 2]

Before: [2, 2, 0, 3]
11 1 3 3
After:  [2, 2, 0, 6]

Before: [2, 2, 0, 2]
2 0 3 2
After:  [2, 2, 3, 2]

Before: [1, 1, 2, 1]
8 3 3 2
After:  [1, 1, 1, 1]

Before: [1, 0, 1, 3]
9 2 3 1
After:  [1, 3, 1, 3]

Before: [2, 0, 2, 3]
11 0 3 2
After:  [2, 0, 6, 3]

Before: [1, 1, 2, 0]
13 1 3 1
After:  [1, 3, 2, 0]

Before: [1, 1, 3, 0]
4 1 0 2
After:  [1, 1, 1, 0]

Before: [3, 2, 3, 1]
12 2 2 1
After:  [3, 2, 3, 1]

Before: [0, 2, 3, 3]
7 0 2 1
After:  [0, 0, 3, 3]

Before: [3, 1, 2, 1]
15 2 1 3
After:  [3, 1, 2, 3]

Before: [1, 3, 1, 1]
8 3 3 3
After:  [1, 3, 1, 1]

Before: [1, 1, 0, 1]
4 1 0 3
After:  [1, 1, 0, 1]

Before: [0, 1, 0, 0]
15 0 1 0
After:  [1, 1, 0, 0]

Before: [3, 0, 2, 2]
1 2 2 0
After:  [2, 0, 2, 2]

Before: [0, 0, 2, 0]
3 0 0 0
After:  [0, 0, 2, 0]

Before: [3, 0, 2, 1]
6 3 2 2
After:  [3, 0, 3, 1]

Before: [1, 3, 2, 3]
1 3 3 3
After:  [1, 3, 2, 3]

Before: [1, 1, 2, 1]
4 1 0 3
After:  [1, 1, 2, 1]

Before: [0, 2, 3, 3]
11 2 3 2
After:  [0, 2, 9, 3]

Before: [0, 2, 3, 2]
3 0 0 2
After:  [0, 2, 0, 2]

Before: [1, 0, 2, 1]
11 0 2 3
After:  [1, 0, 2, 2]

Before: [3, 2, 1, 0]
13 2 3 2
After:  [3, 2, 3, 0]

Before: [3, 2, 1, 3]
11 0 3 3
After:  [3, 2, 1, 9]

Before: [3, 0, 2, 3]
11 3 2 2
After:  [3, 0, 6, 3]

Before: [0, 1, 3, 3]
9 1 3 0
After:  [3, 1, 3, 3]

Before: [1, 0, 3, 3]
9 0 3 2
After:  [1, 0, 3, 3]

Before: [2, 1, 2, 0]
0 3 1 3
After:  [2, 1, 2, 1]

Before: [0, 0, 3, 1]
8 3 3 3
After:  [0, 0, 3, 1]

Before: [1, 1, 2, 1]
8 3 3 3
After:  [1, 1, 2, 1]

Before: [1, 2, 2, 3]
11 0 2 3
After:  [1, 2, 2, 2]

Before: [3, 3, 3, 3]
1 3 1 1
After:  [3, 3, 3, 3]

Before: [0, 1, 2, 3]
9 1 3 0
After:  [3, 1, 2, 3]

Before: [1, 1, 0, 3]
1 3 3 0
After:  [3, 1, 0, 3]

Before: [2, 2, 3, 1]
6 3 2 3
After:  [2, 2, 3, 3]

Before: [1, 3, 3, 1]
8 3 3 0
After:  [1, 3, 3, 1]

Before: [0, 2, 3, 1]
7 0 3 0
After:  [0, 2, 3, 1]

Before: [0, 1, 2, 1]
5 1 3 3
After:  [0, 1, 2, 1]

Before: [3, 1, 1, 2]
6 3 1 0
After:  [3, 1, 1, 2]

Before: [1, 1, 2, 1]
5 1 3 3
After:  [1, 1, 2, 1]

Before: [0, 2, 0, 3]
7 0 1 3
After:  [0, 2, 0, 0]

Before: [3, 1, 1, 0]
0 3 1 2
After:  [3, 1, 1, 0]

Before: [3, 1, 0, 1]
5 1 3 3
After:  [3, 1, 0, 1]

Before: [1, 1, 1, 1]
8 2 3 3
After:  [1, 1, 1, 1]

Before: [0, 3, 2, 1]
6 3 2 2
After:  [0, 3, 3, 1]

Before: [0, 2, 1, 3]
3 0 0 3
After:  [0, 2, 1, 0]

Before: [3, 1, 3, 1]
6 3 2 1
After:  [3, 3, 3, 1]

Before: [3, 2, 2, 3]
1 3 0 3
After:  [3, 2, 2, 3]

Before: [3, 2, 1, 1]
8 3 3 2
After:  [3, 2, 1, 1]

Before: [3, 1, 1, 3]
1 3 1 2
After:  [3, 1, 3, 3]

Before: [2, 3, 3, 1]
12 2 2 1
After:  [2, 2, 3, 1]

Before: [3, 1, 3, 0]
0 3 1 1
After:  [3, 1, 3, 0]

Before: [2, 1, 2, 2]
10 1 3 0
After:  [3, 1, 2, 2]

Before: [1, 1, 3, 2]
4 1 0 3
After:  [1, 1, 3, 1]

Before: [0, 1, 0, 0]
7 0 1 3
After:  [0, 1, 0, 0]

Before: [0, 1, 1, 0]
0 3 1 1
After:  [0, 1, 1, 0]

Before: [0, 1, 0, 1]
5 1 3 2
After:  [0, 1, 1, 1]

Before: [2, 1, 1, 1]
5 1 3 1
After:  [2, 1, 1, 1]

Before: [3, 0, 2, 3]
11 0 3 3
After:  [3, 0, 2, 9]

Before: [3, 1, 0, 2]
10 1 3 2
After:  [3, 1, 3, 2]

Before: [1, 2, 2, 3]
9 0 3 2
After:  [1, 2, 3, 3]

Before: [0, 3, 2, 1]
14 1 2 3
After:  [0, 3, 2, 2]

Before: [1, 3, 0, 3]
11 3 3 2
After:  [1, 3, 9, 3]

Before: [0, 0, 2, 1]
6 3 2 2
After:  [0, 0, 3, 1]

Before: [1, 1, 2, 1]
4 1 0 1
After:  [1, 1, 2, 1]

Before: [1, 3, 2, 3]
11 1 2 0
After:  [6, 3, 2, 3]

Before: [2, 2, 1, 0]
2 0 3 3
After:  [2, 2, 1, 3]

Before: [0, 1, 1, 0]
0 3 1 0
After:  [1, 1, 1, 0]

Before: [0, 1, 2, 2]
6 3 1 0
After:  [3, 1, 2, 2]

Before: [1, 3, 3, 2]
15 0 2 0
After:  [3, 3, 3, 2]

Before: [3, 2, 3, 2]
14 2 1 2
After:  [3, 2, 2, 2]

Before: [1, 1, 0, 0]
4 1 0 1
After:  [1, 1, 0, 0]

Before: [0, 1, 3, 0]
0 3 1 0
After:  [1, 1, 3, 0]

Before: [3, 0, 3, 2]
12 2 2 2
After:  [3, 0, 2, 2]

Before: [0, 0, 2, 1]
15 2 2 0
After:  [4, 0, 2, 1]

Before: [3, 3, 0, 1]
8 3 3 0
After:  [1, 3, 0, 1]

Before: [2, 2, 1, 3]
9 2 3 3
After:  [2, 2, 1, 3]

Before: [0, 3, 1, 0]
7 0 1 2
After:  [0, 3, 0, 0]

Before: [1, 3, 2, 2]
14 1 2 2
After:  [1, 3, 2, 2]

Before: [3, 3, 2, 0]
1 2 2 0
After:  [2, 3, 2, 0]

Before: [1, 1, 3, 2]
4 1 0 1
After:  [1, 1, 3, 2]

Before: [1, 0, 2, 2]
1 2 2 0
After:  [2, 0, 2, 2]

Before: [1, 2, 0, 0]
2 1 3 3
After:  [1, 2, 0, 3]

Before: [2, 2, 2, 2]
1 2 0 0
After:  [2, 2, 2, 2]

Before: [0, 3, 2, 2]
1 2 2 2
After:  [0, 3, 2, 2]

Before: [0, 2, 3, 1]
8 3 3 2
After:  [0, 2, 1, 1]

Before: [2, 0, 3, 2]
14 2 0 1
After:  [2, 2, 3, 2]

Before: [1, 1, 1, 3]
4 1 0 1
After:  [1, 1, 1, 3]

Before: [1, 1, 3, 2]
6 3 1 1
After:  [1, 3, 3, 2]

Before: [0, 0, 3, 3]
1 3 1 1
After:  [0, 3, 3, 3]

Before: [3, 1, 3, 2]
6 3 1 0
After:  [3, 1, 3, 2]

Before: [2, 3, 3, 2]
14 2 0 3
After:  [2, 3, 3, 2]

Before: [2, 0, 1, 2]
10 2 3 3
After:  [2, 0, 1, 3]

Before: [2, 1, 2, 3]
1 3 3 0
After:  [3, 1, 2, 3]

Before: [0, 1, 1, 2]
10 2 3 0
After:  [3, 1, 1, 2]

Before: [3, 3, 2, 2]
2 2 3 1
After:  [3, 3, 2, 2]

Before: [1, 1, 0, 2]
4 1 0 0
After:  [1, 1, 0, 2]

Before: [3, 2, 2, 1]
14 0 2 0
After:  [2, 2, 2, 1]

Before: [0, 2, 3, 1]
7 0 1 2
After:  [0, 2, 0, 1]

Before: [1, 1, 2, 3]
11 3 2 2
After:  [1, 1, 6, 3]

Before: [1, 2, 2, 3]
9 0 3 3
After:  [1, 2, 2, 3]

Before: [2, 1, 3, 3]
9 1 3 3
After:  [2, 1, 3, 3]

Before: [0, 1, 3, 1]
5 1 3 3
After:  [0, 1, 3, 1]

Before: [0, 0, 2, 3]
7 0 1 1
After:  [0, 0, 2, 3]

Before: [0, 0, 2, 1]
7 0 2 0
After:  [0, 0, 2, 1]

Before: [0, 1, 0, 3]
1 3 1 1
After:  [0, 3, 0, 3]

Before: [3, 2, 3, 3]
14 2 1 3
After:  [3, 2, 3, 2]

Before: [1, 1, 0, 3]
4 1 0 1
After:  [1, 1, 0, 3]

Before: [0, 1, 1, 1]
5 1 3 3
After:  [0, 1, 1, 1]

Before: [3, 1, 3, 1]
8 3 3 2
After:  [3, 1, 1, 1]

Before: [1, 1, 1, 0]
4 1 0 1
After:  [1, 1, 1, 0]

Before: [1, 2, 2, 3]
15 0 2 0
After:  [3, 2, 2, 3]

Before: [3, 0, 2, 3]
1 3 1 3
After:  [3, 0, 2, 3]

Before: [0, 2, 0, 3]
3 0 0 2
After:  [0, 2, 0, 3]

Before: [2, 3, 0, 3]
15 2 3 2
After:  [2, 3, 3, 3]

Before: [1, 1, 1, 1]
5 1 3 2
After:  [1, 1, 1, 1]

Before: [1, 1, 1, 1]
13 2 3 1
After:  [1, 3, 1, 1]

Before: [2, 2, 2, 1]
15 2 2 3
After:  [2, 2, 2, 4]

Before: [0, 1, 3, 0]
12 2 2 1
After:  [0, 2, 3, 0]

Before: [1, 2, 1, 2]
10 0 3 0
After:  [3, 2, 1, 2]

Before: [1, 0, 3, 1]
12 2 2 0
After:  [2, 0, 3, 1]

Before: [3, 2, 0, 3]
15 2 3 1
After:  [3, 3, 0, 3]

Before: [0, 2, 2, 1]
8 3 3 1
After:  [0, 1, 2, 1]

Before: [2, 2, 1, 3]
9 2 3 1
After:  [2, 3, 1, 3]

Before: [0, 0, 2, 2]
15 2 2 1
After:  [0, 4, 2, 2]

Before: [3, 1, 1, 1]
5 1 3 1
After:  [3, 1, 1, 1]

Before: [1, 1, 3, 1]
5 1 3 2
After:  [1, 1, 1, 1]

Before: [0, 1, 1, 3]
15 0 1 3
After:  [0, 1, 1, 1]

Before: [2, 1, 2, 0]
1 2 0 1
After:  [2, 2, 2, 0]

Before: [0, 1, 1, 0]
3 0 0 1
After:  [0, 0, 1, 0]

Before: [1, 1, 1, 3]
9 2 3 1
After:  [1, 3, 1, 3]

Before: [3, 2, 1, 3]
1 3 3 2
After:  [3, 2, 3, 3]

Before: [0, 1, 2, 3]
7 0 1 1
After:  [0, 0, 2, 3]

Before: [1, 2, 0, 3]
9 0 3 3
After:  [1, 2, 0, 3]

Before: [1, 1, 1, 1]
8 2 3 2
After:  [1, 1, 1, 1]

Before: [0, 0, 1, 1]
13 2 3 2
After:  [0, 0, 3, 1]

Before: [2, 2, 3, 3]
14 2 1 0
After:  [2, 2, 3, 3]

Before: [3, 2, 0, 3]
11 0 3 1
After:  [3, 9, 0, 3]

Before: [0, 1, 1, 2]
10 2 3 2
After:  [0, 1, 3, 2]

Before: [0, 3, 0, 3]
3 0 0 2
After:  [0, 3, 0, 3]

Before: [1, 3, 3, 0]
13 0 3 1
After:  [1, 3, 3, 0]

Before: [1, 3, 1, 1]
13 2 3 1
After:  [1, 3, 1, 1]

Before: [1, 1, 0, 3]
0 2 1 1
After:  [1, 1, 0, 3]

Before: [2, 1, 3, 1]
5 1 3 2
After:  [2, 1, 1, 1]

Before: [0, 1, 0, 3]
1 3 1 0
After:  [3, 1, 0, 3]

Before: [3, 2, 3, 2]
2 1 3 2
After:  [3, 2, 3, 2]

Before: [0, 1, 3, 3]
11 3 3 3
After:  [0, 1, 3, 9]

Before: [1, 1, 0, 2]
6 3 1 1
After:  [1, 3, 0, 2]

Before: [1, 1, 3, 1]
4 1 0 1
After:  [1, 1, 3, 1]

Before: [2, 1, 0, 2]
6 3 1 0
After:  [3, 1, 0, 2]

Before: [0, 0, 2, 3]
1 3 0 2
After:  [0, 0, 3, 3]

Before: [1, 2, 2, 0]
2 2 3 3
After:  [1, 2, 2, 3]

Before: [1, 1, 1, 1]
5 1 3 3
After:  [1, 1, 1, 1]

Before: [3, 2, 2, 0]
14 0 2 2
After:  [3, 2, 2, 0]

Before: [1, 2, 1, 2]
10 2 3 3
After:  [1, 2, 1, 3]

Before: [0, 1, 1, 1]
5 1 3 1
After:  [0, 1, 1, 1]

Before: [3, 2, 2, 0]
15 3 2 3
After:  [3, 2, 2, 2]

Before: [3, 0, 2, 0]
11 0 2 2
After:  [3, 0, 6, 0]

Before: [1, 0, 0, 1]
13 0 3 1
After:  [1, 3, 0, 1]

Before: [0, 1, 3, 3]
9 1 3 3
After:  [0, 1, 3, 3]

Before: [0, 0, 2, 3]
11 2 3 0
After:  [6, 0, 2, 3]

Before: [3, 3, 3, 3]
1 3 0 1
After:  [3, 3, 3, 3]

Before: [2, 3, 1, 0]
13 2 3 3
After:  [2, 3, 1, 3]
"""

program = """
6 1 3 1
6 2 3 2
6 1 2 0
1 0 2 1
13 1 3 1
10 1 3 3
6 1 2 2
6 1 1 1
10 1 0 0
13 0 1 0
10 0 3 3
1 3 2 1
6 3 2 2
6 3 0 0
6 3 1 3
12 0 2 3
13 3 3 3
10 1 3 1
1 1 1 0
6 0 3 1
13 0 0 2
15 2 0 2
6 0 3 3
6 3 2 2
13 2 1 2
13 2 3 2
10 0 2 0
1 0 2 3
13 0 0 0
15 0 2 0
6 3 1 1
6 3 3 2
7 0 2 2
13 2 2 2
10 3 2 3
1 3 2 0
6 2 2 1
6 2 0 2
6 0 0 3
0 3 2 1
13 1 3 1
13 1 1 1
10 0 1 0
1 0 3 3
13 3 0 2
15 2 3 2
13 0 0 0
15 0 3 0
6 0 0 1
12 0 2 1
13 1 3 1
10 1 3 3
1 3 2 1
6 2 1 2
6 0 3 3
6 1 0 0
1 0 2 0
13 0 1 0
13 0 1 0
10 0 1 1
6 3 2 0
13 1 0 3
15 3 1 3
9 2 0 3
13 3 1 3
13 3 2 3
10 1 3 1
1 1 0 2
13 1 0 0
15 0 1 0
6 3 3 1
6 2 3 3
15 0 1 0
13 0 3 0
10 0 2 2
1 2 1 1
6 0 0 0
6 3 2 2
6 2 0 2
13 2 1 2
13 2 3 2
10 2 1 1
6 1 2 2
6 2 0 0
8 0 3 0
13 0 2 0
10 0 1 1
6 3 3 2
6 2 2 0
8 0 3 3
13 3 2 3
10 1 3 1
1 1 3 0
6 3 3 1
6 1 3 3
13 3 2 1
13 1 3 1
10 0 1 0
1 0 2 1
13 1 0 2
15 2 2 2
6 1 1 0
6 3 2 3
1 0 2 0
13 0 3 0
10 1 0 1
1 1 2 3
6 3 2 1
6 2 1 0
6 3 0 2
7 0 2 0
13 0 3 0
10 0 3 3
1 3 0 2
6 2 2 0
13 0 0 3
15 3 2 3
13 1 0 1
15 1 1 1
8 0 3 1
13 1 1 1
10 2 1 2
1 2 0 1
13 2 0 3
15 3 0 3
13 3 0 0
15 0 1 0
6 3 0 2
5 3 2 2
13 2 1 2
13 2 3 2
10 1 2 1
6 3 2 3
13 1 0 0
15 0 2 0
6 3 0 2
14 3 0 2
13 2 2 2
13 2 3 2
10 1 2 1
1 1 2 2
6 2 0 1
6 2 3 3
6 3 0 3
13 3 2 3
10 3 2 2
1 2 2 3
6 2 0 2
13 3 0 1
15 1 3 1
14 1 0 0
13 0 2 0
10 0 3 3
1 3 1 1
6 0 3 3
6 3 2 0
6 0 0 2
7 2 0 3
13 3 1 3
10 1 3 1
6 2 1 3
12 0 2 0
13 0 1 0
10 1 0 1
1 1 2 3
6 2 1 2
6 1 3 0
13 0 0 1
15 1 0 1
1 0 2 2
13 2 3 2
13 2 2 2
10 3 2 3
6 3 1 2
15 0 1 2
13 2 2 2
13 2 1 2
10 3 2 3
1 3 1 0
6 1 0 1
13 3 0 3
15 3 1 3
13 3 0 2
15 2 0 2
13 1 2 1
13 1 2 1
10 0 1 0
1 0 2 1
13 2 0 2
15 2 3 2
6 2 0 3
6 2 3 0
8 0 3 0
13 0 3 0
13 0 1 0
10 1 0 1
13 0 0 2
15 2 2 2
6 1 3 0
1 0 2 3
13 3 2 3
13 3 2 3
10 3 1 1
6 0 1 0
6 0 3 3
0 3 2 0
13 0 2 0
13 0 1 0
10 0 1 1
6 2 1 0
6 2 2 3
8 0 3 0
13 0 1 0
13 0 2 0
10 0 1 1
1 1 3 3
6 3 3 2
13 1 0 0
15 0 1 0
6 2 1 1
9 1 2 0
13 0 1 0
10 0 3 3
1 3 1 2
6 2 1 0
13 1 0 1
15 1 0 1
6 3 1 3
14 3 0 3
13 3 2 3
10 3 2 2
1 2 1 0
13 0 0 3
15 3 2 3
6 1 3 1
6 3 0 2
11 1 3 1
13 1 1 1
10 0 1 0
6 1 3 2
6 0 0 3
6 3 2 1
12 1 2 1
13 1 2 1
10 1 0 0
6 3 1 1
6 1 2 3
6 2 2 2
15 3 1 3
13 3 3 3
13 3 3 3
10 3 0 0
1 0 0 1
6 0 3 0
6 2 1 3
2 2 3 2
13 2 3 2
13 2 2 2
10 1 2 1
1 1 2 0
6 2 3 2
6 0 1 3
6 3 3 1
0 3 2 2
13 2 2 2
13 2 3 2
10 0 2 0
1 0 2 1
6 3 0 0
6 2 2 3
6 0 3 2
7 2 0 0
13 0 3 0
13 0 2 0
10 0 1 1
13 1 0 0
15 0 1 0
6 3 0 2
11 0 3 2
13 2 1 2
13 2 1 2
10 2 1 1
1 1 2 2
6 0 1 1
6 3 1 3
15 0 1 3
13 3 3 3
13 3 3 3
10 3 2 2
1 2 0 3
6 2 0 1
13 1 0 0
15 0 3 0
13 0 0 2
15 2 2 2
4 2 0 0
13 0 2 0
13 0 2 0
10 0 3 3
1 3 1 1
6 1 2 3
13 3 0 0
15 0 1 0
1 0 2 2
13 2 2 2
10 2 1 1
6 3 2 2
6 3 2 0
6 3 0 3
12 3 2 0
13 0 1 0
13 0 2 0
10 1 0 1
1 1 1 0
6 0 1 2
6 2 2 3
6 0 1 1
5 2 3 2
13 2 3 2
10 0 2 0
1 0 2 2
13 0 0 1
15 1 1 1
6 1 2 0
11 0 3 3
13 3 3 3
13 3 3 3
10 2 3 2
1 2 0 0
6 3 3 1
6 3 3 2
6 2 1 3
14 1 3 2
13 2 1 2
10 0 2 0
1 0 0 3
6 1 2 1
6 3 1 2
13 1 0 0
15 0 0 0
13 1 2 2
13 2 3 2
10 3 2 3
1 3 0 1
6 1 2 3
6 2 2 0
6 0 2 2
3 0 3 0
13 0 2 0
13 0 3 0
10 0 1 1
1 1 3 3
6 2 2 0
13 3 0 1
15 1 1 1
11 1 0 2
13 2 3 2
10 2 3 3
1 3 0 2
6 0 2 0
13 2 0 3
15 3 3 3
13 2 0 1
15 1 2 1
14 3 1 3
13 3 3 3
13 3 2 3
10 2 3 2
1 2 0 0
6 0 3 3
6 3 1 1
6 2 0 2
2 2 3 2
13 2 2 2
10 2 0 0
1 0 2 1
6 3 2 0
13 0 0 2
15 2 2 2
0 3 2 0
13 0 1 0
10 0 1 1
1 1 0 3
6 0 2 1
6 0 0 2
6 1 3 0
10 0 0 1
13 1 2 1
10 1 3 3
6 0 1 1
13 0 0 0
15 0 3 0
7 2 0 0
13 0 2 0
10 0 3 3
1 3 2 1
6 2 2 0
6 0 0 3
6 3 1 2
7 0 2 3
13 3 2 3
13 3 1 3
10 3 1 1
6 2 0 3
13 1 0 2
15 2 2 2
6 1 3 0
1 0 2 0
13 0 1 0
13 0 1 0
10 0 1 1
1 1 0 2
13 1 0 0
15 0 2 0
6 3 2 3
6 3 0 1
14 3 0 1
13 1 3 1
10 1 2 2
1 2 0 1
6 2 1 3
6 1 1 2
8 0 3 2
13 2 1 2
10 2 1 1
6 2 1 2
6 3 3 0
6 3 3 3
4 2 0 2
13 2 1 2
10 1 2 1
1 1 1 2
6 1 0 3
6 2 3 1
9 1 0 1
13 1 2 1
10 2 1 2
6 1 3 1
6 2 3 3
6 2 1 0
2 0 3 3
13 3 3 3
10 2 3 2
1 2 1 1
6 3 2 0
6 2 0 2
13 3 0 3
15 3 3 3
9 2 0 0
13 0 2 0
10 0 1 1
1 1 2 2
6 2 2 0
6 0 1 3
6 3 2 1
14 1 0 0
13 0 1 0
10 2 0 2
13 2 0 0
15 0 1 0
13 0 0 1
15 1 2 1
2 1 3 0
13 0 3 0
10 2 0 2
6 3 2 1
6 2 2 0
6 2 3 3
14 1 0 0
13 0 3 0
13 0 3 0
10 0 2 2
1 2 1 0
13 2 0 2
15 2 2 2
6 0 2 3
0 3 2 1
13 1 3 1
10 0 1 0
1 0 3 3
6 0 1 1
6 1 1 0
1 0 2 0
13 0 3 0
10 0 3 3
1 3 3 0
6 1 0 3
6 1 0 1
6 3 2 2
13 1 2 1
13 1 1 1
10 1 0 0
1 0 0 1
6 0 2 0
6 1 1 2
6 2 3 3
6 2 0 0
13 0 1 0
13 0 2 0
10 1 0 1
1 1 1 0
6 1 2 1
6 3 0 2
13 2 0 3
15 3 0 3
13 1 2 1
13 1 3 1
13 1 1 1
10 0 1 0
1 0 3 1
6 3 3 0
12 0 2 0
13 0 3 0
13 0 2 0
10 0 1 1
1 1 0 3
6 3 1 1
6 2 0 0
7 0 2 1
13 1 2 1
10 1 3 3
6 1 0 2
13 2 0 0
15 0 1 0
6 0 1 1
15 0 1 0
13 0 2 0
13 0 3 0
10 0 3 3
1 3 3 1
6 0 2 2
6 1 1 0
6 0 0 3
10 0 0 2
13 2 3 2
10 1 2 1
1 1 2 3
6 3 0 2
6 0 1 1
15 0 1 0
13 0 3 0
10 0 3 3
1 3 3 1
13 3 0 0
15 0 2 0
13 0 0 3
15 3 1 3
6 2 1 2
3 0 3 2
13 2 2 2
13 2 2 2
10 1 2 1
6 1 1 0
13 0 0 3
15 3 0 3
6 3 2 2
5 3 2 3
13 3 1 3
13 3 2 3
10 1 3 1
6 1 0 2
6 2 1 0
6 1 1 3
3 0 3 3
13 3 1 3
10 1 3 1
6 0 2 3
6 2 2 2
6 1 2 0
0 3 2 0
13 0 2 0
10 1 0 1
1 1 3 0
6 2 1 1
0 3 2 3
13 3 2 3
10 0 3 0
1 0 2 1
6 2 3 0
6 0 0 3
0 3 2 2
13 2 3 2
10 2 1 1
1 1 0 2
6 1 3 1
6 3 1 0
13 0 1 0
10 0 2 2
1 2 3 1
6 3 1 2
6 2 3 3
6 2 0 0
9 0 2 0
13 0 1 0
10 0 1 1
1 1 1 3
6 3 2 0
13 1 0 2
15 2 0 2
13 0 0 1
15 1 1 1
7 2 0 2
13 2 1 2
13 2 1 2
10 2 3 3
6 3 1 1
13 0 0 0
15 0 2 0
6 0 1 2
12 1 2 2
13 2 2 2
10 3 2 3
1 3 2 1
6 1 2 2
6 1 3 0
6 2 0 3
10 0 0 2
13 2 1 2
13 2 1 2
10 2 1 1
6 1 1 3
13 1 0 0
15 0 2 0
13 1 0 2
15 2 2 2
11 3 0 0
13 0 3 0
13 0 2 0
10 1 0 1
13 3 0 2
15 2 0 2
6 3 2 0
6 3 3 3
12 0 2 2
13 2 2 2
13 2 1 2
10 2 1 1
1 1 3 2
6 2 3 3
6 2 2 1
2 1 3 3
13 3 2 3
10 2 3 2
1 2 2 3
6 1 3 1
6 2 1 2
6 1 1 0
1 0 2 2
13 2 1 2
10 3 2 3
6 3 0 0
6 3 3 1
6 3 0 2
12 1 2 1
13 1 2 1
10 3 1 3
6 0 1 0
6 2 2 1
9 1 2 1
13 1 3 1
10 1 3 3
1 3 0 1
6 0 2 3
13 2 0 2
15 2 0 2
6 3 0 0
12 0 2 3
13 3 2 3
13 3 2 3
10 3 1 1
1 1 1 3
6 3 3 1
7 2 0 1
13 1 1 1
13 1 3 1
10 1 3 3
1 3 2 0
6 0 2 3
6 1 0 1
13 1 2 2
13 2 2 2
10 2 0 0
6 1 3 3
6 3 2 1
6 3 3 2
13 3 2 3
13 3 3 3
10 0 3 0
1 0 0 1
13 3 0 3
15 3 0 3
13 0 0 2
15 2 2 2
6 2 2 0
0 3 2 3
13 3 2 3
10 3 1 1
1 1 1 0
6 1 1 3
13 3 0 2
15 2 3 2
6 3 2 1
13 3 2 2
13 2 3 2
10 2 0 0
1 0 1 1
6 3 2 3
6 1 3 2
6 0 0 0
12 3 2 3
13 3 1 3
10 1 3 1
1 1 1 3
13 0 0 1
15 1 1 1
6 2 1 2
6 1 3 0
1 0 2 0
13 0 2 0
10 0 3 3
1 3 3 0
6 0 3 3
6 3 1 1
4 2 1 1
13 1 1 1
10 1 0 0
1 0 0 3
6 2 1 1
6 3 2 0
13 2 0 2
15 2 0 2
7 2 0 0
13 0 3 0
13 0 1 0
10 0 3 3
1 3 2 1
6 0 1 0
6 0 3 3
6 2 1 2
0 3 2 3
13 3 2 3
10 1 3 1
6 1 2 3
6 3 1 0
4 2 0 0
13 0 1 0
13 0 1 0
10 0 1 1
1 1 0 3
6 2 0 0
6 3 1 2
13 1 0 1
15 1 0 1
9 0 2 0
13 0 2 0
10 3 0 3
1 3 0 2
13 3 0 0
15 0 2 0
6 1 1 3
15 3 1 0
13 0 1 0
10 2 0 2
1 2 3 0
6 2 1 3
6 0 0 2
6 1 1 1
11 1 3 2
13 2 2 2
10 0 2 0
1 0 3 2
6 0 2 0
6 0 0 3
6 3 1 0
13 0 2 0
10 0 2 2
1 2 3 3
6 3 0 2
13 0 0 0
15 0 2 0
7 0 2 0
13 0 1 0
13 0 3 0
10 3 0 3
1 3 3 2
6 1 0 0
6 2 2 3
11 1 3 3
13 3 3 3
10 3 2 2
1 2 3 1
6 1 1 3
13 0 0 0
15 0 2 0
6 2 3 2
3 0 3 0
13 0 3 0
10 0 1 1
13 2 0 3
15 3 2 3
6 3 3 0
6 0 1 2
5 2 3 0
13 0 2 0
10 1 0 1
1 1 1 3
6 3 1 2
6 3 0 1
6 2 1 0
4 0 1 2
13 2 1 2
10 3 2 3
1 3 2 0
6 0 3 2
6 0 1 1
6 2 2 3
5 2 3 1
13 1 3 1
10 1 0 0
1 0 3 1
13 1 0 2
15 2 1 2
6 2 0 0
13 3 0 3
15 3 3 3
14 3 0 3
13 3 3 3
13 3 3 3
10 1 3 1
1 1 0 2
6 1 0 3
6 1 2 1
3 0 3 1
13 1 3 1
10 1 2 2
1 2 0 1
6 3 1 2
6 0 0 3
5 3 2 2
13 2 1 2
10 1 2 1
1 1 2 0
13 1 0 1
15 1 2 1
6 2 3 2
0 3 2 2
13 2 3 2
10 0 2 0
1 0 1 1
13 3 0 0
15 0 1 0
6 2 2 2
6 1 3 3
1 0 2 0
13 0 1 0
10 1 0 1
1 1 0 3
6 2 2 1
13 1 0 0
15 0 3 0
6 1 1 2
6 2 0 1
13 1 1 1
10 3 1 3
1 3 3 0
6 3 1 2
6 1 0 1
6 2 3 3
13 1 2 3
13 3 2 3
13 3 3 3
10 3 0 0
1 0 3 1
6 1 0 0
6 3 3 3
6 1 1 2
12 3 2 0
13 0 1 0
13 0 2 0
10 0 1 1
1 1 2 2
6 3 0 0
13 0 0 1
15 1 2 1
6 1 1 3
9 1 0 3
13 3 1 3
10 2 3 2
1 2 2 0
6 0 2 2
6 0 0 1
6 1 1 3
10 3 3 1
13 1 2 1
10 0 1 0
1 0 0 1
6 1 1 0
6 2 0 2
6 3 1 3
1 0 2 3
13 3 2 3
10 3 1 1
1 1 2 0
13 3 0 1
15 1 3 1
6 1 0 3
13 1 0 2
15 2 3 2
15 3 1 2
13 2 3 2
10 2 0 0
1 0 2 2
6 1 3 0
10 0 0 1
13 1 2 1
10 2 1 2
1 2 2 1
13 0 0 2
15 2 3 2
6 3 3 0
13 3 2 0
13 0 3 0
10 1 0 1
1 1 0 0
6 0 3 3
13 1 0 1
15 1 0 1
5 3 2 1
13 1 2 1
10 0 1 0
1 0 0 2
13 1 0 1
15 1 2 1
13 1 0 3
15 3 3 3
6 2 1 0
14 3 1 0
13 0 3 0
10 0 2 2
1 2 0 0
"""


def addr(registers, a, b, c):
    registers[c] = registers[a] + registers[b]


def addi(registers, a, b, c):
    registers[c] = registers[a] + b


def mulr(registers, a, b, c):
    registers[c] = registers[a] * registers[b]


def muli(registers, a, b, c):
    registers[c] = registers[a] * b


def banr(registers, a, b, c):
    registers[c] = registers[a] & registers[b]


def bani(registers, a, b, c):
    registers[c] = registers[a] & b


def borr(registers, a, b, c):
    registers[c] = registers[a] | registers[b]


def bori(registers, a, b, c):
    registers[c] = registers[a] | b


def setr(registers, a, b, c):
    registers[c] = registers[a]


def seti(registers, a, b, c):
    registers[c] = a


def gtir(registers, a, b, c):
    registers[c] = 1 if a > registers[b] else 0


def gtri(registers, a, b, c):
    registers[c] = 1 if registers[a] > b else 0


def gtrr(registers, a, b, c):
    registers[c] = 1 if registers[a] > registers[b] else 0


def eqir(registers, a, b, c):
    registers[c] = 1 if a == registers[b] else 0


def eqri(registers, a, b, c):
    registers[c] = 1 if registers[a] == b else 0


def eqrr(registers, a, b, c):
    registers[c] = 1 if registers[a] == registers[b] else 0


ops = {
    addr,
    addi,
    mulr,
    muli,
    banr,
    bani,
    borr,
    bori,
    setr,
    seti,
    gtir,
    gtri,
    gtrr,
    eqir,
    eqri,
    eqrr,
}


def try_ops(before, operation, after):
    valid = []
    for op in ops:
        code = before[:]
        op(code, operation[1], operation[2], operation[3])
        if code == after:
            valid.append(op)
            # print(op)
    return valid


before = None
operation = None
after = None
three_or_more = 0

# Part 2
opcodes = {}
for i in range(16):
    opcodes[i] = list(ops)

for line in samples.splitlines():
    if not line:
        continue
    bm = re.match(r"Before: \[(\d+), (\d+), (\d+), (\d+)\]", line)
    om = re.match(r"(\d+) (\d+) (\d+) (\d+)", line)
    am = re.match(r"After:  \[(\d+), (\d+), (\d+), (\d+)\]", line)
    if bm:
        before = [int(bm.groups()[0]), int(bm.groups()[1]), int(bm.groups()[2]), int(bm.groups()[3])]
        # print(before)

    if om:
        operation = [int(om.groups()[0]), int(om.groups()[1]), int(om.groups()[2]), int(om.groups()[3])]
        # print(operation)

    if am:
        after = [int(am.groups()[0]), int(am.groups()[1]), int(am.groups()[2]), int(am.groups()[3])]
        # print(after)
        valid = try_ops(before, operation, after)
        # Part 1
        if len(valid) >= 3:
            three_or_more += 1

        # Part 2
        to_remove = []
        for op in ops:
            if op not in valid:
                to_remove.append(op)
        for r in to_remove:
            if r in opcodes[operation[0]]:
                opcodes[operation[0]].remove(r)
        if len(opcodes[operation[0]]) == 1:
            # Remove it from others
            for n, v in opcodes.items():
                if n == operation[0]:
                    continue
                if opcodes[operation[0]][0] in v:
                    v.remove(opcodes[operation[0]][0])

# Part 1
print(three_or_more)

# Part 2 - sanity check that all opcodes found
sanity = set()
for n, v in opcodes.items():
    if len(v) > 1:
        raise Exception("Too many")
    if v[0] in sanity:
        raise Exception("Duplicate")
    sanity.add(v[0])

prog_registers = [0, 0, 0, 0]

for line in program.splitlines():
    if not line:
        continue
    om = re.match(r"(\d+) (\d+) (\d+) (\d+)", line)
    operation = [int(om.groups()[0]), int(om.groups()[1]), int(om.groups()[2]),
                 int(om.groups()[3])]
    opcodes[operation[0]][0](prog_registers, operation[1], operation[2], operation[3])

print(prog_registers)