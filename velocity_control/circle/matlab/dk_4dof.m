theta_deg = [-90.0, 60.0 -140.0 80.0];
theta = deg2rad(theta_deg);

j1 = theta(1);
j2 = theta(2);
j3 = theta(3);
j4 = theta(4);

l1 = 0.131;
l2 = 0.110;
l3 = 0.096;
l4 = 0.073;

pe = [-sin(j1) * (l2*cos(j2) + l3 * cos(j2 + j3) + l4 * cos(j2 + j3 + j4));
      cos(j1) * (l2 * cos(j2) + l3 * cos(j2 + j3) + l4 * cos(j2 + j3 + j4));
      l1 + l2 * sin(j2) + l3 * sin(j2 + j3) + l4 * sin(j2 + j3 + j4);
      j2 + j3 + j4];

disp(pe);