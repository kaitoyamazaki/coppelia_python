clear;

syms l1 l2 l3 l4 c1 s1 c2 s2 c23 s23 c234 s234;

kinematics = [c1*(l2*s2+l3*s23+l4*s234) s1*(l2*c2+l3*c23+l4*c234) s1*(l3*c23+l4*c234) l4*s1*c234;
              s1*(l2*s2+l3*s23+l4*s234) -c1*(l2*c2+l3*c23+l4*c234) -c1*(l3*c23+l4*c234) -l4*c1*c234;
              0 -(l2*s2+l3*s23+l4*s234) -(l3*s23+l4*s234) -l4*s234;
              0 1 1 1];

%disp(kinematics)

IK = inv(kinematics);

disp(IK);


% リンクのパラメータ
l1 = 0.132;
l2 = 0.110;
l3 = 0.096;
l4 = 0.073;


% 現在のロボットアームの各ジョイント(度数法)
theta1 = 0;
theta2 = 65;
theta3 = -145;
theta4 = 80;

% 現在のロボットアームの各ジョイント(弧度法)
theta1_rad = deg2rad(theta1);
theta2_rad = deg2rad(theta2);
theta3_rad = deg2rad(theta3);
theta4_rad = deg2rad(theta4);

% ヤコビ行列導出に使う三角関数

c1 = cos(theta1_rad);
s1 = sin(theta1_rad);
c2 = cos(theta2_rad);
s2 = sin(theta2_rad);
c23 = cos(theta2_rad + theta3_rad);
s23 = sin(theta2_rad + theta3_rad);
c234 = cos(theta2_rad + theta3_rad + theta4_rad);
s234 = sin(theta2_rad + theta3_rad + theta4_rad);

theta_i = [theta1 theta2 theta3 theta4];

pos1 = [0.167 -0.013 0.049 -90];
pos2 = [0.167040840701809 -0.0129999871695147 0.049 -90];
dp = pos2 - pos1;
dp = dp.';
 
yakobi = [c1*(l2*s2+l3*s23+l4*s234) s1*(l2*c2+l3*c23+l4*c234) s1*(l3*c23+l4*c234) l4*s1*c234;
          s1*(l2*s2+l3*s23+l4*s234) -c1*(l2*c2+l3*c23+l4*c234) -c1*(l3*c23+l4*c234) -l4*c1*c234;
          0 -(l2*s2+l3*s23+l4*s234) -(l3*s23+l4*s234) -l4*s234;
          0 1 1 1];

yakobi_inv = inv(yakobi);

delta_theta = yakobi_inv * dp;

delta_theta_deg = rad2deg(delta_theta);

theta_i1 = theta_i + delta_theta_deg.';
disp(theta_i1)
theta_i1(1) = theta_i1(1) * -1
theta_i1_rad = deg2rad(theta_i1);

% ヤコビ行列導出に使う三角関数

c1_i1 = cos(theta_i1_rad(1));
s1_i1 = sin(theta_i1_rad(1));
c2_i1 = cos(theta_i1_rad(2));
s2_i1 = sin(theta_i1_rad(2));
c23_i1 = cos(theta_i1_rad(2) + theta_i1_rad(3));
s23_i1 = sin(theta_i1_rad(2) + theta_i1_rad(3));
c234_i1 = cos(theta_i1_rad(2) + theta_i1_rad(3) + theta_i1_rad(4));
s234_i1 = sin(theta_i1_rad(2) + theta_i1_rad(3) + theta_i1_rad(4));

pos2 = [s1_i1*(l2*s2_i1 + l3*s23_i1 + l4*s234_i1);
       -c1_i1*(l2*s2_i1 + l3*s23_i1 + l4*s234_i1);
       l1 + l2*c2_i1 + l3*c23_i1 + l4*c234_i1
       theta_i1(2) + theta_i1(3) + theta_i1(4)];

pos2 = pos2.';

disp(pos2);