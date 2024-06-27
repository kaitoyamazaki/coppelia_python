% モーメントを利用してf1の値を計算するプログラム

clear;

addpath('.', '-end');

% パラメータの設定
mu = 0.80;
m = 0.01484;
g = 9.81;

friction = mu * m * g;
M = 0.01;

% 距離に関するパラメータの設定

l2y = 0.0025;
lgx = 0.0125;
lgy = -0.03;
l1x = 0.02;

% 角度を入力すること
deg = 90;
rad = deg2rad(deg);

fgx = friction * cos(rad);
fgy = friction * sin(rad);

f2 = -1 * fgx;

moment_middle = -l2y*f2 + lgx*fgy-lgy*fgx;

f1_moment = M - moment_middle;
f1 = f1_moment / l1x;