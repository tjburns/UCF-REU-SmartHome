close all;
clear all;
clc;
%these will be given as parameters
%example is below
filename='success_rates.txt';ylabeltext='Success Rates';outputfilename='PDFSR';stepnum=1;
%filename='message_delays.txt';ylabeltext='Message Delays';outputfilename='PDFMD';stepnum=20;

grey = [0.7,0.7,0.7];
darkgrey = [0.4,0.4,0.4];
black=[0 0 0];


type{1}='-o';   color{1} = grey;    lineWidth{1} = 1.5;  markerSize{1} = 7;  
type{2}=':x';  color{2} = black;     lineWidth{2} = 3.0;  markerSize{2} = 12;
type{3}='-.s';   color{3} = darkgrey;    lineWidth{3} = 1.5;  markerSize{3} = 8;
type{4}='--v';  color{4} = grey; lineWidth{4} = 2.0;  markerSize{4} = 7;
type{5}='-*';   color{5}= black;      lineWidth{5}= 1.5;   markerSize{5}= 8;
type{6}='-*';   color{6}= darkgrey;    lineWidth{6}= 1.5;   markerSize{6}= 8;
type{7}='-.h';  color{7}= grey;     lineWidth{7}= 1.5;   markerSize{7}= 8;
type{8}='--p';  color{8}= black;  lineWidth{8}= 2.0;   markerSize{8}= 6;
type{9}='-^';   color{9}= darkgrey;  lineWidth{9}= 2.0;   markerSize{9}= 9;
type{10}=':h';  color{10} = grey;    lineWidth{10} = 3.5; markerSize{10} = 7;
type{11}='--p';   color{11}= black;  lineWidth{11}= 1.5;   markerSize{11}= 8;
type{12}='-.h';  color{12} = darkgrey;    lineWidth{12} = 3.5; markerSize{12} = 6;



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





figure;
for j=1:count
	A=sort(bars{j});
	c=length(A);
	% ceil makes 3.2 to 4
	% fix makes 3.6 to 3
	B=zeros(1,ceil(A(c)/stepnum)+1);
    for i=1:c
        v=fix(A(i)/stepnum)+1;
        B(v)=B(v)+1/c;
    end
    
	y=(0:stepnum:(stepnum*length(B))-1);

	plot(y,B,type{j},'color', color{j},'LineWidth',lineWidth{j} , 'MarkerSize',markerSize{j});
    hold on;
    %bottom dash will be processed as if it is latex expression. We are
    %escaping from that.
    names{j}=strrep(names{j},'_','\_');
end




ylabel('Probability', 'FontSize',60); 
xlabel(ylabeltext, 'FontSize',60);
set(gca,'FontSize',60);

ExpLegend = legend(names(1:count));                                 
set(ExpLegend,'FontSize',20);
rect = [0.59 0.77, 0.2, 0.15];

set(ExpLegend, 'Position', rect);
set(gcf, 'PaperPosition',[0 0 80 60]); %Position the plot further to the left and down. Extend the plot to fill entire paper.
set(gcf, 'PaperSize', [80 60]); %Keep the same paper size
colormap gray
saveas(gcf, outputfilename, 'pdf');
%closing the figure
set(gcf, 'Visible', 'off');

