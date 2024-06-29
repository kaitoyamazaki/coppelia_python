% 計算した角度データの最大値と最小値を表示

clear;

addpath('.', '-end');
addpath('data', '-end');

theta1 = load('data/typeA1_theta.mat');
theta2 = load('data/typeA2_theta.mat');
theta3 = load('data/typeB1_theta.mat');
theta4 = load('data/typeB2_theta.mat');

theta1 = theta1.theta1;
theta2 = theta2.theta2;
theta3 = theta3.theta3;
theta4 = theta4.theta4;

theta1(1) = [];
theta2(1) = [];
theta3(1) = [];
theta4(1) = [];

% 最大値の表示
max1 = max(theta1);
max2 = max(theta2);
max3 = max(theta3);
max4 = max(theta4);

% 最小値の表示
min1 = min(theta1);
min2 = min(theta2);
min3 = min(theta3);
min4 = min(theta4);

% 小さい順にソート
theta1 = sort(theta1);
theta2 = sort(theta2);
theta3 = sort(theta3);
theta4 = sort(theta4);