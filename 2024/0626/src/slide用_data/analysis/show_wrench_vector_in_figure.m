% 部分拘束typeAのwrench coneに関するプログラム
% f3, f1のみから成る平面上を動くベクトルを描画

% 初期化
clear;

% パスの追加
addpath('.', '-end');
addpath('use_data', '-end');
addpath('figure', '-end');

% グラフデータの取得と出力
openfig('figure/wrench_typeA3.fig');

<<<<<<< HEAD
data = load('use_data/object_wrench_110.mat');
=======
data = load('use_data/object_wrench_160.mat');
>>>>>>> 63511d8622d4d4edcbfcdc59cc936c9629402165
data = data.object_wrench;


% 移動平均フィルタの実装
size  = 5;
fx = movmean(data(:,2), size);
fy = movmean(data(:,3), size);
m = movmean(data(:,4), size);

data = [data(:,1) fx fy m];

data(isnan(data)) = 0;

% 行列の行数を取得
numRows = 1000;
%view(210, 20);
view(310, 44);

hold on;


pause(5);

for i = 1:numRows
    p = plot3([0, data(i,2)*10], [0, data(i,3)*10], [0,data(i,4)*10], 'Color', [1.0, 0.33, 0.65], 'LineWidth', 4.0);

    pause(0.05);
    delete(p);
end

hold off;