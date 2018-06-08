function [optx,zmin,is_bounded,sol] = lp(c,A,b)
% [optx,Jmin,is_bounded,sol] = lp(c,A,b)
% This program finds a solution of the standard linear programming problem:
%   minimize    z = c'x
%   subject to  Ax = b, x >= 0
% using the two phase method, where the simplex method is used at each stage.
% optx: an optimal solution.
% zmin: the optimal value. 
% is_bounded: 1 if the solution is bounded; 0 if unbounded.
% sol: 1 if the problem is solvable; 0 if unsolvable.

[m,n] = size(A);
% Phase one
for i = 1:m
	if b(i) < 0
		A(i,:) = -A(i,:);
		b(i) = -b(i);
	endif
endfor
if m == 1
	d = -A;
else
	d = -sum(A);
endif
w0 = sum(b);
H = [A b;c' 0;d -w0]; % The initial simplex table of phase one
index = 1:n;
basis = n+1:n+m;
[H,basis,is_bounded] = simplex(H,basis,index,1);
if H(m+2,n+1) < -1e-10
	sol = 0;
	disp('unsolvable')
	optx = []; zmin = []; is_bounded = [];
else
	sol = 1;
	j = 0;
	for i = 1:n
		j = j+1;
		if H(m+2,j) > 1e-10
			H(:,j) = [];
			index(j) = [];
			j = j-1;
		endif
	endfor
	H(m+2,:) = [];
% Phase two
	[H,basis,is_bounded] = simplex(H,basis,index,2);
	if is_bounded == 1
		optx = zeros(n+m,1);
		[n1,n2] = size(H);
		for i = 1:m
			optx(basis(i)) = H(i,n2);
		endfor
		optx(n+1:n+m,:) = [];
		zmin = -H(n1,n2);
	else
		optx = [];
		zmin = -Inf;
	endif
endif
endfunction
