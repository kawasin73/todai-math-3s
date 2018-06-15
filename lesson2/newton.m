function [r] = newton(f1, f2, x)
  while(true)
    diff = f1(x) / f2(x);
    if abs(diff) < 0.0001
      break
    end
    x = x - diff
  endwhile
  r = x
endfunction
