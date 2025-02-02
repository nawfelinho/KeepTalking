#ifndef CAPTEUR_DISTANCE_HPP
#define CAPTEUR_DISTANCE_HPP

#include "mbed.h"
#include <cstdint>

class CapteurDistance {
    private:
        AnalogIn capteur;
        uint16_t distance{0};
        void setDistance(uint16_t value){this->distance=value;};
    public:
        CapteurDistance(PinName pin):capteur(pin){};
        ~CapteurDistance()=default;
        uint16_t getDistance(){return this->distance;};
        void readCapteur(){setDistance(uint16_t(capteur.read_u16()*0.01998425));};


};
/*
 -distance uint16_t
        -setDistance()
        +CapteurDistance(Pinname)
        ~CapeteurDistance()
        +getDistance() uint16_t
        +readCapteur()
        */
#endif // CAPTEUR_DISTANCE_HPP