clear all
close all

frx = [1; 2; 3; 4; 5;6;7]';

% Data
mit = [-0.0264 -0.4557 -0.5190 -0.4360 -0.0663 -0.6979 -0.4937];

tri = [0.000830999 0.001491397 0.001516466 0.001822922 0.00193348];

tju = [0.00029018 0.00124358 0.001507521 0.001225513 0.001285868];

xjtu = [0.00229439 0.002630064 0.002855354 0.003785249 0.00666101];


% Plotting
figure;
bar(frx, mit, 'FaceColor', [0, 0.5625, 0.7422], 'EdgeColor', [0, 0.5625, 0.7422], 'LineWidth', 1);
hold on;
%plot(frx, tri, '-^', 'Color', [0.8516, 0.3242, 0.0977], 'MarkerFaceColor', [0.8516, 0.3242, 0.0977], 'LineWidth', 2);
%plot(frx, tju, '-s', 'Color', [0, 0.6196, 0.4510], 'MarkerFaceColor', [0, 0.6196, 0.4510], 'LineWidth', 2);
%plot(frx, xjtu, '-s', 'Color', [0.8000, 0.4745, 0.6549], 'MarkerFaceColor', [0.8000, 0.4745, 0.6549], 'LineWidth', 2);


% Labels and Legend
xlabel('Number of Blocks');
ylabel('MSE');

% Axes Limits and Ticks
%xlim([min(frx)-0.5, max(frx)+8]);
%set(gca, 'XTick', frx, 'XScale', 'log', 'XTickLabel', string(frx));

xlim([0, 8]);
set(gca, 'XTick', 0:1:7);

ylim([-0.9, 0]);          % lower limit -1, upper limit 0
set(gca,'YTick',-0.9:0.1:0);

% Formatting
set(gca, 'FontName', 'Arial', 'FontSize', 18, 'FontWeight', 'bold', 'LineWidth', 1.5);
set(gca, 'PlotBoxAspectRatio', [1 1 1]);  % Equal length axes
box on;
grid on;

set(gca, 'XMinorTick', 'off', 'XMinorGrid', 'off');
set(gca, 'YMinorTick', 'off', 'YMinorGrid', 'off');

% Formatting
set(gca, 'FontName', 'Arial', 'FontSize', 18, 'FontWeight', 'bold', 'LineWidth', 1.5);
%set(gca, 'PlotBoxAspectRatio', [1 1 1]);  % Equal length axes
set(gca,'PlotBoxAspectRatioMode','auto');   % 或显式改回自动
box on;
grid on;

% Adjust axes position to remove white margins
ti = get(gca, 'TightInset');
set(gca, 'Position', [ti(1), ti(2), 1 - ti(1) - ti(3), 1 - ti(2) - ti(4)]);
set(gca, 'LooseInset', [0, 0, 0, 0]);

% Optimize figure appearance
set(gcf, 'Units', 'centimeters');
pos = get(gcf, 'Position');
set(gcf, 'PaperUnits', 'centimeters');
set(gcf, 'PaperPosition', [0, 0, pos(3), pos(4)]);
set(gcf, 'PaperSize', [pos(3), pos(4)]);

% Save the figure without white margins
%print(gcf, 'myfigure.png', '-dpng', '-r300');
%set(gcf, 'PaperPosition', [0, 0, pos(3), pos(4)]);
%set(gcf, 'PaperSize', [pos(3), pos(4)]);

