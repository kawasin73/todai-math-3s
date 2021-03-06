# 数理演習2 演習課題2

## 問1

### 黄金分割法

```octave
octave:38> golden(@f1, 0.01, 1, 20)
x1 =  0.38815
x2 =  0.62185
a =  0.38815
a =  0.62185
b =  0.85556
b =  0.76629
a =  0.67702
b =  0.73220
b =  0.71112
a =  0.69005
a =  0.69810
b =  0.70615
a =  0.70117
b =  0.70425
a =  0.70235
a =  0.70307
b =  0.70380
a =  0.70335
b =  0.70363
b =  0.70352
a =  0.70342
b =  0.70348
r1 =  0.70342
r2 =  0.70348
ans =  0.70342
```

### 二分割法

```octave
octave:41> bisection(@f1_1, 0.01, 1, 20)
a =  0.50500
b =  0.75250
a =  0.62875
a =  0.69062
b =  0.72156
b =  0.70609
a =  0.69836
a =  0.70223
b =  0.70416
a =  0.70319
b =  0.70368
a =  0.70344
b =  0.70356
b =  0.70350
a =  0.70347
b =  0.70348
b =  0.70347
b =  0.70347
a =  0.70347
b =  0.70347
r1 =  0.70347
r2 =  0.70347
ans =  0.70347
```

### ニュートン法

```octave
octave:50> newton(@f1_1, @f1_2, 5)
x =  4.0004
x =  3.0021
x =  2.0112
x =  1.0751
x =  0.62020
x =  0.69249
x =  0.70329
x =  0.70347
r =  0.70347
ans =  0.70347
```

### まとめ

全て、`0.70347` に収束した。

## 問2

### 黄金分割法

```octave
octave:44> golden(@f2, 4.1, 5, 20)
x1 =  4.4438
x2 =  4.6562
a =  4.4438
a =  4.6562
b =  4.8687
b =  4.7875
a =  4.7064
b =  4.7565
a =  4.7255
b =  4.7447
b =  4.7374
a =  4.7301
a =  4.7329
b =  4.7357
b =  4.7346
a =  4.7335
b =  4.7342
b =  4.7339
a =  4.7337
b =  4.7338
b =  4.7338
a =  4.7337
r1 =  4.7337
r2 =  4.7338
ans =  4.7337
```

### 二分割法

```octave
octave:46> bisection(@f2_1, 4.1, 5, 20)
a =  4.5500
b =  4.7750
a =  4.6625
a =  4.7188
b =  4.7469
a =  4.7328
b =  4.7398
b =  4.7363
b =  4.7346
a =  4.7337
b =  4.7341
b =  4.7339
b =  4.7338
b =  4.7337
a =  4.7337
b =  4.7337
a =  4.7337
a =  4.7337
a =  4.7337
b =  4.7337
r1 =  4.7337
r2 =  4.7337
ans =  4.7337
```

### ニュートン法

```octave
octave:57> newton(@f2_1, @f2_2, 5)
x =  4.0665
x =  4.0041
x =  4.0019
r =  4.0019
ans =  4.0019
```

```octave
octave:59> newton(@f2_1, @f2_2, 4.5)
x =  4.8785
x =  4.6957
x =  4.7338
r =  4.7338
ans =  4.7338
```

### 考察

この指揮は、たくさんの局所的最適解があるため、黄金分割法、二分割法の場合は、正しく範囲を指定しないと大域的最適解に収束できない。
ニュートン法も正しい出発点を選ばないと大域的最適解に収束しない。
