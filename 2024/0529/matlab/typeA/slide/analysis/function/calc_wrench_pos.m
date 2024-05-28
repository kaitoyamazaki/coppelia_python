% 関数(後で記述する)

function [wrench] = calc_wrench_pos(l1, l2, l3)
    f1 = 1;
    f2 = 1;
    f3 = 1;

    wrench = [];

    for i = 0:0.00001:1
        for j = 0:0.00001:1

            s = i;
            t = j;
            u = 1 - s - t;

            if(0 <= s && s <= 1 && 0 <= t & t <= 1 && 0 <= u && u <= 1)

                A = [0 -1 0;
                1 0 1;
                l1(1) l2(2) l3(1)];

                edit_f1 = s * f1;
                edit_f2 = t * f2;
                edit_f3 = u * f3;

                all_f1 = [edit_f1; 0; 0];
                all_f2 = [0; edit_f2; 0];
                all_f3 = [0; 0; edit_f3];

                ans_f1 = A * all_f1;
                ans_f2 = A * all_f2;
                ans_f3 = A * all_f3;

                wrench1 = [ans_f1(1) ans_f1(2) ans_f1(3)];
                wrench2 = [ans_f2(1) ans_f2(2) ans_f2(3)];
                wrench3 = [ans_f3(1) ans_f3(2) ans_f3(3)];

                all_wrench = wrench1 + wrench2 + wrench3;

                if(all_wrench(3) == 0)
                    wrench = [wrench; all_wrench];
                end

            end
        end
    end
end