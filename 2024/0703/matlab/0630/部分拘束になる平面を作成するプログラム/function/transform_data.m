% データのモーメントを0にするものと, メッシュ関数が適用可能に変形する関数

function [x, y, z] = transform_data(data)
    row = size(data,1);
    for i = 1:row
        data(i, 3) = 0;
    end

    remainder = rem(row, 5);

    x = reshape(data(1:row-remainder, 1), [], 5);
    y = reshape(data(1:row-remainder, 2), [], 5);
    z = reshape(data(1:row-remainder, 3), [], 5);
end