%Author: Oscar Aguilar Aguila Isaías 766468
%%
close all 
clc
clear all
%%
%Obtaining data from LMV385.raw using LTspice2Matlab.m
filename='LMV385.raw';
figure(5)
dataObtained=LTspice2Matlab(filename,[5 10 11]);%values provided by professor on class
%% Plotting Obtained data

semilogx(dataObtained.freq_vect,20*log10(dataObtained.variable_mat));

ylabel('Magnitude [dB]'); 
xlabel('Frequency [Hz]');
title('Band Pass filter amplifier circuit frequency response vs Simulation Data')
grid on 
hold on
%% storing tested frequencies
frequencies=[10 20 40 50 80 100 200 500 800 1000];
%% A1
A1=[60.26694915,85.36363636,94.8244898,94.88085106,95.57676349,96.96638655,87.23478261,67.96428571,51.26785714,35.85185185];

%% A2 
A2=[1.732405259,2.05484558,2.541193182,2.847064628,2.970391595,2.94613918,2.978618421,3.078034682,2.886015326,2.508264463];
%% Atotal
Atotal=[104.4067797,175.4090909,240.9673469,270.1319149,283.9004149,285.6764706,259.8391304,209.1964286,147.9598214,89.92592593];
%% Plotting my obtained gains for first stage of the amplifier
semilogx(frequencies,20*log10(A1), 'o-');
%% Plotting my obtained gains for second stage of the amplifier
semilogx(frequencies,20*log10(A2),'o-');
%% Plotting my obtained gains for the total amplifier
semilogx(frequencies,20*log10(Atotal),'o-');
%% setting up the legends
legend('Location','southeast');
legend([dataObtained.variable_name_list(5) dataObtained.variable_name_list(10) dataObtained.variable_name_list(11) 'A1 Measured' 'A2 Measured' 'Atotal Measured']);