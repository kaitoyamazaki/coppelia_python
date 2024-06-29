% 事前に計算したデータからモーメントがゼロになる点データを計算する

clear;

addpath('.', '-end');
addpath('data', '-end');

data = load('data/typeA1_レンチベクトルのデータ.mat');
data2 = load('data/typeA2_レンチベクトルのデータ.mat');
data3 = load('data/typeB1_レンチベクトルのデータ.mat');
data4 = load('data/typeB2_レンチベクトルのデータ.mat');

data = data.wrench_point;
data2 = data2.wrench_point;
data3 = data3.wrench_point;
data4 = data4.wrench_point;


data_zero = [];
data2_zero = [];
data3_zero = [];
data4_zero = [];

for i = 1:size(data, 1)
    if(data(i, 3) == 0)
        data_zero = [data_zero; data(i, :)];
    end
end

for i = 1:size(data2, 1)
    if(data2(i, 3) == 0)
        data2_zero = [data2_zero; data2(i, :)];
    end
end

for i = 1:size(data3, 1)
    if(data3(i, 3) == 0)
        data3_zero = [data3_zero; data3(i, :)];
    end
end

for i = 1:size(data4, 1)
    if(data4(i, 3) == 0)
        data4_zero = [data4_zero; data4(i, :)];
    end
end