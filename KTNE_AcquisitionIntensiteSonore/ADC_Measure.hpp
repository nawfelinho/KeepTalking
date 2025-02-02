#ifndef ADC_MEASURE_HPP
#define ADC_MEASURE_HPP

#include "mbed.h"
#include <cstdint>
#include <vector>
#include <iostream>

class ADC_Measure {
public:
    ADC_Measure(PinName pin, float vref, size_t buffer_size);
    void update(); // Effectue une seule itération (sans boucle infinie)

    // Getters pour accéder aux valeurs
    float get_instant_voltage() const;
    float get_average_voltage() const;
    float get_measured_voltage() const;

private:
    AnalogIn adc;
    const float Vref;
    const size_t buffer_size;
    std::vector<float> buffer;
    size_t index;

    float instant_voltage;
    float measured_voltage;
    float average_voltage;

    void measure();
    void calculate_average();
    void display_results();
};

#endif // ADC_MEASURE_HPP