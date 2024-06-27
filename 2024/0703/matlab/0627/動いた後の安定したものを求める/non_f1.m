
% 回転がないことを前提にして角度だけを解く

clear;

addpath('.', '-end');

% パラメータの設定
mu = 0.80;
m = 0.01484;
g = 9.81;

friction = mu * m * g;

save_data = zeros(10000, 2);

% 距離に関するパラメータの設定

l1x = 0.02;
l2y = 0.0025;
lgx = 0.0125;
lgy = -0.03;
M = 0.000;
i = 1;

for deg = 270:1:360
    rad = deg2rad(deg);
    fgx = friction * cos(rad);
    fgy = friction * sin(rad);

    f2 = -1 * fgx;
    moment_middle = -l2y*f2 + lgx*fgy-lgy*fgx;

    data = [deg moment_middle];
    save_data(i, :) = data;
    i = i+1;
end