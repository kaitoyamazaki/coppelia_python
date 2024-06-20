% ランダムに取得した点の距離をチェックするプログラム
% 一番近いものを探す

clear;

addpath('.', '-end');
addpath('data', '-end');

load('data/random_point.mat', 'random_point');

initial_pos = [random_point(1,1) random_point(1,2) random_point(1,3)];

x = random_point(:, 1) - initial_pos(1);
y = random_point(:, 2) - initial_pos(2);
z = random_point(:, 3) - initial_pos(3);

direction = x.^2 + y.^2 + z.^2;