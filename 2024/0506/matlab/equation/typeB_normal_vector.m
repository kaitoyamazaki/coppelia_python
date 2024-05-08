% 部分拘束typeBの等式に実数値を代入して法線ベクトルを求める

addpath('.', '-end');

% シンボリック変数の設定
syms f1 f2 f3 F Co So l1x l2y l3y

% 方程式の定義

eq1 = f1 + F*So == 0;
eq2 = -f2 + f3 + F*Co == 0;
eq3 = l1x*f1 + l2y*f2 - l3y*f3 == 0;

% 方程式を解く

solutions = solve([eq1,eq2, eq3], [f1, f2, f3]);

disp(solutions.f1);
disp(solutions.f2);
disp(solutions.f3);

F_val = 0.75 * 0.0625 * 9.81;
l1x_val = 0.0075;
l2y_val = 0.00275;
l3y_val = 0.0015;

num_f1 = subs(solutions.f1, [F, l1x, l2y, l3y], [F_val, l1x_val, l2y_val, l3y_val]);
num_f2 = subs(solutions.f2, [F, l1x, l2y, l3y], [F_val, l1x_val, l2y_val, l3y_val]);
num_f3 = subs(solutions.f3, [F, l1x, l2y, l3y], [F_val, l1x_val, l2y_val, l3y_val]);

disp('f1の値 : ');
disp(num_f1);

disp('f2の値 : ');
disp(num_f2);

disp('f3の値 : ');
disp(num_f3);