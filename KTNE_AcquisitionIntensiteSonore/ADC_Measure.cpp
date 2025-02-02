#include "ADC_Measure.hpp"
#include "mbed.h"

ADC_Measure::ADC_Measure(PinName pin, float vref, size_t buffer_size)
    : adc(pin), Vref(vref), buffer_size(buffer_size), buffer(buffer_size, 0.0f), index(0) {}

void ADC_Measure::update() {
    measure();
    calculate_average();
    //display_results();
}

void ADC_Measure::measure() {
    float valeur = adc.read();
    instant_voltage = valeur * 100;
    measured_voltage = adc.read_voltage();

    buffer[index] = instant_voltage;
    index = (index + 1) % buffer_size;
}

void ADC_Measure::calculate_average() {
    float sum = 0.0f;
    for (float val : buffer) {
        sum += val;
    }
    average_voltage = sum / static_cast<float>(buffer_size);
}

void ADC_Measure::display_results() {
    std::cout << "Tension instantanée : " << instant_voltage
              << ", Tension mesurée : " << measured_voltage
              << " V, Moyenne : " << average_voltage << " V\n";
}

float ADC_Measure::get_instant_voltage() const {
    return instant_voltage;
}

float ADC_Measure::get_average_voltage() const {
    return average_voltage;
}

float ADC_Measure::get_measured_voltage() const {
    return measured_voltage;
}