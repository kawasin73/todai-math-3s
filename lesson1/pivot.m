function H1 = pivot(H,ip,jp)
% H1 = pivot(H,ip,jp)
[n,m] = size(H);
piv = H(ip,jp);
if piv == 0
	disp('singular')
else
	H(ip,:) = H(ip,:)/piv;
	for i = 1:n
		if i != ip
			H(i,:) = H(i,:) - H(i,jp)*H(ip,:);
		endif
	endfor
endif
H1 = H;
endfunction
