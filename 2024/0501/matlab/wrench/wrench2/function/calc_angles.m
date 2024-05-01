% 取得したwrenchベクトルを基に角度を計算する

function angles = calc_angles(points)
    angles = [];

    [rows, cols] = size(points);

    for i = 1:rows
        angle = atan2(points(i, 2), points(i, 1));
        angle = rad2deg(angle);
        %disp(angle)
        angles = [angles; angle];
    end
end