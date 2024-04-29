addpath('.', '-end');

syms l1x l1y l2x l2y l3x l3y c1 s1 c2 s2 c3 s3 F s0 c0 

A = [c1 -1 c3;
    s1 0 s3;
    l1x*s1 - l1y*c1 l2y l3x*s3 - l3y*c3];

a = inv(A);

disp(a);