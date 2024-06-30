% 事前に計算した拘束を維持可能である点群データをもとに平面を作成する.

clear;

addpath('.', '-end');
addpath('function', '-end');
addpath('data', '-end');

data1 = load('data/typeA1_モーメントゼロ点.mat');
data2 = load('data/typeA2_モーメントゼロ点.mat');
data3 = load('data/typeA3_モーメントゼロ点.mat');
data4 = load('data/typeA4_モーメントゼロ点.mat');
data5 = load('data/typeB1_モーメントゼロ点.mat');
data6 = load('data/typeB2_モーメントゼロ点.mat');
data7 = load('data/typeB3_モーメントゼロ点.mat');
data8 = load('data/typeB4_モーメントゼロ点.mat');

data1 = data1.data_zero;
data2 = data2.data2_zero;
data3 = data3.data_zero;
data4 = data4.data2_zero;

data5 = data5.data3_zero;
data6 = data6.data4_zero;
data7 = data7.data3_zero;
data8 = data8.data4_zero;

[data1x, data1y, data1z] = transform_data(data1);
[data2x, data2y, data2z] = transform_data(data2);
[data3x, data3y, data3z] = transform_data(data3);
[data4x, data4y, data4z] = transform_data(data4);
[data5x, data5y, data5z] = transform_data(data5);
[data6x, data6y, data6z] = transform_data(data6);
[data7x, data7y, data7z] = transform_data(data7);
[data8x, data8y, data8z] = transform_data(data8);

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

mesh1 = mesh(data1x, data1y, data1z, 'FaceColor', [0 0 139/255], 'LineStyle', 'none', 'FaceAlpha', 0.45);
mesh2 = mesh(data2x, data2y, data2z, 'FaceColor', [0 0 255/255], 'LineStyle', 'none', 'FaceAlpha', 0.45);
mesh3 = mesh(data3x, data3y, data3z, 'FaceColor', [135/255 206/255 235/255], 'LineStyle', 'none', 'FaceAlpha', 0.45);
mesh4 = mesh(data4x, data4y, data4z, 'FaceColor', [176/255 224/255 230/255], 'LineStyle', 'none', 'FaceAlpha', 0.45);

mesh5 = mesh(data5x, data5y, data5z, 'FaceColor', [0 100/255 0], 'LineStyle', 'none', 'FaceAlpha', 0.45);
mesh6 = mesh(data6x, data6y, data6z, 'FaceColor', [0 128/255 0], 'LineStyle', 'none', 'FaceAlpha', 0.45);
mesh7 = mesh(data7x, data7y, data7z, 'FaceColor', [144/255 238/255 144/255], 'LineStyle', 'none', 'FaceAlpha', 0.45);
mesh8 = mesh(data8x, data8y, data8z, 'FaceColor', [173/255 255/255 47/255], 'LineStyle', 'none', 'FaceAlpha', 0.45);

hold off;