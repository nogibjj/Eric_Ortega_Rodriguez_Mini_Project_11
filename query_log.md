```sql

                    SELECT 
                        a."Name/Alias", 
                        SUM(a.Appearances) AS total_appearances, 
                        COUNT(b.battle_id) AS total_battles
                    FROM 
                        Avengers a
                    JOIN 
                        Battles b ON a.avenger_id = b.avenger_id
                    GROUP BY 
                        a."Name/Alias"
                    HAVING 
                        SUM(a.Appearances) > 100  -- Only Avengers with more than 100 appearances
                    ORDER BY 
                        total_battles DESC, total_appearances DESC
                
```

```response from databricks
E
r
r
o
r
:
 


[
P
A
R
S
E
_
S
Y
N
T
A
X
_
E
R
R
O
R
]
 
S
y
n
t
a
x
 
e
r
r
o
r
 
a
t
 
o
r
 
n
e
a
r
 
'
"
N
a
m
e
/
A
l
i
a
s
"
'
.
 
S
Q
L
S
T
A
T
E
:
 
4
2
6
0
1
 
(
l
i
n
e
 
3
,
 
p
o
s
 
2
6
)




=
=
 
S
Q
L
 
=
=




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
S
E
L
E
C
T
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
.
"
N
a
m
e
/
A
l
i
a
s
"
,
 


-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
^
^
^


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
S
U
M
(
a
.
A
p
p
e
a
r
a
n
c
e
s
)
 
A
S
 
t
o
t
a
l
_
a
p
p
e
a
r
a
n
c
e
s
,
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
C
O
U
N
T
(
b
.
b
a
t
t
l
e
_
i
d
)
 
A
S
 
t
o
t
a
l
_
b
a
t
t
l
e
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
F
R
O
M
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
A
v
e
n
g
e
r
s
 
a


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
J
O
I
N
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
B
a
t
t
l
e
s
 
b
 
O
N
 
a
.
a
v
e
n
g
e
r
_
i
d
 
=
 
b
.
a
v
e
n
g
e
r
_
i
d


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
G
R
O
U
P
 
B
Y
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
.
"
N
a
m
e
/
A
l
i
a
s
"


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
H
A
V
I
N
G
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
S
U
M
(
a
.
A
p
p
e
a
r
a
n
c
e
s
)
 
>
 
1
0
0
 
 
-
-
 
O
n
l
y
 
A
v
e
n
g
e
r
s
 
w
i
t
h
 
m
o
r
e
 
t
h
a
n
 
1
0
0
 
a
p
p
e
a
r
a
n
c
e
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
O
R
D
E
R
 
B
Y
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
o
t
a
l
_
b
a
t
t
l
e
s
 
D
E
S
C
,
 
t
o
t
a
l
_
a
p
p
e
a
r
a
n
c
e
s
 
D
E
S
C


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


```

```sql

                    SELECT 
                        a."Name/Alias", 
                        SUM(a.Appearances) AS total_appearances, 
                        COUNT(b.battle_id) AS total_battles
                    FROM 
                        Avengers a
                    JOIN 
                        Battles b ON a.avenger_id = b.avenger_id
                    GROUP BY 
                        a."Name/Alias"
                    HAVING 
                        SUM(a.Appearances) > 100  -- Only Avengers with more than 100 appearances
                    ORDER BY 
                        total_battles DESC, total_appearances DESC
                
```

```response from databricks
E
r
r
o
r
:
 


[
P
A
R
S
E
_
S
Y
N
T
A
X
_
E
R
R
O
R
]
 
S
y
n
t
a
x
 
e
r
r
o
r
 
a
t
 
o
r
 
n
e
a
r
 
'
"
N
a
m
e
/
A
l
i
a
s
"
'
.
 
S
Q
L
S
T
A
T
E
:
 
4
2
6
0
1
 
(
l
i
n
e
 
3
,
 
p
o
s
 
2
6
)




=
=
 
S
Q
L
 
=
=




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
S
E
L
E
C
T
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
.
"
N
a
m
e
/
A
l
i
a
s
"
,
 


-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
^
^
^


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
S
U
M
(
a
.
A
p
p
e
a
r
a
n
c
e
s
)
 
A
S
 
t
o
t
a
l
_
a
p
p
e
a
r
a
n
c
e
s
,
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
C
O
U
N
T
(
b
.
b
a
t
t
l
e
_
i
d
)
 
A
S
 
t
o
t
a
l
_
b
a
t
t
l
e
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
F
R
O
M
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
A
v
e
n
g
e
r
s
 
a


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
J
O
I
N
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
B
a
t
t
l
e
s
 
b
 
O
N
 
a
.
a
v
e
n
g
e
r
_
i
d
 
=
 
b
.
a
v
e
n
g
e
r
_
i
d


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
G
R
O
U
P
 
B
Y
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
.
"
N
a
m
e
/
A
l
i
a
s
"


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
H
A
V
I
N
G
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
S
U
M
(
a
.
A
p
p
e
a
r
a
n
c
e
s
)
 
>
 
1
0
0
 
 
-
-
 
O
n
l
y
 
A
v
e
n
g
e
r
s
 
w
i
t
h
 
m
o
r
e
 
t
h
a
n
 
1
0
0
 
a
p
p
e
a
r
a
n
c
e
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
O
R
D
E
R
 
B
Y
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
o
t
a
l
_
b
a
t
t
l
e
s
 
D
E
S
C
,
 
t
o
t
a
l
_
a
p
p
e
a
r
a
n
c
e
s
 
D
E
S
C


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


```

```sql

                    SELECT 
                        a."Name/Alias", 
                        SUM(a.Appearances) AS total_appearances, 
                        COUNT(b.battle_id) AS total_battles
                    FROM 
                        Avengers a
                    JOIN 
                        Battles b ON a.avenger_id = b.avenger_id
                    GROUP BY 
                        a."Name/Alias"
                    HAVING 
                        SUM(a.Appearances) > 100  -- Only Avengers with more than 100 appearances
                    ORDER BY 
                        total_battles DESC, total_appearances DESC
                
```

```response from databricks
E
r
r
o
r
:
 


[
P
A
R
S
E
_
S
Y
N
T
A
X
_
E
R
R
O
R
]
 
S
y
n
t
a
x
 
e
r
r
o
r
 
a
t
 
o
r
 
n
e
a
r
 
'
"
N
a
m
e
/
A
l
i
a
s
"
'
.
 
S
Q
L
S
T
A
T
E
:
 
4
2
6
0
1
 
(
l
i
n
e
 
3
,
 
p
o
s
 
2
6
)




=
=
 
S
Q
L
 
=
=




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
S
E
L
E
C
T
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
.
"
N
a
m
e
/
A
l
i
a
s
"
,
 


-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
^
^
^


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
S
U
M
(
a
.
A
p
p
e
a
r
a
n
c
e
s
)
 
A
S
 
t
o
t
a
l
_
a
p
p
e
a
r
a
n
c
e
s
,
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
C
O
U
N
T
(
b
.
b
a
t
t
l
e
_
i
d
)
 
A
S
 
t
o
t
a
l
_
b
a
t
t
l
e
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
F
R
O
M
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
A
v
e
n
g
e
r
s
 
a


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
J
O
I
N
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
B
a
t
t
l
e
s
 
b
 
O
N
 
a
.
a
v
e
n
g
e
r
_
i
d
 
=
 
b
.
a
v
e
n
g
e
r
_
i
d


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
G
R
O
U
P
 
B
Y
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
.
"
N
a
m
e
/
A
l
i
a
s
"


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
H
A
V
I
N
G
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
S
U
M
(
a
.
A
p
p
e
a
r
a
n
c
e
s
)
 
>
 
1
0
0
 
 
-
-
 
O
n
l
y
 
A
v
e
n
g
e
r
s
 
w
i
t
h
 
m
o
r
e
 
t
h
a
n
 
1
0
0
 
a
p
p
e
a
r
a
n
c
e
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
O
R
D
E
R
 
B
Y
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
o
t
a
l
_
b
a
t
t
l
e
s
 
D
E
S
C
,
 
t
o
t
a
l
_
a
p
p
e
a
r
a
n
c
e
s
 
D
E
S
C


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


```

```sql

                    SELECT 
                        a."Name/Alias", 
                        SUM(a.Appearances) AS total_appearances, 
                        COUNT(b.battle_id) AS total_battles
                    FROM 
                        Avengers a
                    JOIN 
                        Battles b ON a.avenger_id = b.avenger_id
                    GROUP BY 
                        a."Name/Alias"
                    HAVING 
                        SUM(a.Appearances) > 100  -- Only Avengers with more than 100 appearances
                    ORDER BY 
                        total_battles DESC, total_appearances DESC
                
```

```response from databricks
E
r
r
o
r
:
 


[
P
A
R
S
E
_
S
Y
N
T
A
X
_
E
R
R
O
R
]
 
S
y
n
t
a
x
 
e
r
r
o
r
 
a
t
 
o
r
 
n
e
a
r
 
'
"
N
a
m
e
/
A
l
i
a
s
"
'
.
 
S
Q
L
S
T
A
T
E
:
 
4
2
6
0
1
 
(
l
i
n
e
 
3
,
 
p
o
s
 
2
6
)




=
=
 
S
Q
L
 
=
=




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
S
E
L
E
C
T
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
.
"
N
a
m
e
/
A
l
i
a
s
"
,
 


-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
^
^
^


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
S
U
M
(
a
.
A
p
p
e
a
r
a
n
c
e
s
)
 
A
S
 
t
o
t
a
l
_
a
p
p
e
a
r
a
n
c
e
s
,
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
C
O
U
N
T
(
b
.
b
a
t
t
l
e
_
i
d
)
 
A
S
 
t
o
t
a
l
_
b
a
t
t
l
e
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
F
R
O
M
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
A
v
e
n
g
e
r
s
 
a


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
J
O
I
N
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
B
a
t
t
l
e
s
 
b
 
O
N
 
a
.
a
v
e
n
g
e
r
_
i
d
 
=
 
b
.
a
v
e
n
g
e
r
_
i
d


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
G
R
O
U
P
 
B
Y
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
.
"
N
a
m
e
/
A
l
i
a
s
"


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
H
A
V
I
N
G
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
S
U
M
(
a
.
A
p
p
e
a
r
a
n
c
e
s
)
 
>
 
1
0
0
 
 
-
-
 
O
n
l
y
 
A
v
e
n
g
e
r
s
 
w
i
t
h
 
m
o
r
e
 
t
h
a
n
 
1
0
0
 
a
p
p
e
a
r
a
n
c
e
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
O
R
D
E
R
 
B
Y
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
o
t
a
l
_
b
a
t
t
l
e
s
 
D
E
S
C
,
 
t
o
t
a
l
_
a
p
p
e
a
r
a
n
c
e
s
 
D
E
S
C


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


```

```sql

                    SELECT 
                        a."Name/Alias", 
                        SUM(a.Appearances) AS total_appearances, 
                        COUNT(b.battle_id) AS total_battles
                    FROM 
                        Avengers a
                    JOIN 
                        Battles b ON a.avenger_id = b.avenger_id
                    GROUP BY 
                        a."Name/Alias"
                    HAVING 
                        SUM(a.Appearances) > 100  -- Only Avengers with more than 100 appearances
                    ORDER BY 
                        total_battles DESC, total_appearances DESC
                
```

```response from databricks
E
r
r
o
r
:
 


[
P
A
R
S
E
_
S
Y
N
T
A
X
_
E
R
R
O
R
]
 
S
y
n
t
a
x
 
e
r
r
o
r
 
a
t
 
o
r
 
n
e
a
r
 
'
"
N
a
m
e
/
A
l
i
a
s
"
'
.
 
S
Q
L
S
T
A
T
E
:
 
4
2
6
0
1
 
(
l
i
n
e
 
3
,
 
p
o
s
 
2
6
)




=
=
 
S
Q
L
 
=
=




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
S
E
L
E
C
T
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
.
"
N
a
m
e
/
A
l
i
a
s
"
,
 


-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
^
^
^


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
S
U
M
(
a
.
A
p
p
e
a
r
a
n
c
e
s
)
 
A
S
 
t
o
t
a
l
_
a
p
p
e
a
r
a
n
c
e
s
,
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
C
O
U
N
T
(
b
.
b
a
t
t
l
e
_
i
d
)
 
A
S
 
t
o
t
a
l
_
b
a
t
t
l
e
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
F
R
O
M
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
A
v
e
n
g
e
r
s
 
a


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
J
O
I
N
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
B
a
t
t
l
e
s
 
b
 
O
N
 
a
.
a
v
e
n
g
e
r
_
i
d
 
=
 
b
.
a
v
e
n
g
e
r
_
i
d


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
G
R
O
U
P
 
B
Y
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
.
"
N
a
m
e
/
A
l
i
a
s
"


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
H
A
V
I
N
G
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
S
U
M
(
a
.
A
p
p
e
a
r
a
n
c
e
s
)
 
>
 
1
0
0
 
 
-
-
 
O
n
l
y
 
A
v
e
n
g
e
r
s
 
w
i
t
h
 
m
o
r
e
 
t
h
a
n
 
1
0
0
 
a
p
p
e
a
r
a
n
c
e
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
O
R
D
E
R
 
B
Y
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
o
t
a
l
_
b
a
t
t
l
e
s
 
D
E
S
C
,
 
t
o
t
a
l
_
a
p
p
e
a
r
a
n
c
e
s
 
D
E
S
C


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


```

