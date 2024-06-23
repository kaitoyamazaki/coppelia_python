% データのインポート（CSVファイル等の形式を仮定）
data = csvread('path_to_your_data.csv'); % データファイルのパスを指定

% データの分割（列の仮定: 時間データが1列目、信号データが2列目）
time = data(:, 1);
signal = data(:, 2);

% 移動平均フィルタの適用
window_size = 5;
filtered_signal = movmean(signal, window_size);

% プロット
figure;
plot(time, signal, 'b', 'DisplayName', 'Original Signal');
hold on;
plot(time, filtered_signal, 'r', 'DisplayName', 'Filtered Signal');
title('Signal with Moving Average Filter');
xlabel('Time [s]');
ylabel('Amplitude');
legend show;
hold off;
