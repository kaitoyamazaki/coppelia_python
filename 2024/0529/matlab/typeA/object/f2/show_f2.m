% 部分拘束typeAにおけるプログラム
% 法線ベクトルf1のみを表示する

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

load('../data/f2_data.mat');

f2_x = 5.0;
f2_y = 27.5;

for i = 1:1:101

    x = wrench2(i, 1) * 10;
    y = wrench2(i, 2) * 10;

    h1 = quiver(f2_x, f2_y, x, y, 'Color', [1.0, 0.65, 0.0], 'LineWidth', 2.0, 'AutoScale', 'off');

    pause(0.1);

    if(i == 101)
        disp('');
    else
        delete(h1)
    end
end

hold off;