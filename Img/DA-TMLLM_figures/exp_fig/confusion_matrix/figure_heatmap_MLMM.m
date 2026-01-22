clear all;close all;clc

%% proposed

% Generating data
% �������ʼ��? 11��11�������и���Ϊָ������
C = randn(11,11);

C(1,:)=[32, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0]
C(2,:)=[1, 33, 1, 0, 0, 0, 0, 0, 0, 1, 0]
C(3,:)=[1, 1, 31, 1, 0, 0, 0, 0, 2, 0, 0]
C(4,:)=[0, 0, 0, 34, 2, 0, 0, 0, 0, 0, 0]
C(5,:)=[0, 2, 0, 0, 33, 1, 0, 0, 0, 0, 0]
C(6,:)=[0, 2, 0, 0, 0, 34, 0, 0, 0, 0, 0]
C(7,:)=[0, 0, 1, 0, 0, 4, 30, 1, 0, 0, 0]
C(8,:)=[0, 2, 1, 0, 1, 0, 1, 31, 0, 0, 0]
C(9,:)=[0, 1, 2, 0, 0, 1, 0, 0, 31, 1, 0]
C(10,:)=[1, 2, 0, 0, 1, 0, 0, 0, 0, 32, 0]
C(11,:)=[0, 0, 4, 7, 0, 2, 0, 4, 1, 0, 42]


% ÿ�а��кͽ��й�һ��
C(1,:) = C(1,:)/sum(C(1,:));
C(2,:) = C(2,:)/sum(C(2,:));
C(3,:) = C(3,:)/sum(C(3,:));
C(4,:) = C(4,:)/sum(C(4,:));
C(5,:) = C(5,:)/sum(C(5,:));
C(6,:) = C(6,:)/sum(C(6,:));
C(7,:) = C(7,:)/sum(C(7,:));
C(8,:) = C(8,:)/sum(C(8,:));
C(9,:) = C(9,:)/sum(C(9,:));
C(10,:) = C(10,:)/sum(C(10,:));
C(11,:) = C(11,:)/sum(C(11,:));


text_title = '';
text_labels = {'Predicted label','True label'};
%C = corrcoef(x);
limits_data = [0 1]; %for correlation matrix
text_labels_cells{1} = {'FF','MiIR','MoIR','SIR','MiB','MoB','SB','MiOR','MoOR','SOR','UI'}; %x-axis cell labels
text_labels_cells{2} = {'FF','MiIR','MoIR','SIR','MiB','MoB','SB','MiOR','MoOR','SOR','UI'}; %y-axis cell labels

colorscheme = 'YlGnBu';

% Heatmap figure
figure_heatmap(C,colorscheme,text_title,text_labels,limits_data,text_labels_cells);

set(gcf,'PaperUnits','centimeters','PaperPosition',[0 0 160 160])

set(gca, 'Fontname', 'Times New Roman', 'Fontsize', 12);
