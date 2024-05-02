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

F_val = 0.75 * 0.0625 * 9.81;
l1x_val = 0.008;
l2y_val = 0.027;
l3x_val = -0.012;

num_f1 = subs(solutions.f1, [F, l1x, l2y, l3x], [F_val, l1x_val, l2y_val, l3x_val]);
num_f2 = subs(solutions.f2, [F, l1x, l2y, l3x], [F_val, l1x_val, l2y_val, l3x_val]);
num_f3 = subs(solutions.f3, [F, l1x, l2y, l3x], [F_val, l1x_val, l2y_val, l3x_val]);

disp('f1の値 : ');
disp(num_f1);

disp('f2の値 : ');
disp(num_f2);

disp('f3の値 : ');
disp(num_f3);