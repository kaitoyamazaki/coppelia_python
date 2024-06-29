% wrench coneを計算して表示するプログラムを作成

clear;

addpath('.', '-end');
addpath('function', '-end');


% 法線ベクトルの定義

f1 = [-1; 0; 0];
f2 = [1; 0; 0];
f3 = [0; 1; 0];

% 位置ベクトルの定義
l1 = [5.0; 14.271; 0];
l2 = [-5.0; 27.5; 0];
l3 = [-7.5; 30.0; 0];

% 位置ベクトルの単位をmに変換する
l1 = l1 / 1000;
l2 = l2 / 1000;
l3 = l3 / 1000;

% レンチベクトルの集合をそれぞれ定義
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

    % 現在のレンチベクトルを計算
    wrench1 = [edit_f1(1) edit_f1(2) now_moment1(3)];
    wrench2 = [edit_f2(1) edit_f2(2) now_moment2(3)];
    wrench3 = [edit_f3(1) edit_f3(2) now_moment3(3)];

    m1 = [m1; wrench1];
    m2 = [m2; wrench2];
    m3 = [m3; wrench3];
end

% mesh()関数を利用するためのデータを取得する計算を下記で実行
[pointx1, pointy1, pointz1] = calc_plane(m1(end, :), m2(end, :));
[pointx2, pointy2, pointz2] = calc_plane(m2(end, :), m3(end, :));
[pointx3, pointy3, pointz3] = calc_plane(m3(end, :), m1(end, :));

% グラフ描画開始

figure;

hold on;
grid on;

%グラフの範囲を設定
xlim([-1, 1]);
ylim([-1, 1]);
zlim([-0.03, 0.03]);

%ラベルの描画
xlabel('fx  [N]', 'FontSize', 10.5, 'FontWeight', 'bold', 'Color', 'r');
ylabel('fy  [N]', 'FontSize', 10.5, 'FontWeight', 'bold', 'Color', 'g');
zlabel('ω  [Nm]', 'FontSize', 10.5, 'FontWeight', 'bold', 'Color', 'b');

% レンチベクトルを描画
plot3(m1(:,1), m1(:,2), m1(:,3), 'Color', 'k', 'LineWidth', 1.5);
plot3(m2(:,1), m2(:,2), m2(:,3), 'Color', 'k', 'LineWidth', 1.5);
plot3(m3(:,1), m3(:,2), m3(:,3), 'Color', 'k', 'LineWidth', 1.5);

% レンチベクトルから成る平面を作成
mesh1 = mesh(pointx1, pointy1, pointz1, 'FaceColor', 'b', 'LineStyle', 'none', 'FaceAlpha', 0.25);
mesh2 = mesh(pointx2, pointy2, pointz2, 'FaceColor', 'b', 'LineStyle', 'none', 'FaceAlpha', 0.25);
mesh3 = mesh(pointx3, pointy3, pointz3, 'FaceColor', 'b', 'LineStyle', 'none', 'FaceAlpha', 0.25);

plot_not_wrench_edge(m1(end, :), m2(end, :), m3(end, :));

% グラフタイトル
title('typeA in Wrench Space');

% 軸線を描画
line([min(xlim) max(xlim)], [0 0], [0 0], 'Color', 'red', 'LineWidth', 1.0);
line([0 0], [min(ylim), max(ylim)], [0 0], 'Color', 'green', 'LineWidth', 1.0);
line([0 0], [0 0], [min(zlim) max(zlim)], 'Color', 'blue', 'LineWidth', 1.0);

hold off;