% 方程o式を定義して解いてもらうプログラム

addpath('.', '-end');

% シンボリック変数の定義
syms c1 s1 c2 s2 c3 s3 Co So l1x l1y l2x l2y l3x l3y F f1 f2 f3

% 角度の定義

deg1 = 135;
deg2 = 180;
deg3 = 45;
deg_o = atan2(-0.0065, 0.003);

% 方程式の定義

eq1 = c1*f1 + c3*f3 + F*Co == 0;
eq2 = s1*f1 - f2 + s3*f3 -F*So == 0;
eq3 = l1x*f1*s1 - l1y*f1*c1 -l2x*f2 + l3x*f3*s3 - l3y*f3*c3 == 0;

% 方程式を解く
solutions = solve([eq1, eq2, eq3], [f1, f2, f3]);

disp(solutions.f1);
disp(solutions.f2);
disp(solutions.f3);

c1_val = cos(deg2rad(deg1));
s1_val = sin(deg2rad(deg1));
c2_val = cos(deg2rad(deg2));
s2_val = sin(deg2rad(deg2));
c3_val = cos(deg2rad(deg3));
s3_val = sin(deg2rad(deg3));
Co_val = cos(deg_o);
So_val = sin(deg_o);
l1x_val = 0.006;
l1y_val = 0.016;
l2x_val = 0.005;
l2y_val = 0.014;
l3x_val = -0.001;
l3y_val = 0.019;
F_val = 0.75 * 0.0625 * 9.81;


num_f1 = subs(solutions.f1, [c1, s1, c2, s2, c3, s3, Co, So, l1x, l1y, l2x, l2y, l3x, l3y, F], [c1_val, s1_val, c2_val, s2_val, c3_val, s3_val, Co_val, So_val, l1x_val, l1y_val, l2x_val, l2y_val, l3x_val, l3y_val, F_val]);
num_f2 = subs(solutions.f2, [c1, s1, c2, s2, c3, s3, Co, So, l1x, l1y, l2x, l2y, l3x, l3y, F], [c1_val, s1_val, c2_val, s2_val, c3_val, s3_val, Co_val, So_val, l1x_val, l1y_val, l2x_val, l2y_val, l3x_val, l3y_val, F_val]);
num_f3 = subs(solutions.f3, [c1, s1, c2, s2, c3, s3, Co, So, l1x, l1y, l2x, l2y, l3x, l3y, F], [c1_val, s1_val, c2_val, s2_val, c3_val, s3_val, Co_val, So_val, l1x_val, l1y_val, l2x_val, l2y_val, l3x_val, l3y_val, F_val]);

disp('f1の値 : ');
disp(num_f1);

disp('f2の値 : ');
disp(num_f2);

disp('f3の値 : ');
disp(num_f3);