% モーメントから角加速度, 姿勢の変化を計算する


clear;

moment = 0.0026;
mu = 0.80;
m = 0.01484;
g = 9.81;
inertia = 0.00091;

full_time = 10;
time = 0.0;
interval_time = 0.05;

num = full_time / interval_time;

theta_row = zeros(num,2);
row = size(theta_row, 1);

friction = mu * m * g;

ddtheta = moment / inertia;


old_time = 0.0;
old_theta = 0.0;

for i = 1:row
    local_time = time - old_time;
    dtheta = ddtheta * local_time;
    theta = dtheta * local_time + old_theta;

    theta_row(i, :) = [time theta];

    old_theta = theta;
    old_time = time;
    time = time + 0.05;
end

disp(rad2deg(theta_row(end, 2)));