syms l1 l2 c_1 s_1 c_12 s_12

kinematics = [-l1*s_1 - l2*s_12 -l2*s_12;
              l1*c_1 + l2*c_12 l2*c_12];

IK = det(kinematics);

disp(IK)