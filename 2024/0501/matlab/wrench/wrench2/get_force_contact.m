% wrenchで導出した領域を基に最大角度と最小角度を導出するプログラム

clear;

addpath('.', '-end');
addpath('function', '-end');

% 力の成分
f1 = [0;1;0];
f2 = [-1;0;0];
f3 = [0;1;0];

% 位置ベクトル
l1 = [0.008; 0.003; 0.0];
l2 = [0.006; 0.027; 0.0];
l3 = [-0.012; 0.030; 0.0];

m1 = [];
m2 = [];
m3 = [];

for i = 0:1
    edit_f1 = i * f1;
    edit_f2 = i * f2;
    edit_f3 = i * f3;

    now_moment1 = cross(l1, edit_f1);
    now_moment2 = cross(l2, edit_f2);
    now_moment3 = cross(l3, edit_f3);

    wrench_f1 = [edit_f1(1) edit_f1(2) now_moment1(3)];
    wrench_f2 = [edit_f2(1) edit_f2(2) now_moment2(3)];
    wrench_f3 = [edit_f3(1) edit_f3(2) now_moment3(3)];

    m1 = [m1; wrench_f1];
    m2 = [m2; wrench_f2];
    m3 = [m3; wrench_f3];
end

moment_point1 = m1(end, :);
moment_point2 = m2(end, :);
moment_point3 = m3(end, :);

plane_coeff1 = cross(moment_point1, moment_point2);
plane_coeff2 = cross(moment_point2, moment_point3);
plane_coeff3 = cross(moment_point3, moment_point1);

points = get_angles(plane_coeff1, plane_coeff2, plane_coeff3);

angles = calc_angles(points);

maxValue = max(angles(:));

minValue = min(angles(:));

% 結果を表示
%disp(['The maximum value is: ', num2str(maxValue)]);
%disp(['The minimum value is: ', num2str(minValue)]);

disp(maxValue);
disp(minValue);