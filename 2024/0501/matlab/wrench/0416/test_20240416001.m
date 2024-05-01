% 部分拘束typeBのwrench空間を作成する

clear;

addpath('.', '-end');
addpath('function', '-end');

% 力の成分
f1 = [-1; 0; 0];
f2 = [1; 0; 0];
f3 = [1; 0; 0];

% z軸周りの回転行列を設定

theta2 = deg2rad(135);
theta3 = deg2rad(45);

Rz2 = [cos(theta2) -sin(theta2) 0; sin(theta2) cos(theta2) 0; 0 0 1];
Rz3 = [cos(theta3) -sin(theta3) 0; sin(theta3) cos(theta3) 0; 0 0 1];

% 力の成分の変更

f2 = Rz2 * f2;
f3 = Rz3 * f3;

% 位置ベクトル
l1 = [0.00439 0.01386 0];
l2 = [0.00484 0.0 0];
l3 = [-0.01099 0.019282 0];

m1 = [];
m2 = [];
m3 = [];

count = 1;

for i = 0:1
    edit_f1 = i * f1;
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

plane1_coefficient = cross(moment_point1, moment_point2);
plane2_coefficient = cross(moment_point2, moment_point3);
plane3_coefficient = cross(moment_point3, moment_point1);

[points1_x, points1_y, points1_z] = create_plane(moment_point1, moment_point2, plane1_coefficient);
[points2_x, points2_y, points2_z] = create_plane(moment_point2, moment_point3, plane2_coefficient);
[points3_x, points3_y, points3_z] = create_plane(moment_point3, moment_point1, plane3_coefficient);

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
plot3(x, y, z, '-o', 'LineWidth', 5);
plot3(x2, y2, z2, '-o', 'LineWidth', 5);
plot3(x3, y3, z3, '-o', 'LineWidth', 5);

% 平面の作成

mesh1 = mesh(points1_x, points1_y, points1_z, 'FaceColor', 'r');
mesh2 = mesh(points2_x, points2_y, points2_z, 'FaceColor', 'b');
mesh3 = mesh(points3_x, points3_y, points3_z, 'FaceColor', 'g');
% plot3(test_x, test_y, test_z, 'o', 'MarkerSize', 10, 'MarkerFaceColor', 'k');
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