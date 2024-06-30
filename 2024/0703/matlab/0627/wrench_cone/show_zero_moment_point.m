% 計算したゼロモーメントのポイントを平面としてプロットする

clear;

addpath('.', '-end');
addpath('function', '-end');

data = load('data/typeA1_モーメントゼロ点.mat');
data2 = load('data/typeA2_モーメントゼロ点.mat');
data3 = load('data/typeB1_モーメントゼロ点.mat');
data4 = load('data/typeB2_モーメントゼロ点.mat');

data = data.data_zero;
data2 = data2.data2_zero;
data3 = data3.data3_zero;
data4 = data4.data4_zero;

[data1x, data1y, data1z] = calc_zero_plane(data);
[data2x, data2y, data2z] = calc_zero_plane(data2);
[data3x, data3y, data3z] = calc_zero_plane(data3);
[data4x, data4y, data4z] = calc_zero_plane(data4);


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

mesh1 = mesh(data1x, data1y, data1z, 'FaceColor', 'b', 'LineStyle', 'none', 'FaceAlpha', 0.25);
mesh2 = mesh(data2x, data2y, data2z, 'FaceColor', 'b', 'LineStyle', 'none', 'FaceAlpha', 0.25);
mesh3 = mesh(data3x, data3y, data3z, 'FaceColor', 'b', 'LineStyle', 'none', 'FaceAlpha', 0.25);
mesh4 = mesh(data4x, data4y, data4z, 'FaceColor', 'b', 'LineStyle', 'none', 'FaceAlpha', 0.25);

hold off;