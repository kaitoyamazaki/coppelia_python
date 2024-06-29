% 取得したゼロモーメントポイントから角度を計算する

clear;

data = load('data/typeA1_モーメントゼロ点.mat');
data2 = load('data/typeA2_モーメントゼロ点.mat');
data3 = load('data/typeB1_モーメントゼロ点.mat');
data4 = load('data/typeB2_モーメントゼロ点.mat');

data = data.data_zero;
data2 = data2.data2_zero;
data3 = data3.data3_zero;
data4 = data4.data4_zero;

row = size(data,1);
row2 = size(data2,1);
row3 = size(data3,1);
row4 = size(data4,1);

theta1 = zeros(row, 1);
theta2 = zeros(row2, 1);
theta3 = zeros(row3, 1);
theta4 = zeros(row4, 1);

for i = 1:row
    theta = atan2(data(i,2), data(i,1));
    theta = rad2deg(theta);
    theta1(i, 1) = theta;
end

for i = 1:row2
    theta = atan2(data2(i,2), data2(i,1));
    theta = rad2deg(theta);
    theta2(i, 1) = theta;
end

for i = 1:row3
    theta = atan2(data3(i,2), data3(i,1));
    theta = rad2deg(theta);
    theta3(i, 1) = theta;
end

for i = 1:row4
    theta = atan2(data4(i,2), data4(i,1));
    theta = rad2deg(theta);
    theta4(i, 1) = theta;
end
