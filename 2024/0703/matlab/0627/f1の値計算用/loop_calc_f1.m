% f1計算のプログラムを作成する

clear;

addpath('.', '-end');

% パラメータの設定
mu = 0.80;
m = 0.01484;
g = 9.81;

friction = mu * m * g;

save_data = zeros(10000, 3);

% 距離に関するパラメータの設定

l2y = 0.0025;
lgx = 0.0125;
lgy = -0.03;
l1x = 0.02;

% 角度を入力すること
deg = 180 + 180;
rad = deg2rad(deg);

fgx = friction * cos(rad);
fgy = friction * sin(rad);

f2 = -1 * fgx;

moment_middle = -l2y*f2 + lgx*fgy-lgy*fgx;
i = 1;

for M = -0.03:0.001:0.03
    f1_moment = M - moment_middle;
    f1 = f1_moment / l1x;
    f3 = f1 + fgy;

    data = [M f1 f3];
    save_data(i, :) = data;
    i = i+1;
end