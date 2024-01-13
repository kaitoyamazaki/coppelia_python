joint_deg = [0.0 65.0 -145.0 80];
joint = deg2rad(joint_deg);
l1 = 0.13156;
l2 = 0.1104;
l3 = 0.096;
l4 = 0.07318;

p = [sin(joint(1))*(l2*sin(joint(2)) + l3*sin(joint(2) + joint(3)) + l4*sin(joint(2) + joint(3) + joint(4)));
     -cos(joint(1))*(l2*sin(joint(2)) + l3*sin(joint(2) + joint(3)) + l4*sin(joint(2) + joint(3) + joint(4)))
     l1 + l2*cos(joint(2)) + l3*cos(joint(2) + joint(3) + l4*cos(joint(2) + joint(3) + joint(3)));
     joint(2) + joint(3) + joint(4)];

%disp(p)

p2 = [cos(joint(1)) * (l2 * cos(joint(2)) + l3 * cos(joint(2) + joint(3)) + l4 * cos(joint(2) + joint(3) + joint(4)));
      sin(joint(1)) * (l2 * cos(joint(2)) + l3 * cos(joint(2) + joint(3)) + l4 * cos(joint(2) + joint(3) + joint(4)));
      l2 * sin(joint(2)) + l3 * sin(joint(2) + joint(3)) + l4 * sin(joint(2) + joint(3) + joint(4)) + l4;
      joint(2) + joint(3) + joint(4)];

disp(p2)