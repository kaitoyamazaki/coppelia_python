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
%data = load('use_data/object_wrench.mat');
%data = load('use_data/object_wrench_1680.mat');
%data = load('use_data/object_wrench_2680.mat');

%data = load('use_data/object_wrench_base_cog.mat');
%data = load('use_data/object_wrench_base_cog_1680.mat');
data = load('use_data/object_wrench_base_cog_2680.mat');
data = data.object_wrench;

hold on;

pause(5);

for i = 1:size(data, 1)
    p = plot3([0, data(i,2)*10], [0, data(i,3)*10], [0,data(i,4)*10], 'Color', [1.0, 0.33, 0.65], 'LineWidth', 4.0);

    pause(0.05);
    delete(p);
end

hold off;