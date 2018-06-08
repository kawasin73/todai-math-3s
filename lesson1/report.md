# 課題

## 課題１

G5 ~ G7 はスラック変数とする

### 標準形

```
min(-5000 * G1 - 6000 * G2 - 7000 * G3 -8000 * G4)

subject to:

2 * G1 + 3 * G2 + 4 * G3 + 6 * G4 + G5 = 150
    G1 + 4 * G2 + 5 * G3 + 3 * G4 + G6 = 180
3 * G1 + 4 * G2 +     G3 + 2 * G4 + G7 = 120

Gn >= 0 (n は 1から7) 
```

### コマンド

```
A = [
2 3 4 6 1 0 0;
1 4 5 3 0 1 0;
3 4 1 2 0 0 1
]
b = [150 180 120]'
c = [-5000 -6000 -7000 -8000 0 0 0]'
[optx,Jmin,is_bounded,sol] = lp(c,A,b)
```

### 結果

```
octave:13> [optx,Jmin,is_bounded,sol] = lp(c,A,b)
optx =

   33.00000
    0.00000
   21.00000
    0.00000
    0.00000
   42.00000
    0.00000

Jmin = -312000
is_bounded =  1
sol =  1
```

最適解は、(G1, G2, G3, G4) = (33, 0, 21, 0) の時で、`312000`円の利益が得られる。

## 課題2

テレビ、ラジオ、新聞、週刊誌、広告板 の広告費投下量をそれぞれ、`x1`, `x2`, `x3`, `x4`, `x5` とおく(単位は万円)
x6 ~ x11 はスラック変数とする

### 標準形

```
min(-3 * x1 - 2 * x2 - 2.5 * x3 - 2 * x4 - 1.5 * x5)
subject to:
 0.6 * x1 + 0.6 * x2 - 0.4 * x3 - 0.4 * x4 - 0.4 * x5 + x6 = 0
-0.9 * x1 - 0.9 * x2 + 0.1 * x3 + 0.1 * x4 + 0.1 * x5 + x7 = 0
-0.2 * x1 - 0.2 * x2 - 0.2 * x3 + 0.8 * x4 - 0.2 * x5 + x8 = 0
 0.1 * x1 -       x2                                  + x9 = 0
                                      - x4 +       x5 + x10 = 0
x1 + x2 + x3 + x4 + x5 + x11 = 100000
xn >= 0 (n は 1から11)
```

### コマンド

```
A = [0.6 0.6 -0.4 -0.4 -0.4 1 0 0 0 0 0;
-0.9 -0.9 0.1 0.1 0.1 0 1 0 0 0 0;
-0.2 -0.2 -0.2 0.8 -0.2 0 0 1 0 0 0;
0.1 -1 0 0 0 0 0 0 1 0 0;
0 0 0 -1 1 0 0 0 0 1 0;
1 1 1 1 1 0 0 0 0 0 1]
b = [0 0 0 0 0 100000]'
c = [-3 -2 -2.5 -2 -1.5 0 0 0 0 0 0]'
[optx,Jmin,is_bounded,sol] = lp(c,A,b)
```

### 結果

```
octave:7> [optx,Jmin,is_bounded,sol] = lp(c,A,b)
optx =

   3.6364e+04
   3.6364e+03
   6.0000e+04
   0.0000e+00
   0.0000e+00
   0.0000e+00
   3.0000e+04
   2.0000e+04
   0.0000e+00
   0.0000e+00
   0.0000e+00

Jmin =   -2.6636e+05
is_bounded =  1
sol =  1
```

(x1, x2, x3, x4, x5) = (36364, 3636, 60000, 0, 0) の時、26億6360万円の効果を得られる

## 課題3

A, B, C, D を生産する量をそれぞれ `a`, `b`, `c`, `d` とする。(単位はkl)
x1 ~ x4 はスラック変数とする

### 標準形

```
min(-26 * a - 35 * b - 14 * c - 15 * d)
subject to:
1.3 * a + 0.9 * b + 1.4 * c     + x1 = 300
0.6 * a + 0.4 * b +         + d + x2 = 200
      a                         + x3 = 180
                b               + x4 = 170
a, b, c, d, xn >= 0 (n は 1から4)
```

### コマンド

```
A = [1.3 0.9 1.4 0 1 0 0 0;
0.6 0.4 0 1.0 0 1 0 0;
1 0 0 0 0 0 1 0;
0 1 0 0 0 0 0 1]
b = [300 200 180 170]'
c = [-26 -35 -14 -15 0 0 0 0]'
[optx,Jmin,is_bounded,sol] = lp(c,A,b)
```

### 結果

```
octave:11> [optx,Jmin,is_bounded,sol] = lp(c,A,b)
optx =

   113.07692
   170.00000
     0.00000
    64.15385
     0.00000
     0.00000
    66.92308
     0.00000

Jmin = -9852.3
is_bounded =  1
sol =  1
```

(a, b, c, d) = (113.07, 170.0, 0, 64.15) の時、9852.3千円の利益が得られる

## 課題4

A, B, C のそれぞれの 混合率を、 a, b, c とする
x1 ~ x4 はスラック変数とする 

### 標準形

```
min(-20 * a - 18 * b - 23 * c)
-250 * a - 240 * b - 260 * c + x1 = -250
-0.92 * a - 1.10 * b - 0.98 * c + x2 = -1.00
10.2 * a + 9.5 * b + 9.5 * c + x3 = 10
0.9 * a + 0.8 * b + 1.0 * c + x4 = 1.0
a + b + c = 1.0
```

### コマンド

```
A = [-250 -240 -260 1 0 0 0;
-0.92 -1.10 -0.98 0 1 0 0;
10.2 9.5 9.5 0 0 1 0;
0.9 0.8 1.0 0 0 0 1;
1 1 1 0 0 0 0]
b = [-250 -1.00 10 1.0 1.0]'
c = [-20 -18 -23 0 0 0 0]'
[optx,Jmin,is_bounded,sol] = lp(c,A,b)
```

### 結果

```
octave:15> [optx,Jmin,is_bounded,sol] = lp(c,A,b)
optx =

   0.00000
   0.16667
   0.83333
   6.66667
   0.00000
   0.50000
   0.03333

Jmin = -22.167
is_bounded =  1
sol =  1
```

(a, b, c) = (0, 0.166, 0.833) の時最も経済的になる

### その２

```
b = [-249 -1.00 10 1.0 1.0]'
```

に変えて行うと

#### 結果

```
octave:19> [optx,Jmin,is_bounded,sol] = lp(c,A,b)
optx =

   0.00000
   0.16667
   0.83333
   7.66667
   0.00000
   0.50000
   0.03333

Jmin = -22.167
is_bounded =  1
sol =  1
```

温度を変えても変わらない。
