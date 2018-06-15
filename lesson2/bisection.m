function [r1, r2] = bisection(f, a, b, n)
  for i = 1:n
    if f((a + b) / 2) > 0
      b = (a + b) / 2
    else
      a = (a + b) / 2
    endif
  endfor
  r1 = a
  r2 = b
endfunction