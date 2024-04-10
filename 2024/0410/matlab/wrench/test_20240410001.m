% 境界の上限をチェックするプログラム

clear;

addpath('.', '-end');

% 力の成分
f1 = [0 1 0];
f2 = [-1 0 0];
f3 = [1 0 0];

% 位置ベクトル
l1 = [0.0075 0.03 0];
l2 = [0.005 0.0275 0];
l3 = [-0.005 0.015 0];

m1 = [];
m2 = [];
m3 = [];

count = 1;

for i = 0:1
    edit_f1= i * f1;
    edit_f2 = i * f2;
    edit_f3 = i * f3;

    now_moment1 = cross(l1, edit_f1);
    now_moment2 = cross(l2, edit_f2);
    now_moment3 = cross(l3, edit_f3);

    wrench_f1 = [edit_f1(1) edit_f1(2) now_moment1(3)];
    wrench_f2 = [edit_f2(1) edit_f2(2) now_moment2(3)];
    wrench_f3 = [edit_f3(1) edit_f3(2) now_moment3(3)];

    m1 = [m1; wrench_f1];
    m2 = [m2; wrench_f2];
    m3 = [m3; wrench_f3];
end

moment_point1 = m1(end, :);
moment_point2 = m2(end, :);
moment_point3 = m3(end, :);

%plane1_coefficient = cross(moment_point1, moment_point2);

x = [0, moment_point1(1)];
y = [0, moment_point1(2)];
z = [0, moment_point1(3)];

x2 = [0, moment_point2(1)];
y2 = [0, moment_point2(2)];
z2 = [0, moment_point2(3)];

x3 = [0, moment_point3(1)];
y3 = [0, moment_point3(2)];
z3 = [0, moment_point3(3)];

% グラフ描画開始
figure;

hold on;

% wrenchに関する直線を描画
plot3(x, y, z, '-o');
plot3(x2, y2, z2, '-o');
plot3(x3, y3, z3, '-o');
grid on;

% ラベルの描画
xlabel('X');
ylabel('Y');
zlabel('Z');

% グラフの範囲を設定
xlim([-1, 1]);
ylim([-1, 1]);
zlim([-0.03, 0.03]);

view(45, 45);

% 軸線を描画
line([min(xlim) max(xlim)], [0 0], [0 0], 'Color', 'red', 'LineWidth', 2);
line([0 0], [min(ylim) max(ylim)], [0 0], 'Color', 'green', 'LineWidth', 2);
line([0 0], [0 0], [min(zlim) max(zlim)], 'Color', 'blue', 'LineWidth', 2);

hold off;