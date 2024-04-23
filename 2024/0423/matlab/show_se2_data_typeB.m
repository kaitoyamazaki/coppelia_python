% シミュレーションで取得した値を可視化(typeAのみ)
addpath('../../..', '-end');

csv_list_s1 = dir('data/B/success/typeB/*.csv');

hold on;
view(-145,45);
xlim([-200 200]);
ylim([0 300]);
zlim([0 180]);
xlabel('x[mm]');
ylabel('y[mm]');
zlabel('theta[rad]');

for i = 1:length(csv_list_s1)
    filepath = fullfile(csv_list_s1(i).folder, csv_list_s1(i).name);

    se2_data = readmatrix(filepath);

    plot3(se2_data(:, 1), se2_data(:,2), se2_data(:,3), "LineWidth", 3, 'Color', 'g');

    se2_data_first_row = se2_data(1, :);
    se2_data_end_row = se2_data(end, :);

    plot3(se2_data_first_row(:,1), se2_data_first_row(:,2), se2_data_first_row(:,3), '.', 'MarkerSize', 30, 'Color', 'b');
    plot3(se2_data_end_row(:,1), se2_data_end_row(:,2), se2_data_end_row(:,3), '.', 'MarkerSize', 30, 'Color', 'k');
end

grid on;
hold off;