% ランダムに3次元空間上にある点を導出する関数
function [x, y, z] = search_coordinate()
    x = 2 * rand - 1;
    y = 2 * rand - 1;
    z = 0.06 * rand - 0.03;
end