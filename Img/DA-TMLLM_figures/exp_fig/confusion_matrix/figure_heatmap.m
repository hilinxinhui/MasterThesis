function figure_heatmap(data_input,color_scheme_in,...
    text_title_in,text_labels_in,limits_data_in,text_labels_cells_in,...
    savefig_in,savefig_name_in)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Adaption of MATLAB heatmap function to plot nice publication-quality heatmaps easily
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Written by: Ahmed Abdul Quadeer
% E-mail: ahmedaq@gmail.com
% Last change: May 4, 2018
% Copyright (c) Ahmed Abdul Quadeer, 2018
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Inputs:   
%
% - data_input: Input data       
%   A matrix of size MxN
%
% - color_scheme_in: Color scheme for heatmap
%   Brewermap package required from
%   https://github.com/DrosteEffect/BrewerMap/blob/master/brewermap.m
%   For example: 'OrRd', 'YlOrRd', 'BuPu', or 'BuGn'.
%
% - text_title_in: Title of the heatmap
%   Cell (containing text)
%
% - text_labels_in: Labels for x-axis and y-axis
%   Cell of length 2, with first cell having text of x-axis label and 
%   second cell having text of y-axis label
%
% - limits_data_in: Lower and upper limit of colormap (based on data)
%   Row vector of length 2: [Lower_limit Upper_limit]
%   For example: 
%       * [-1 1] for a correlation matirx
%       * [0 100] for a matrix showing overlap between different vectors
%
% - text_labels_cells: Labels for x-axis and y-axis cells
%   Cell of length 2, with first cell having a vector of x-axis cell 
%   labels and second cell having a vector of y-axis cell labels
%
% - savefig_in: Option to save figure automatically (in png format)
%   * 1 - Yes, save the figure
%   * 0 - No
%
% - savefig_name_in: Name for the figure file
%   Text data
%
% Output: Heatmap figure

%% Setting font and size

set(0,'DefaultAxesFontName','Arial')
set(0,'DefaultTextFontName','Arial')
set(0,'DefaultAxesFontSize',8)
set(0,'DefaultTextFontSize',8)

%% Defaults

%Brewermap add-on is required for defining colormaps
color_scheme = brewermap(100,'RdPu');
% 'YlOrRd','BuPu', and 'BuGn' are nice as well
text_title = ' ';
text_labels{1} = ' ';
text_labels{2} = ' ';
text_labels_cells{1} = (1:1:size(data_input,1));
text_labels_cells{2} = (1:1:size(data_input,2));
limits_data = [round2dp(min(data_input(:)),0) round2dp(max(data_input(:)),0)];
savefig = 0;
savefig_name = 'heatmap_example';

%% Processing with respect to the number of input arguments

if  nargin == 2
    color_scheme = brewermap(100,color_scheme_in);
elseif nargin == 3
    color_scheme = brewermap(100,color_scheme_in);
    text_title = text_title_in;
elseif nargin == 4
    color_scheme = brewermap(100,color_scheme_in);
    text_title = text_title_in;
    text_labels = text_labels_in;
elseif nargin == 4
    color_scheme = brewermap(100,color_scheme_in);
    text_title = text_title_in;
    text_labels = text_labels_in;    
    limits_data = limits_data_in;
elseif nargin == 6
    color_scheme = brewermap(100,color_scheme_in);
    text_title = text_title_in;
    text_labels = text_labels_in;
    text_labels_cells = text_labels_cells_in;    
    limits_data = limits_data_in;
elseif nargin == 7
    color_scheme = brewermap(100,color_scheme_in);
    text_title = text_title_in;
    text_labels = text_labels_in;
    text_labels_cells = text_labels_cells_in;    
    limits_data = limits_data_in;
    savefig = savefig_in;
elseif nargin == 8
    color_scheme = brewermap(100,color_scheme_in);
    text_title = text_title_in;
    text_labels = text_labels_in;
    text_labels_cells = text_labels_cells_in;    
    limits_data = limits_data_in;
    savefig = savefig_in;
    savefig_name = savefig_name_in;
end

%% Rounding to 2 decimal points

data_input = round2dp(data_input,2);
% Code downloaded from 
% https://www.mathworks.com/matlabcentral/fileexchange/24213-round2dp?focused=5117033&tab=function&s_tid=gn_loc_drop

%% Generating heatmap figure

figure;
heatmap(text_labels_cells{1},text_labels_cells{2},data_input);
title(text_title)
h = set(gca,'Colormap',color_scheme,'ColorLimits',limits_data);
xlabel(text_labels{1})
ylabel(text_labels{2})

%% Saving figure

if savefig == 1
    
    if size(data_input,1) == size(data_input,2)
        set(gcf,'PaperUnits','centimeters','PaperPosition',[0 0 20 16])
        print(savefig_name,'-dpng','-r300')
    elseif (size(data_input,1) > size(data_input,2)) && (size(data_input,1) < 3*size(data_input,2))
        set(gcf,'PaperUnits','centimeters','PaperPosition',[0 0 10 20])
        print(savefig_name,'-dpng','-r300')
    elseif size(data_input,1) > 3*size(data_input,2)
        set(gcf,'PaperUnits','centimeters','PaperPosition',[0 0 8 20])
        print(savefig_name,'-dpng','-r300')
    elseif (size(data_input,1) < size(data_input,2)) && (size(data_input,1) > 0.5*size(data_input,2))
        set(gcf,'PaperUnits','centimeters','PaperPosition',[0 0 20 10])
        print(savefig_name,'-dpng','-r300')
    elseif size(data_input,1) < 0.5*size(data_input,2)
        set(gcf,'PaperUnits','centimeters','PaperPosition',[0 0 20 6])
        print(savefig_name,'-dpng','-r300')
    end
    
end

%% 生成 heatmap（把原来的两三行换成下面这一段即可）
hMap = heatmap( ...                                    % ← 把返回值存下来
        text_labels_cells{1}, ...
        text_labels_cells{2}, ...
        data_input);
    
% ① 把你原先的配色/范围设回来
hMap.Colormap    = color_scheme;   % ← 这行别删
hMap.ColorLimits = limits_data;    % ← 这行别删

% 基本属性（你原来的 set/ title/ xlabel/ ylabel 都可以改成下面的写法）

hMap.Title       = text_title;
hMap.XLabel      = text_labels{1};
hMap.YLabel      = text_labels{2};

% ---------- 让坐标轴 & 标题等全部文字加粗（R2018 适用） ----------
ax = struct(hMap).Axes;           % ① 取到内部坐标轴（**隐藏属性**）
ax.FontWeight = 'bold';          % 1) 刻度文字  ←← 你想加粗的重点
ax.XLabel.FontWeight = 'bold';   % 2) X 轴标题
ax.YLabel.FontWeight = 'bold';   % 3) Y 轴标题
ax.Title.FontWeight  = 'bold';   % 4) 图标题
% colorbar(struct(hMap).Axes,'off');   % 仅隐藏
hMap.ColorbarVisible = 'off';

% -------------------------------------------------------------------

% （可选）如果想让单元格里的数值也显得更粗，可再换个“本身就是粗体”的字体：
%ax.FontName = 'Arial Black';     % 或 'Times New Roman Bold'，看机器上装的字体
%ax.FontSize = 20;                % 字号稍微调大更明显