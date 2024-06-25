% シミュレーションで取得したデータを解析するプログラム
% 具体的には, 位置座標の偏差から, 速度の方向, モーメントを計算する

clear;

addpath('.', '-end');
addpath('../data', '-end');

%filepath = '../data/90度方向_並進.csv';
%filepath = '../data/100度方向_並進.csv';
%filepath = '../data/110度方向_並進.csv';
%filepath = '../data/120度方向_並進.csv';
%filepath = '../data/130度方向_並進.csv';
%filepath = '../data/140度方向_並進.csv';
filepath = '../data/150度方向_並進.csv';
%filepath = '../data/160度方向_並進.csv';
%filepath = '../data/170度方向_並進.csv';
%filepath = '../data/180度方向_並進.csv';
data = readmatrix(filepath);

old_data = data(1, :);

% 偏差に関する処理
dp_row = [];

for i = 1:size(data,1)
    dp = data(i, :) - old_data;
    dp_row = [dp_row; dp];

    old_data = data(i, :);
end

% 速度に関する処理
velocity_row = [];

for i = 1:size(dp_row,1)
    dtime = dp_row(i, 1);
    v = [dp_row(i, 2)/dtime dp_row(i, 3)/dtime];
    velocity_row = [velocity_row; v];
end

direction_row = [];

for i=1:size(velocity_row,1)
    time = data(i, 1);
    theta = atan2(velocity_row(i,2), velocity_row(i,1));
    theta_data = [time theta];
    direction_row = [direction_row; theta_data];
end

mu = 0.80;
m = 0.01484;
g = 9.81;

friction = mu * m * g;
object_wrench = [];

for i = 1:size(direction_row,1)
    friction_x = friction * cos(direction_row(i, 2));
    friction_y = friction * sin(direction_row(i, 2));
    friction_vector = [friction_x friction_y 0];
    pos_vector = [data(i,4) data(i,5) 0];
    moment = cross(pos_vector, friction_vector);
    want_data = [direction_row(i,1) friction_vector(1) friction_vector(2) moment(3)];
    object_wrench = [object_wrench; want_data];
    %object_moment = [object_moment; want_data];
end

%save_filepath = 'use_data/object_wrench_90.mat';
%save_filepath = 'use_data/object_wrench_100.mat';
%save_filepath = 'use_data/object_wrench_110.mat';
%save_filepath = 'use_data/object_wrench_120.mat';
%save_filepath = 'use_data/object_wrench_130.mat';
%save_filepath = 'use_data/object_wrench_140.mat';
%save_filepath = 'use_data/object_wrench_150.mat';
%save_filepath = 'use_data/object_wrench_160.mat';
%save_filepath = 'use_data/object_wrench_170.mat';
%save_filepath = 'use_data/object_wrench_180.mat';
%save(save_filepath, 'object_wrench');