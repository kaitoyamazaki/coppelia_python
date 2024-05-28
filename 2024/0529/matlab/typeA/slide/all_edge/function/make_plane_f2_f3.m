% ２つのエッジで作成する面

function [wrench_x, wrench_y, wrench_z] = make_plane_f2_f3(l1, l2, l3);

    wrench_pos = [];

    f1 = 0;
    f2 = 1;
    f3 = 1;

    for i = 0:0.01:1
        for j = 0:0.01:1
            if(i+j < 1)
                A = [0 -1 0;
                    1 0 1;
                    l1(1) l2(2) l3(1)];

                edit_f1 = i * f1;
                edit_f2 = i * f2;
                edit_f3 = j * f3;

                all_f1 = [edit_f1; 0; 0];
                all_f2 = [0; edit_f2; 0];
                all_f3 = [0; 0; edit_f3];

                ans_f1 = A * all_f1;
                ans_f2 = A * all_f2;
                ans_f3 = A * all_f3;

                wrench1 = [ans_f1(1) ans_f1(2) ans_f1(3)];
                wrench2 = [ans_f2(1) ans_f2(2) ans_f2(3)];
                wrench3 = [ans_f3(1) ans_f3(2) ans_f3(3)];

                wrench = wrench1 + wrench2 + wrench3;
                wrench_pos = [wrench_pos; wrench];
            end
        end
    end

    remainder = rem(size(wrench_pos, 1), 5);

    wrench_x = reshape(wrench_pos(1:size(wrench_pos, 1) - remainder, 1), [], 5);
    wrench_y = reshape(wrench_pos(1:size(wrench_pos, 1) - remainder, 2), [], 5);
    wrench_z = reshape(wrench_pos(1:size(wrench_pos, 1) - remainder, 3), [], 5);

end