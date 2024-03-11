% シミュレータ内で取得した物体データをse2空間で描画する

addpath('../../..', '-end');

csv_list = dir('../data/*.csv');


hold on;
view(-45,15);
xlim([-100 100]);
ylim([-100 100]);
zlim([0 180]);
xlabel('x[mm]');
ylabel('y[mm]');
zlabel('theta[rad]');

for i = 1:length(csv_list)
    filepath = fullfile(csv_list(i).folder, csv_list(i).name);

    se2_data = readmatrix(filepath);

    plot3(se2_data(:, 1), se2_data(:, 2), se2_data(:, 3), "LineWidth", 3, 'Color', 'g');

    se2_data_first_row = se2_data(1, :);
    se2_data_end_row = se2_data(end, :);

    plot3(se2_data_first_row(:, 1), se2_data_first_row(:, 2), se2_data_first_row(:, 3), '.', 'MarkerSize', 30, 'Color', 'b');
    plot3(se2_data_end_row(:, 1), se2_data_end_row(:, 2), se2_data_end_row(:, 3), '.', 'MarkerSize', 30, 'Color', 'k');
end

grid on;
hold off;