function [r1, r2] = golden(f, a, b, n)
  t = (-1 + sqrt(5)) / 2;
  x1 = t * t * (b - a) + a
  x2 = t * (b - a) + a
  y1 = f(x1);
  y2 = f(x2);
  for i=1:n
    if y1 < y2
      b = x2
      x2 = x1;
      y2 = y1;
      x1 = (t ^ 2) * (b - a) + a;
      y1 = f(x1);
    else
      a = x1
      x1 = x2;
      y1 = y2;
      x2 = t * (b - a) + a;
      y2 = f(x2);
    endif

    if x1 > x2
      break
    endif
  endfor
  r1 = a
  r2 = b
endfunction
