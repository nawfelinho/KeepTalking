#include "mbed.h"
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <array>

#include "ADC_Measure.hpp"

int main() {
    constexpr float Vref = 3.3f; //Tension de fonctionnement du micro
    constexpr size_t buffer_size = 1; //Taille du buffer pour lissage des mesures
    //constexpr uint32_t measure_interval = 100; //Interval de temps entre 2 mesures

    ADC_Measure adc_measure(p15, Vref, buffer_size); //Constructeur de la classe adc_mesure (capteur de son)
    float measure = 0;

    while (true) {
        adc_measure.update(); // Effectue une mesure
        measure = adc_measure.get_instant_voltage(); //récupération de la mesure

        printf("mesure = %f\n", measure);
        ThisThread::sleep_for(100ms); // interval entre 2 mesure
        }

    return 0;
}









/*
// Déclaration de l'ADC
AnalogIn ADC(p15,5);
constexpr float Vref = 3.3;
constexpr size_t buffer_size = 100; // Taille du buffer pour lisser les données
constexpr uint32_t Mesure_interval(1000);
int main() {
    std::array<float, buffer_size> buffer = {0};
    size_t index = 0;

    while (true) {
        float valeur = ADC.read();
        float tension = valeur * Vref;
        float tension2 = ADC.read_voltage();
        // Mettre à jour le buffer
        buffer[index] = tension;
        index = (index + 1) % buffer_size;

        // Calculer la moyenne
        float moyenne = 0;
        for (float val : buffer) {
            moyenne += val;
        }
        moyenne /= buffer_size;

        std::cout << "Tension instantanée : " << tension << "tension mesurée : " << tension2
                  << " V, Moyenne : " << moyenne << " V\n";

        ThisThread::sleep_for(Mesure_interval);
    }
}*/
/*   
int main()
{
    float valeur = 0;
    float tension = 0;
    float vref = 0;
    uint16_t valeur_brute = 0;

    while (true) {
        //valeur_brute = ADC.read_u16();
        //std::printf("VAL BRUTE : %u\n\n", valeur_brute);
        //Lecture de la valeur analogique et conversion par l'ADC
        valeur = ADC.read();
        std::cout << "VAL :" << valeur << std::endl;
        std::printf("\n");
        //tension = ADC.read_voltage();
        //std::printf("TENSION: %f\n\n", tension);



        ThisThread::sleep_for(100ms);
    }
}*/

