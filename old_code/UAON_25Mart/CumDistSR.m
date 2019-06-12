close all;
clear all;
clc;
ylabeltext='Success Rates';filename='success_rates.txt';outputfilename='CDFSR';

grey = [0.7,0.7,0.7];
darkgrey = [0.4,0.4,0.4];
black=[0 0 0];

type{1}='-';   color{1} = grey;    lineWidth{1} = 1.5;  markerSize{1} = 7;  
type{2}='-.';  color{2} = black;     lineWidth{2} = 3.0;  markerSize{2} = 12;
type{3}='--';   color{3} = darkgrey;    lineWidth{3} = 1.5;  markerSize{3} = 8;
type{4}=':';  color{4} = grey; lineWidth{4} = 2.0;  markerSize{4} = 7;
type{5}='-';   color{5}= black;      lineWidth{5}= 1.5;   markerSize{5}= 8;
type{6}='-.';   color{6}= darkgrey;    lineWidth{6}= 1.5;   markerSize{6}= 8;
type{7}='--';  color{7}= grey;     lineWidth{7}= 1.5;   markerSize{7}= 8;
type{8}=':';  color{8}= black;  lineWidth{8}= 2.0;   markerSize{8}= 6;
type{9}='-';   color{9}= darkgrey;  lineWidth{9}= 2.0;   markerSize{9}= 9;
type{10}='-.';  color{10} = grey;    lineWidth{10} = 3.5; markerSize{10} = 7;
type{11}='--';   color{11}= black;  lineWidth{11}= 1.5;   markerSize{11}= 8;
type{12}=':';  color{12} = darkgrey;    lineWidth{12} = 3.5; markerSize{12} = 6;

folders=dir;
folders(1:2) = [];
% Get a logical vector that tells which is a directory.
dirFlags = [folders.isdir];
% Extract only those that are directories.
folders = folders(dirFlags);

lengthf=length(folders);
names=cell(1,lengthf);
count=1;
bars=cell(1,lengthf);

for i=1:lengthf
        names{count}=(folders(i).name);
        insidefolders=dir(names{count});
        for j=1:length(insidefolders)
            if strcmp(insidefolders(j).name,filename)==1
                nameOfFile=strcat(folders(i).name,'/',insidefolders(j).name);
                %disp(nameOfFile);
                bars{count}=load(nameOfFile);
            end
        end
        count=count+1;
end
count=count-1;


for i=1:count
	hold on;
	arr=bars{i};
	h=cdfplot(arr);
	hold off;
	set(h,'color',color{i});
    set(h,'LineStyle',type{i});
    set(h,'LineWidth',lineWidth{i});
    set(h,'MarkerSize',markerSize{i});
end

ylabel('Percentage', 'FontSize',40); 
xlabel(strcat(ylabeltext,' (%)'), 'FontSize',40);
set(gca,'FontSize',40);
title('');

ExpLegend = legend(names(1:count));     
set(ExpLegend,'FontSize',10);
set(ExpLegend,'Location','southeast');

%rect = [0.7 0.15 0.17 0.16];
%set(ExpLegend, 'Position', rect);

set(gcf, 'PaperPosition',[0 0 40 30]); %Position the plot further to the left and down. Extend the plot to fill entire paper.
set(gcf, 'PaperSize', [40 30]); %Keep the same paper size
colormap gray
saveas(gcf, outputfilename, 'pdf');		