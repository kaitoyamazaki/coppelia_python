joint_deg = [90 -30 -90];
joint = deg2rad(joint_deg);
link = [0 0.4 0.2];

p = [-(link(2)*cos(joint(1))*sin(joint(2)) + link(3)*cos(joint(1))*sin(joint(2)+joint(3)));
     -(link(2)*sin(joint(1))*sin(joint(2)) + link(3)*sin(joint(1))*sin(joint(2)+joint(3)));
     link(1) + link(2)*cos(joint(2)) + link(3)*cos(joint(2) + joint(3))];

disp(p);