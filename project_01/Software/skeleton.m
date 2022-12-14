function skeleton
% This is the skeleton outline of the glucose sensor program

clear = "";
button_state = 0;
% If button is pressed, initiate sensing procedure
while button_state == 0
    button_state = read_button;
end

ir_data = initiate_sensor();
[mgdl, mmol] = analyze(ir_data);
glucose = [mgdl, mmol];
unit_toggle = 1;
output_screen(glucose(unit_toggle));

button_state = 0;

while button_state == 0
    button_state = read_button;
end

output_screen(clear);
if unit_toggle == 1
    output_screen(glucose(2));
    unit_toggle = 2;
else
    output_screen(glucose(1));
    unit_toggle = 1;
end

end

function button_value = read_button
% Reads button input

button_value = 1;

end

function data = initiate_sensor
% Reads spectroscopy data

data = 499; % Analog voltage of sensor

end


function [mgdl,mmol] = analyze(data)
% Performs regression on calibrate sensor readings and converts to glucose
% concentration levels
severe_hypo = 53; % Severe Hypoglycemia is <53 mg/dL
hypo = 70; % Hypoglycemia is <70 mg/dL
hyper = 125; % Hyperglycemia is >125 mg/dL
severe_hyper = 200; % Sever Hyperglycemia is >200 mg/dL
red = 3;
yellow = 2;
green = 1;

mgdl = (3*10^-5) *data^2 + 0.2903*data - 4.798; % Glucose concentration in mg/dL
mmol = mgdl/18; % Glucose concentration in mmol/L

led = green;
if mgdl > severe_hyper || mgdl < severe_hypo
    led = red;
elseif mgdl > hyper || mgdl < hypo
    led = yellow;
end

activate_led(led, 1);

end

function activate_led(led, state)
% Toggles LED given the index of the color LED and whether HIGH or LOW
% state is requested
leds = ["green", "yellow", "red"];
fprintf("%s LED is toggled %d\n", leds(led), state);
end

function output_screen(output)
% This function outputs result to display

disp(output);

end
