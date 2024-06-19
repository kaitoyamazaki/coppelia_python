% Number of random points
numPoints = 100;

% Initial point
initialPoint = [0.0, 0.0, 0.0];

% Generate random points within specified ranges
x = -0.5 + rand(numPoints, 1) * (0.5 - (-0.5));
y = rand(numPoints, 1) * (1.0 - 0);
z = -180 + rand(numPoints, 1) * (180 - (-180));

% Add the initial point
x = [initialPoint(1); x];
y = [initialPoint(2); y];
z = [initialPoint(3); z];

% Define colors: red for the initial point, blue for others
colors = [1, 0, 0; repmat([0, 0, 1], numPoints, 1)];

% Plot the points
figure;
scatter3(x, y, z, 36, colors, 'filled');
xlabel('x [m]');
ylabel('y [m]');
zlabel('\theta [°]');
zlim([-180, 180]);
title('test');
grid on;

view(45, 50);