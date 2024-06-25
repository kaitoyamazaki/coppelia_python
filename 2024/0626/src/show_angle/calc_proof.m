% 計算の証明用

clear;

mu = 0.8;
m = 0.01484;
g = 9.81;

friction = mu * m * g;

theta = 150;
theta_rad = deg2rad(theta);

F = [friction*cos(theta_rad) friction*sin(theta_rad) 0];

f2 = friction * cos(theta_rad);

l1 = [0.0075 0.0300 0.0];
l2 = [0.005 0.0275 0.0];
l3 = [-0.0125, 0.0300, 0.0];

f2_e = [f2 0 0];
f2_m = cross(l2, f2_e);

f2_m = f2_m(3);

f1_and_f3 = F(2);