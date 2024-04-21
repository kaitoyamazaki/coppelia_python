% 方程o式を定義して解いてもらうプログラム

addpath('.', '-end');

% シンボリック変数の定義
syms c1 s1 c2 s2 c3 s3 Co So l1x l1y l2x l2y l3x l3y F f1 f2 f3

% 方程式の定義

eq1 = c1*f1 + c3*f3 + F*Co == 0;
eq2 = s1*f1 - f2 + s3*f3 -F*So == 0;
eq3 = l1x*f1*s1 - l1y*f1*c1 -l2x*f2 + l3x*f3*s3 - l3y*f3*c3 == 0;

% 方程式を解く
solutions = solve([eq1, eq2, eq3], [f1, f2, f3]);

disp(solutions.f1);
disp(solutions.f2);
disp(solutions.f3);