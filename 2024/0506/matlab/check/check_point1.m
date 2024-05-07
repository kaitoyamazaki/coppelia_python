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

plane1_coefficient = cross(moment_point1, moment_point2);

expected_number_of_rows = 100000;

points = zeros(expected_number_of_rows, 3);

count = 1;

for lamda = 0:0.05:1
    for mu = 0:0.05:1
        if (lamda + mu <= 1)
            point = lamda * moment_point1 + mu * moment_point2;
            if abs(plane1_coefficient(1) * point(1) + plane1_coefficient(2) * point(2) + plane1_coefficient(3) * point(3)) < 1e-10
                points(count, :) = point;
                count = count + 1;
            end
        end
    end
end

points = points(1:count-1, :);
remainder = rem(count, 5);

points_x = reshape(points(1:count-remainder, 1), [], 5);
points_y = reshape(points(1:count-remainder, 2), [], 5);
points_z = reshape(points(1:count-remainder, 3), [], 5);

x = [0, moment_point1(1)];
y = [0, moment_point1(2)];
z = [0, moment_point1(3)];

x2 = [0, moment_point2(1)];
y2 = [0, moment_point2(2)];
z2 = [0, moment_point2(3)];

x3 = [0, moment_point3(1)];
y3 = [0, moment_point3(2)];
z3 = [0, moment_point3(3)];


% ランダムな点をプロット
while true
    [test_x, test_y, test_z] = search_coordinate();
    if plane1_coefficient(1) * test_x + plane1_coefficient(2) * test_y + plane1_coefficient(3) * test_z >= 0
        break
    end
end

% グラフ描画開始
figure;

hold on;

% wrenchに関する直線を描画
plot3(x, y, z, '-o');
plot3(x2, y2, z2, '-o');
plot3(x3, y3, z3, '-o');

% 平面の作成

mesh = mesh(points_x, points_y, points_z);
plot3(test_x, test_y, test_z, 'o', 'MarkerSize', 10, 'MarkerFaceColor', 'k');
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