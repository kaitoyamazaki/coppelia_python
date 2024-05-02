% 方程式を定義して解を導出するプログラム

addpath('.', '-end');

syms f1 f2 f3 F so co l1x l2y l3x

% 方程式の定義

eq1 = f1 + f3 + F*so == 0;
eq2 = -f2 + F*co == 0;
eq3 = l1x*f1 + l2y*f2 + l3x*f3 == 0;

solutions = solve([eq1, eq2, eq3], [f1, f2, f3]);

disp(solutions.f1);
disp(solutions.f2);
disp(solutions.f3);