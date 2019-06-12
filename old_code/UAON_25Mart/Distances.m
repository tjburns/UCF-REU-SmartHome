% In the same folder with this file there are folders 
% each of the folder has txt files
% these txt files are being processed
% the name of the folders are used as legend
% Safa Bacanli 2017 May


grey = [0.7,0.7,0.7];
darkgrey = [0.4,0.4,0.4];
black=[0 0 0];

folders=dir(workfolder);
folders(1:2) = [];
% Get a logical vector that tells which is a directory.
dirFlags = [folders.isdir];
% Extract only those that are directories.
folders = folders(dirFlags);

lengthf=length(folders);
names=cell(1,lengthf);
count=1;
bars=zeros(1,lengthf);
%bars is an 2D array
%each row is the folder name related simulation


for i=1:lengthf
        %the names of the folders will be in this cell vector
        names{count}=(folders(i).name);
        insidefolders=dir(strcat(workfolder,names{count}));
        %for each file inside this folder
        for j=1:length(insidefolders)
            if strcmp(insidefolders(j).name,'UAVDistances.txt')==1
				nameOfFile=strcat(workfolder,folders(i).name,'\',insidefolders(j).name);
                %get the relative path of this file
                bars(count,1)=mean(load(nameOfFile));
            end
        end
        %bottom dash will be processed as if it is latex expression. We are
        %escaping from that.
        names{count}=strrep(names{count},'_','\_');
        count=count+1;
end

%this is vital as count is increased 1 more
count=count-1;

%bars till count will be used in this bars array only. So we only get
%count items
bar(1:count, bars(1:count,:), 1);
% we are increasing the y limit so that there will be space to put
% the legend box
z=ylim;
ylim([0 z(2)+8000]);


set(gca, 'XTick',(1:count), 'XTickLabel',names(1:count));

set(gca,'FontSize',55);

ylabel('Distance(m)', 'FontSize',55); 
xlabel('Routing Types', 'FontSize',55);


legendarr=cell(1,1);
legendarr{1}='Distances Travelled by UAVs';
ExpLegend = legend(legendarr);

                                 
set(ExpLegend,'FontSize',20);
%rect = [0.56 0.77, 0.2, 0.15];
%set(ExpLegend, 'Position', rect);
set(ExpLegend,'Location','northeast');

set(gcf, 'PaperPosition',[0 0 80 60]); %Position the plot further to the left and down. Extend the plot to fill entire paper.
set(gcf, 'PaperSize', [80 60]); %Keep the same paper size
set(gca, 'box','on');
colormap gray
saveas(gcf, outputfilename, 'pdf');			
close all;
clear all;