% シミュレータ内で取得した物体データをse2空間で描画する

addpath('../../..', '-end');
se2_data = readmatrix('../data/object_se2_data.csv');
se2_data2 = readmatrix('../data/object_se2_data2.csv');

hold on;
view(-45,15);
xlim([-100 100]);
ylim([-100 100]);
zlim([0 180]);
xlabel('x[mm]');
ylabel('y[mm]');
zlabel('theta[rad]');


plot3(se2_data(:, 1), se2_data(:, 2), se2_data(:, 3), "LineWidth", 3, 'Color', 'g');
plot3(se2_data2(:, 1), se2_data2(:, 2), se2_data2(:, 3), "LineWidth", 3, 'Color', 'r');

se2_data_first_row = se2_data(1, :);
se2_data2_first_row = se2_data2(1, :);

plot3(se2_data_first_row(:, 1), se2_data_first_row(:, 2), se2_data_first_row(:, 3), '.', 'MarkerSize', 30, 'Color', 'b');
plot3(se2_data2_first_row(:, 1), se2_data2_first_row(:, 2), se2_data2_first_row(:, 3), '.', 'MarkerSize', 30, 'Color', 'b');

se2_data_end_row = se2_data(end, :);
se2_data2_end_row = se2_data2(end, :);

plot3(se2_data_end_row(:, 1), se2_data_end_row(:, 2), se2_data_end_row(:, 3), '.', 'MarkerSize', 30, 'Color', 'k');
plot3(se2_data2_end_row(:, 1), se2_data2_end_row(:, 2), se2_data2_end_row(:, 3), '.', 'MarkerSize', 30, 'Color', 'k');

grid on;
hold off;