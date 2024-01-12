syms l1 l2 l3 l4 c1 s1 c2 s2 c23 s23 c234 s234

kinematics = [c1*(l2*s2+l3*s23+l4*s234) s1*(l2*c2+l3*c23+l4*c234) s1*(l3*c23+l4*c234) l4*s1*c234;
              s1*(l2*s2+l3*s23+l4*s234) -c1*(l2*c2+l3*c23+l4*c234) -c1*(l3*c23+l4*c234) -l4*c1*c234;
              0 -(l2*s2+l3*s23+l4*s234) -(l3*s23+l4*s234) -l4*s234;
              0 1 1 1];

%disp(kinematics)

IK = inv(kinematics);

disp(IK)