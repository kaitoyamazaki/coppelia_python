% 部分拘束typeBのレンチコーンを導出する
% 一旦計算する


clear;

addpath('.', '-end');

% 力の成分
f1 = 1;
f2 = 1;
f3 = 1;

% 位置ベクトルの設定
l1 = [0.0075 0.03 0.0];
l2 = [0.005 0.027 0.0];
l3 = [-0.005 0.012 0.0];

% wrenchベクトルを格納する箇所
m1 = [];
m2 = [];
m3 = [];

% wrenchベクトルを計算

for i = 0:1
    edit_f1 = i * f1;
    edit_f2 = i * f2;
    edit_f3 = i * f3;

    now_moment = cross
end