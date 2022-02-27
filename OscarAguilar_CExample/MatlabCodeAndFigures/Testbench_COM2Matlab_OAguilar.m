%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Testbench Communication from FreeSoc2 to Matlab
% Version 2.0, Aguilar Aguila 08.07.2020
% -Scaled readings 
% -Changed to 5 readings in total
% -Output of Vpp
%
% Version 1.0, Bannwarth, 30.05.2020
%
% Behaviour: 
% - Everytime Maltlab writes ‘s’on the UART, the PSoC sends new measurement 
%    results and Matalab writes 'o' if these data is received.
% - The Script terminates after 10 data transfers.
%
% Using:
% 1. Connect FreeSoc2 to USB (i.e. Power Up)
% 2. Check the correct serial Port Settings
% 3. Start this Matlab Script
% 4. Run this Script
% 5. Press the external Push Button to start measuring
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

close all;
%%
clear all;
clc;
vcc=4.65;%multimeter measured
res=2^16;
maxFreq=2000;


priorPorts=instrfind;
delete(priorPorts);
PSoC=serial('COM10', 'BaudRate', 9600, 'InputBufferSize', 14000);
fopen(PSoC);

f1 = figure;
count = 1;

flg_data_avai = 0;
fwrite(PSoC,'s','uchar') % means send, I am ready to receive
while(flg_data_avai == 0)
   
       if PSoC.BytesAvailable >= 2048
             fwrite(PSoC,'o','uchar') % means I received all expected data
             rx_data_adc = fread(PSoC,1024,'uint16');
             rx_data_adc=rx_data_adc*vcc/res;
             fprintf(" Transfer %i DONE \n",count);
             
             % Plotting the received data
                
             figure(f1)
             subplot(2,1,1);
             plot([0:(length(rx_data_adc)-1)],rx_data_adc(1:(length(rx_data_adc))));
             ylabel('Voltage [V]'); 
             xlabel('Sample Number');
             title(['Received Time Domain Data No.:',num2str(count)]);
             subplot(2,1,2);
             samples=[0:1023];
             plot(samples*(maxFreq/length(rx_data_adc)),mag2db(abs(fft(rx_data_adc))/max(abs(fft(rx_data_adc)))));

             ylabel('Magnitude in relative full scale [dB]'); 
             xlabel('Frequency [Hz]');
             title('FFT -  Matlab');

             % Save the received data
             save(strcat('CW_rx_data_adc_',int2str(count),'.mat'),'rx_data_adc');
             count=count+1;
       end

       if count == 6
           break;
       end

       fwrite(PSoC,'s','uchar'); % means send, I am ready to receive
end

fclose(PSoC);

fprintf(" Scipt End \n");
maximum=max(rx_data_adc);
minimum=min(rx_data_adc);
vpp=maximum-minimum;
fprintf(" MAX = %i \n",maximum);
fprintf(" MIN = %i \n",minimum);
fprintf(" VPP = %i \n",vpp);

