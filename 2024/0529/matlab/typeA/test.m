% 部分拘束typeAのwrench coneを導出する

clear;

addpath('.', '-end');
addpath('function', '-end');

f1 = [0; 1; 0];
f2 = [-1; 0; 0];
f3 = [0; 1; 0];

l1 = [0.0075; 0.003; 0.0];
l2 = [0.005; 0.00275; 0.0];
l3 = [-0.005; 0.003; 0.0];

m1 = [];
m2 = [];
m3 = [];

% エッジの計算
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

[points_x1, points_y1, points_z1] = make_plane(moment_point1, moment_point2);
[points_x2, points_y2, points_z2] = make_plane(moment_point2, moment_point3);
[points_x3, points_y3, points_z3] = make_plane(moment_point3, moment_point1);

% m1, m2, m3で代用できそう
%[x1, y1, z1] = get_wrench_vec(moment_point1);
%[x2, y2, z2] = get_wrench_vec(moment_point2);
%[x3, y3, z3] = get_wrench_vec(moment_point3);

% グラフ描画開始
figure;

hold on;

% wrenchに関する直線を描画
plot3(m1(1), m1(2), m1(3), 'Color', 'k', 'LineWidth', 3.0)
plot3(m2(1), m2(2), m2(3), 'Color', 'k', 'LineWidth', 3.0)
plot3(m3(1), m3(2), m3(3), 'Color', 'k', 'LineWidth', 3.0)

% 平面の作成

mesh1 = mesh(points_x1, points_y1, points_z1, 'FaceColor', 'b', 'LineStyle', 'none', 'FaceAlpha', 0.25);
mesh2 = mesh(points_x2, points_y2, points_z2, 'FaceColor', 'b', 'LineStyle', 'none', 'FaceAlpha', 0.25);
mesh3 = mesh(points_x3, points_y3, points_z3, 'FaceColor', 'b', 'LineStyle', 'none', 'FaceAlpha', 0.25);

plot_edge(moment_point1, moment_point2, moment_point3);

grid on;

%ラベルの描画
xlabel('X  [m]');
ylabel('Y  [m]');
zlabel('Z  [Nm]');

%グラフの範囲を設定
xlim([-1, 1]);
ylim([-1, 1]);
zlim([-0.03, 0.03]);

view(-150, 30);

% 軸線を描画
line([min(xlim) max(xlim)], [0 0], [0 0], 'Color', 'red', 'LineWidth', 3.0);
line([0 0], [min(ylim), max(ylim)], [0 0], 'Color', 'green', 'LineWidth', 3.0);
line([0 0], [0 0], [min(zlim) max(zlim)], 'Color', 'blue', 'LineWidth', 3.0);

hold off;