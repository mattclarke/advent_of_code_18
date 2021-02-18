raw_data = """165, 169
334, 217
330, 227
317, 72
304, 232
115, 225
323, 344
161, 204
316, 259
63, 250
280, 205
84, 282
271, 158
190, 296
106, 349
171, 178
203, 108
89, 271
193, 254
111, 210
341, 343
349, 311
143, 172
170, 307
128, 157
183, 315
211, 297
74, 281
119, 164
266, 345
184, 62
96, 142
134, 61
117, 52
318, 72
338, 287
61, 215
323, 255
93, 171
325, 249
183, 171
71, 235
329, 306
322, 219
151, 298
180, 255
336, 291
72, 300
223, 286
179, 257
"""


# raw_data = """1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9
# """

import re


# Part 1
# Extract coords
coords = []
min_x = 100000000
min_y = 100000000
max_x = 0
max_y = 0

for d in raw_data.splitlines():
    m = re.match(r"(\d+),\s(\d+)", d)
    if not m:
        print("Ooops", d)
    c = (int(m.groups()[0]), int(m.groups()[1]))
    coords.append(c)

    min_x = min(c[0], min_x)
    max_x = max(c[0], max_x)
    min_y = min(c[1], min_y)
    max_y = max(c[1], max_y)

# Draw it
# alpha = [chr(i) for i in range(65, 91)]
# letter = 0
#
# for j in range(min_y, max_y + 1):
#     line = ""
#     for i in range(min_x, max_x + 1):
#         if (i,j) in coords:
#             line += alpha[letter]
#             letter += 1
#             if letter == len(alpha):
#                 letter = 0
#         else:
#             line += "."
#     print(line)


def calc_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_closest(a, coords):
    closest = []
    dist = calc_dist(a, coords[0])

    for b in coords:
        d = calc_dist(a, b)
        if d < dist:
            dist = d
            closest = [b]
        elif d == dist:
            # Double match
            closest.append(b)
    return closest


results = {}

for j in range(min_y, max_y + 1):
    for i in range(min_x, max_x + 1):
        # Find closest
        c = get_closest((i,j), coords)
        if len(c) == 1:
            if c[0] in results:
                results[c[0]] += 1
            else:
                results[c[0]] = 1

most = 0
for k, v in results.items():
    most = max(most, v)

print(most)

# Part 2
def get_total_distance(a, coords):
    total = 0

    for b in coords:
        total += calc_dist(a, b)
    return total


limit = 10000 # 32 for test case
count = 0

for j in range(min_y, max_y + 1):
    for i in range(min_x, max_x + 1):
        t = get_total_distance((i,j), coords)
        if t < limit:
            # print("{},{} = {}".format(i,j,t))
            count += 1

print(count)
