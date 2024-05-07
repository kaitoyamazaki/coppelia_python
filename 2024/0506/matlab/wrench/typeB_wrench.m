% 部分拘束typeAのwrench coneを導出する
% そこを基にそれぞれの力の大きさを導出する

clear;

addpath('.', '-end');
addpath('function', '-end');

% 力の成分
f1 = [0; 1; 0];
f2 = [-1; 0; 0];
f3 = [1; 0; 0];

% 位置ベクトル
l1 = [0.008; 0.003; 0.0];
l2 = [0.006; 0.027; 0.0];
l3 = [-0.006; 0.015; 0.0];

% wrenchベクトルを格納する箇所
m1 = [];
m2 = [];
m3 = [];

% wrenchベクトルを計算
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

[points_x1, points_y1, points_z1] = create_plane(moment_point1, moment_point2);
[points_x2, points_y2, points_z2] = create_plane(moment_point2, moment_point3);
[points_x3, points_y3, points_z3] = create_plane(moment_point3, moment_point1);

[x1, y1, z1] = get_wrench_vec(moment_point1);
[x2, y2, z2] = get_wrench_vec(moment_point2);
[x3, y3, z3] = get_wrench_vec(moment_point3);

[maxAngle, minAngle, internal_points] = get_angle_range(moment_point1, moment_point2, moment_point3);

%save('data/applay_typeB_wrench_point.mat', 'internal_points');
num_of_solve = 0;

[random_points_in_wrench_typeB, coeff_num] = output_random_wrench_point_coeff_num(moment_point1, moment_point2, moment_point3, internal_points);




% グラフ描画開始
figure;

hold on;

% wrenchに関する直線を描画
plot3(x1, y1, z1, 'Color', 'k', 'LineWidth', 3.0)
plot3(x2, y2, z2, 'Color', 'k', 'LineWidth', 3.0)
plot3(x3, y3, z3, 'Color', 'k', 'LineWidth', 3.0)

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

view(60, -15);

% 軸線を描画
line([min(xlim) max(xlim)], [0 0], [0 0], 'Color', 'red', 'LineWidth', 3.0);
line([0 0], [min(ylim), max(ylim)], [0 0], 'Color', 'green', 'LineWidth', 3.0);
line([0 0], [0 0], [min(zlim) max(zlim)], 'Color', 'blue', 'LineWidth', 3.0);

hold off;