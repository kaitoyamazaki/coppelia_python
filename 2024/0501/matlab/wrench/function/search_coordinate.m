% ランダムに3次元空間上にある点を導出する関数
function [x, y, z] = search_coordinate()
    x = 1 * rand - 0.5;
    y = 1 * rand - 0.5;
    z = 0.03 * rand - 0.015;
end