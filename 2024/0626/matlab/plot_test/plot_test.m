% Parameters
r_inner = 0.1; % Radius of the inner circle
r_outer = 0.3; % Radius of the outer circle
N = 100; % Number of points to generate

% Generate random points in polar coordinates
theta = 2 * pi * rand(N, 1); % Random angles
r = sqrt((r_outer^2 - r_inner^2) * rand(N, 1) + r_inner^2); % Random radii ensuring uniform distribution

% Convert to Cartesian coordinates
x = r .* cos(theta);
y = r .* sin(theta);

% Generate random orientations for z coordinate
z = -180 + 360 * rand(N, 1);

% Plotting the generated points
figure;
scatter(x, y, 'b.');
hold on;
viscircles([0, 0], r_inner, 'LineWidth', 1, 'Color', 'k');
viscircles([0, 0], r_outer, 'LineWidth', 1, 'Color', 'k');
axis equal;
grid on;
title('Random points in the annular region between two circles');

% Displaying a sample of generated 3D points
sample_points = [x, y, z];
disp('Sample of generated 3D points:');
disp(sample_points(1:10, :));