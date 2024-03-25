addpath('../../..', '-end');

l1 = 0.13156;
l2 = 0.1104;
l3 = 0.096;
l4 = 0.07318;

j1 = -30;
j2 = 40;
j3 = 90;
j4 = -65;

j1 = deg2rad(j1);
j2 = deg2rad(j2);
j3 = deg2rad(j3);
j4 = deg2rad(j4);

x = -sin(j1) * (l2 * sin(j2) + l3 * sin(j2+j3) + l4 * sin(j2+j3+j4));
y = cos(j1) * (l2 * sin(j2) + l3 * sin(j2+j3) + l4 * sin(j2+j3+j4));
z = l1 + l2 * cos(j2) + l3 * cos(j2+j3) + l4 * cos(j2+j3+j4);
z = z + 0.017;
theta = j2 + j3 + j4;
theta = rad2deg(theta);