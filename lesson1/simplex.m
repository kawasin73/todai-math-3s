function [H1,basis,is_bounded] = simplex(H,basis,index,s)
% [H1,basis,is_bounded] = simplex(H,basis,index,s)
% H: simplex table.
% basis: the indices of basis.
% index: the indices of x.
% s: 1 for phase one; 2 for phase two.
% H1: new simplex table.
% is_bounded: 1 if the solution is bounded; 0 if unbounded.

switch s
case 1
	s0 = 2;
case 2
	s0 = 1;
endswitch
[n1,n2] = size(H);
sol = 0;
while sol == 0
	[fm,jp] = min(H(n1,1:n2-1));
	if fm >= 0
		is_bounded = 1;    % bounded solution
		sol = 1;
	else
		[hm,ip] = max(H(1:n1-s0,jp));
		if hm <= 0
			is_bounded = 0;  % unbounded solution
			sol = 1;
		else
			for i = 1:n1-s0
				if H(i,jp) > 0
					h1(i) = H(i,n2)/H(i,jp);
				else 
					h1(i) = Inf;
				endif
			endfor
			[minh1,ip] = min(h1);
			basis(ip) = index(jp);
			H = pivot(H,ip,jp);
		endif
	endif
endwhile
H1 = H;
endfunction
