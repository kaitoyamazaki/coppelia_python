% 凸包内の点を見つけるためのプログラム
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

count = 1;

for i = 0:0.01:1
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
    count = count + 1;
end

moment_point1 = m1(end, :);
moment_point2 = m2(end, :);
moment_point3 = m3(end, :);

in_hull_points = [];

count2 = 1;

for i = 1:count-1
    for alpha = 0:0.01:1
        for beta = 0:0.01:(1-alpha)
            gammar = 1 - alpha - beta;

            force_moment = alpha * m1(i,:) + beta * m2(i,:) + gammar * m3(i,:);

            in_hull_points = [in_hull_points; force_moment];
            count2 = count2 + 1;
        end
    end
end

% プロット初期化
figure;
hold on;

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

plot3(in_hull_points(:,1), in_hull_points(:,2), in_hull_points(:,3), '.', 'Color', 'b');

% グリッド表示
grid on;

% X軸
line([min(get(gca, 'XLim')) max(get(gca, 'XLim'))], [0 0], [0 0], 'Color', 'red', 'LineWidth', 2);

% Y軸
line([0 0], [min(get(gca, 'YLim')) max(get(gca, 'YLim'))], [0 0], 'Color', 'green', 'LineWidth', 2);

% Z軸
line([0 0], [0 0], [min(get(gca, 'ZLim')) max(get(gca, 'ZLim'))], 'Color', 'blue', 'LineWidth', 2);

view(45, 45);

hold off;