% 部分拘束typeAの法線ベクトルを逆行列で導出する

syms f1 f2 f3 F Co So l1x l1y l2x l2y l3x l3y

% 行列の定義

A = [0 1 0;
    1 0 1;
    l1x l2y l3x];

inv_A = inv(A);

disp(inv_A);