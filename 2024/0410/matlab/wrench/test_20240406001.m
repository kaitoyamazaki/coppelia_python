% 媒介変数を利用した平面の方程式の導出・利用検証
% 全ての力による力モーメント空間をスパンする
clear;

addpath('.', '-end');
%alpha_radius = 1.0e+100000;

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

expected_number_of_rows = 100000;

points = zeros(expected_number_of_rows, 3);
count = 1;

for lamda = 0:0.01:1
    for mu = 0:0.01:1

        point = lamda * moment_point1 + mu * moment_point2;

        if abs(plane1_coefficient(1) * point(1) + plane1_coefficient(2) * point(2) + plane1_coefficient(3) * point(3)) < 1e-10
            points(count, :) = point;
            count = count + 1;
        end
    end
end

points = points(1:count-1, :);

points1_x = reshape(points(1:count-2,1), [], 5);
points1_y = reshape(points(1:count-2,2), [], 5);
points1_z = reshape(points(1:count-2,3), [], 5);

points = zeros(expected_number_of_rows, 3);
count = 1;

for lamda = 0:0.01:1
    for mu = 0:0.01:1

        point = lamda * moment_point2 + mu * moment_point3;

        if abs(plane2_coefficient(1) * point(1) + plane2_coefficient(2) * point(2) + plane2_coefficient(3) * point(3)) < 1e-10
            points(count, :) = point;
            count = count + 1;
        end
    end
end

points = points(1:count-1, :);

points2_x = reshape(points(1:count-2,1), [], 5);
points2_y = reshape(points(1:count-2,2), [], 5);
points2_z = reshape(points(1:count-2,3), [], 5);

points = zeros(expected_number_of_rows, 3);
count = 1;

for lamda = 0:0.01:1
    for mu = 0:0.01:1

        point = lamda * moment_point3 + mu * moment_point1;

        if abs(plane3_coefficient(1) * point(1) + plane3_coefficient(2) * point(2) + plane3_coefficient(3) * point(3)) < 1e-10
            points(count, :) = point;
            count = count + 1;
        end
    end
end

points = points(1:count-1, :);

points3_x = reshape(points(1:count-2,1), [], 5);
points3_y = reshape(points(1:count-2,2), [], 5);
points3_z = reshape(points(1:count-2,3), [], 5);

% プロット初期化
figure;
hold on;

mesh1 = mesh(points1_x, points1_y, points1_z, 'LineStyle', "none", 'FaceColor', 'b', 'FaceAlpha', 0.25);
%s1 = surf(points1_x, points1_y, points1_z, 'EdgeColor', "none", 'FaceColor', 'b', 'FaceAlpha', 0.25);

mesh2 = mesh(points2_x, points2_y, points2_z, 'LineStyle', "none", 'FaceColor', 'r', 'FaceAlpha', 0.25);
%s2 = surf(points2_x, points2_y, points2_z, 'EdgeColor', "none", 'FaceColor', 'b', 'FaceAlpha', 0.25);

mesh3 = mesh(points3_x, points3_y, points3_z, 'LineStyle', "none", 'FaceColor', 'g', 'FaceAlpha', 0.25);
%s3 = surf(points3_x, points3_y, points3_z, 'EdgeColor', "none", 'FaceColor', 'b', 'FaceAlpha', 0.25);

title('Convex Hull of the points on the plane');


quiver3(0, 0, 0, moment_point1(1), moment_point1(2), moment_point1(3), 'k', 'LineWidth', 2.0);
quiver3(0, 0, 0, moment_point2(1), moment_point2(2), moment_point2(3), 'k', 'LineWidth', 2.0);
quiver3(0, 0, 0, moment_point3(1), moment_point3(2), moment_point3(3), 'k', 'LineWidth', 2.0);


% 軸ラベル
xlabel('x');
ylabel('y');
zlabel('z');

% 表示範囲の設定
%axis equal;
xlim([-1, 1]);
ylim([-1, 1]);
zlim([-0.03, 0.03]);

% グリッド表示
grid on;

xlim([-1 1]);
ylim([-1 1]);
zlim([-0.03 0.03]);

% X軸
line([min(get(gca, 'XLim')) max(get(gca, 'XLim'))], [0 0], [0 0], 'Color', 'red', 'LineWidth', 2);

% Y軸
line([0 0], [min(get(gca, 'YLim')) max(get(gca, 'YLim'))], [0 0], 'Color', 'green', 'LineWidth', 2);

% Z軸
line([0 0], [0 0], [min(get(gca, 'ZLim')) max(get(gca, 'ZLim'))], 'Color', 'blue', 'LineWidth', 2);

view(45, 45);


hold off;