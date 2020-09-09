% Jacob Rusch
% 11 June 2020
% Getting Von Mises stress at integration points and averaging them to
% produce a stress-strain plot

clear;
clc;

%% Get data from text files that were exported from ABAQUS

filename = '0_90_90_Angles-S-S33.txt';
delimiterIn = ' ';
headerlinesIn = 4;
Import_data = importdata(filename,delimiterIn,headerlinesIn);
stress = Import_data.data(:,[2,3,4,5,6,7,8,9]);

filename = '0_90_90_Angles-LE-LE33.txt';
delimiterIn = ' ';
headerlinesIn = 4;
Import_data = importdata(filename,delimiterIn,headerlinesIn);
strain = Import_data.data(:,[2,3,4,5,6,7,8,9]);


%% Volume averaging
% In this simulation, there is only one element but there are eight
% integration points, so the data will be averaged over the integrations
% points. Can do this in one loop since all the simulations are run for the
% same amount of steps and therefore have the same rows and columns

Average_VM = sum(stress,2)/size(stress,2);
Average_LE = sum(strain,2)/size(strain,2);

Average_VM = Average_VM';
Average_LE = Average_LE';

%% Plotting
% plotting the stress-strain curve
figure
subplot(1,2,1)
plot(abs(Average_LE),abs(Average_VM))
title('Averaged Stress vs Strain [100]','FontSize',14)
% axis([0 0.1 0 1200])
xlabel('Logrithmic Strain LE (\epsilon)','FontSize',14)
ylabel('\sigma_3_3 (MPa)','FontSize',14)
subplot(1,2,2)
plot(abs(strain),abs(stress))
title('Stress vs Strain at Each Gauss Point [100]','FontSize',14)
% axis([0 0.1 0 1200])
xlabel('Logrithmic Strain LE (\epsilon)','FontSize',14)
ylabel('\sigma_3_3 (MPa)','FontSize',14)

