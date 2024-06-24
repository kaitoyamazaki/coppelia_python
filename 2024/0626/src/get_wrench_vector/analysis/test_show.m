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
data = load('use_data/object_wrench_3080.mat');
data = data.object_wrench;

% 移動平均フィルタの実装
size  = 5;
fx = movmean(data(:,2), size);
fy = movmean(data(:,3), size);
m = movmean(data(:,4), size);

after_data = [data(:,1) fx fy m];

% NaNを0に置き換え
after_data(isnan(after_data)) = 0;

% 行列の行数を取得
numRows = size(after_data, 1);

% 行数を表示
disp(numRows);