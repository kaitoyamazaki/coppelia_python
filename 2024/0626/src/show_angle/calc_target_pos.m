% 毎回計算するのが面倒なので, 配列を作成して、シミュレーションをするときの基準にする
% typeA用のもの, typeBBはまた別で考える

base_theta = 90;
distance = 0.05;

direction_row = zeros(10, 3);

for i = 0:9
    theta = i*10 + base_theta; 
    theta_rad = deg2rad(theta);
    dx = distance * cos(theta_rad);
    dy = distance * sin(theta_rad);
    want_data = [theta dx dy];
    direction_row(i+1, :) = want_data;
end