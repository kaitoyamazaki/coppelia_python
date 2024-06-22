% 別プログラムで計算したモーメントを利用して, 角加速度・角速度を計算する. 理想は偏差も求める

clear;

addpath('.', '-end');
addpath('use_data', '-end');

filepath = 'use_data/object_moment_理想値.mat';

data = load(filepath);
data = data.object_moment;

inertia = 0.00091;
ang_accele_data = [];

for i = 1:size(data,1)
    ang_accele = data(i, 2) / inertia;
    want_data = [data(i, 1) ang_accele];
    ang_accele_data = [ang_accele_data; want_data];
end

ang_vel_data = [];
old_time = ang_accele_data(1, 1);

for i = 1:size(ang_accele_data, 1)
    dtime = ang_accele_data(i, 1) - old_time;
    ang_vel = ang_accele_data(i, 2) * dtime;
    want_data = [ang_accele_data(i, 1) ang_vel];
    ang_vel_data = [ang_vel_data; want_data];
    old_time = ang_accele_data(i, 1);
end

ang_data = [];
old_time = ang_vel_data(1,1);
ang = 0;

for i = 1:size(ang_vel_data, 1)
    dtime = ang_vel_data(i, 1) - old_time;
    dtheta = ang_vel_data(i, 2) * dtime;

    if isnan(dtheta)
        dtheta = 0;
    end

    ang = ang + dtheta;
    want_data = [ang_vel_data(i, 1) ang];
    ang_data = [ang_data; want_data];
    old_time = ang_vel_data(i, 1);
end