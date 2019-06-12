close all;
clear all;
clc;
% In the same folder with this file there are folders 
% each of the folder has txt files
% these txt files are being processed
% the name of the folders are used as legend
% Safa Bacanli 2017 May
%the name of the file to be processed in each folder is called filename
%these will be given as parameters

filename='success_rates.txt';ylabeltext='Success Rates';outputfilename='BoxSR';

grey = [0.7,0.7,0.7];
darkgrey = [0.4,0.4,0.4];
black=[0 0 0];

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
        %the names of the folders will be in this cell vector
        names{count}=(folders(i).name);
        insidefolders=dir(names{count});
        %for each file inside this folder
        for j=1:length(insidefolders)
            if strcmp(insidefolders(j).name,filename)==1
                %get the relative path of this file
                nameOfFile=strcat(folders(i).name,'/',insidefolders(j).name);
                %load into the bars cell vector
                bars{count}=load(nameOfFile);
            end
        end
        count=count+1; 
end

%this is vital as count is increased 1 more
count=count-1;

minofrates= length(bars{1});
for fixbars=2:count
    if length(bars{fixbars})< minofrates
        minofrates=length(bars{fixbars});
    end
end

lastbars=cell(1,count);
for p=1:count
    lastbars{p}=bars{fixbars}(1:minofrates);    
end


%we need to convert cell vector to array so that boxplot can draw it
barsarr=cell2mat(lastbars);

figure;
boxplot(barsarr,'Notch','off','Labels',names(1:count),'Colors','k','Whisker',1);
set(gca, 'XTick',(1:count), 'XTickLabel',names(1:count))

set(gca,'FontSize',60);

ylabel(ylabeltext, 'FontSize',60); 
xlabel('Routing Types', 'FontSize',60);

                                 

set(gcf, 'PaperPosition',[0 0 80 60]); %Position the plot further to the left and down. Extend the plot to fill entire paper.
set(gcf, 'PaperSize', [80 60]); %Keep the same paper size
set(gca, 'box','on');
colormap gray
saveas(gcf, outputfilename, 'pdf');	




