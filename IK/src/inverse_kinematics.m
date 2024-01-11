syms l2 l3 l4 c2 s2 c23 s23 c234 s234

kinematics = [-l2*s2-l3*s23-l4*s234 -l3*s23-l4*s234 -l4 *s234;
              l2*c23+l3*c23+l4*c234 l3*c23+l4*c234 l4*c234;
              1 1 1];

IK = inv(kinematics);

disp(IK)