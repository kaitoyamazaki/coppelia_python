% 事前に計算したデータからモーメントがゼロになる点データを計算する

clear;

addpath('.', '-end');
addpath('data', '-end');
addpath('function', '-end');

data = load('data/typeA3_レンチベクトルのデータ.mat');
data2 = load('data/typeA4_レンチベクトルのデータ.mat');
data3 = load('data/typeB3_レンチベクトルのデータ.mat');
data4 = load('data/typeB4_レンチベクトルのデータ.mat');

data = data.wrench_point;
data2 = data2.wrench_point;
data3 = data3.wrench_point;
data4 = data4.wrench_point;

rows = size(data,1);
data_zero = zeros(rows, 3);
data2_zero = zeros(rows, 3);
data3_zero = zeros(rows, 3);
data4_zero = zeros(rows, 3);

count = 1;

for i = 1:size(data, 1)
    if(data(i, 3) == 0)
        data_zero(count, :) = data(i, :);
        count = count + 1;
    end
end

count = 1;

for i = 1:size(data2, 1)
    if(data2(i, 3) == 0)
        data2_zero(count, :) = data2(i, :);
        count = count + 1;
    end
end

count = 1;

for i = 1:size(data3, 1)
    if(data3(i, 3) >  0)
        data3_zero(count, :) = data3(i, :);
        count = count + 1;
    end
end

count = 1;

for i = 1:size(data4, 1)
    if(data4(i, 3) <  0)
        data4_zero(count, :) = data4(i, :);
        count = count + 1;
    end
end

data_zero(all(data_zero == 0, 2), :) = [];
data2_zero(all(data2_zero == 0, 2), :) = [];
data3_zero(all(data3_zero == 0, 2), :) = [];
data4_zero(all(data4_zero == 0, 2), :) = [];