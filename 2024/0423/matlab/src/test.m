% シンボリック変数の定義
syms a b c d e f x y

% 方程式の定義

eq1 = a*x + b*y - c == 0;
eq2 = d*x + e * y - f == 0;

% 方程式を解く
solutions = solve([eq1, eq2], [x, y]);

% 特定の値を与える

a_val = 1; b_val = 2; c_val = 3;
d_val = 4; e_val = 5; f_val = 6;

num_x = subs(solutions.x, [a, b, c, d, e, f], [a_val, b_val, c_val, d_val, e_val, f_val]);
num_y = subs(solutions.y, [a, b, c, d, e, f], [a_val, b_val, c_val, d_val, e_val, f_val]);

% 数値解を表示

disp('xの値 : ')
disp(num_x);

disp('yの値 : ')
disp(num_y);