@echo off
matlab -nodisplay -nodesktop -nosplash -noFigureWindows -r "BoxPlotSR;quit"
matlab -nodisplay -nodesktop -nosplash -noFigureWindows -r "BoxPlotMD;quit"


matlab -nodisplay -nodesktop -nosplash -noFigureWindows -r "CumDistSR;quit;"
matlab -nodisplay -nodesktop -nosplash -noFigureWindows -r "CumDistMD;quit"


matlab -nodisplay -nodesktop -nosplash -noFigureWindows -r "ProbDistFunc('message_delays.txt','Message Delays','PDFMD',20);quit"
matlab -nodisplay -nodesktop -nosplash -noFigureWindows -r "ProbDistFunc('success_rates.txt','Success Rates','PDFSR',1);quit;"
matlab -nodisplay -nodesktop -nosplash -noFigureWindows -r "MultipleBar;quit;"
matlab -nodisplay -nodesktop -nosplash -noFigureWindows -r "MultipleBarDistance;quit;"
:end