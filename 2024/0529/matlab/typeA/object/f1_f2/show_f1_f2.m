% 部分拘束typeAにおけるプログラム
% 法線ベクトルf1, f2を表示する

% 初期化
clear;

% パスを追加
addpath('.', '-end');
addpath('function', '-end');
addpath('../data', '-end');

openfig('../data/object_typeA.fig');

hold on;

% 法線ベクトルの定義
f1 = 1;
f2 = 0;
f3 = 0;

% 法線ベクトルの位置ベクトルの定義
l1 = [0.0075; 0.03; 0.0];
l2 = [0.005; 0.0275; 0.0];
l3 = [-0.0125; 0.03; 0.0];

load('../data/f1_data_f12.mat');
load('../data/f2_data_f12.mat');
load('../data/wrench_f12.mat');

f1_x = 7.5;
f1_y = 30.0;

f2_x = 5.0;
f2_y = 27.5;

cop_x = -2.5;
cop_y = 27.5;

for i = 1:1:101

    x1 = wrench1(i, 1) * 10;
    y1 = wrench1(i, 2) * 10;

    x2 = wrench2(i, 1) * 10;
    y2 = wrench2(i, 2) * 10;

    x = wrench(i, 1) * 10;
    y = wrench(i, 2) * 10;

    h1 = quiver(f1_x, f1_y, x1, y1, 'Color', [1.0, 1.0, 0.0], 'LineWidth', 2.0, 'AutoScale', 'off');
    h2 = quiver(f2_x, f2_y, x2, y2, 'Color', [1.0, 0.65, 0.0], 'LineWidth', 2.0, 'AutoScale', 'off');
    h3 = quiver(cop_x, cop_y, x, y, 'Color', 'k', 'LineWidth', 2.0, 'AutoScale', 'off');

    pause(0.1);

    if(i == 101)
        disp('');
    else
        delete(h1);
        delete(h2);
        delete(h3);
    end
end

hold off;