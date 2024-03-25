% xとyの値を導出する(進行方向の角度を指定する時）

addpath('../../..', '-end');

theta_deg = 70;
theta = deg2rad(theta_deg);
length = 0.001;

x = length * cos(theta);
y = length * sin(theta);