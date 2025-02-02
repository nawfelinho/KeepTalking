#ifndef _CODECOULEUR_
#define _CODECOULEUR_

#define FREQUENCY 20000
#define TRAME_PRESENCE_ID 0x730
#define TRAME_COULEUR_ID 0x030
#define MASK 0x7FF
 
#include "TCS34725.hpp"
#include <cstdint>
 
class CodeCouleur {
private:
    I2C i2c;
    TCS34725 tcs34725;
    CAN can;
public:
    CodeCouleur(PinName sda, PinName scl, PinName rx, PinName tx) : i2c(sda, scl), tcs34725(i2c), can(rx, tx) {};
    virtual ~CodeCouleur() = default;
    void Initialize();
    int CoderCouleur();
	bool recevoirTramePresence();
	void envoyerTramePresence();
	void envoyerTrameCode(int codeCouleur);
};

#endif