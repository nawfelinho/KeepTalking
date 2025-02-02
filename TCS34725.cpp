#include "TCS34725.hpp"
#include "mbed.h"
 
TCS34725::TCS34725(I2C &i2c, TCS34725::IntegrationTime iTime, TCS34725::Gain gain)
    : i2c(i2c), integrationTime(iTime), gain(gain), initialized(false) {}
 
bool TCS34725::Initialize() {
    uint8_t id = read8(TCS34725_ID);
    if (id != 0x44) { // ID du capteur
        return false;
    }

    initialized = true;
 
    setIntegrationTime(integrationTime);
    setGain(gain);
 
    write8(TCS34725_ENABLE, TCS34725_ENABLE_PON);
    write8(TCS34725_ENABLE, TCS34725_ENABLE_PON | TCS34725_ENABLE_AEN);
 
    return true;
}
 
void TCS34725::setIntegrationTime(TCS34725::IntegrationTime iTime) {
    if (!initialized) Initialize();
    write8(TCS34725_ATIME, static_cast<uint8_t>(iTime));
    integrationTime = iTime;
}
 
void TCS34725::setGain(TCS34725::Gain gain) {
    if (!initialized) Initialize();
    write8(TCS34725_CONTROL, static_cast<uint8_t>(gain));
    gain = gain;
}

uint16_t TCS34725::Normalize(uint16_t value) {
    if (value < 85) 
        value = 0;
    else if (value > 170) 
        value = 255;
    else 
        value = 128;
    return value;
};

void TCS34725::FormaterCouleur(uint16_t *r, uint16_t *g, uint16_t *b, uint16_t *c) {

    uint16_t r_normalized{0};
    uint16_t g_normalized{0};
    uint16_t b_normalized{0};

    if (*c > 10) {
        // Normalisation des valeurs RGB en fonction de C
        r_normalized = (*r * 255) / *c;
        g_normalized = (*g * 255) / *c;
        b_normalized = (*b * 255) / *c;

        r_normalized = TCS34725::Normalize(r_normalized);
        g_normalized = TCS34725::Normalize(g_normalized);
        b_normalized = TCS34725::Normalize(b_normalized);
    }
}

void TCS34725::CapterCouleur(uint16_t *r, uint16_t *g, uint16_t *b, uint16_t *c) {
    if (!initialized) Initialize();
 
    *c = read16(TCS34725_CDATAL);
    *r = read16(TCS34725_RDATAL);
    *g = read16(TCS34725_GDATAL);
    *b = read16(TCS34725_BDATAL);
 
    // On attend pendant l'acquisition
    //switch (integrationTime) {
        //case TCS34725::IntegrationTime::TCS34725_INTEGRATIONTIME_2_4MS:  ThisThread::sleep_for(3ms); break;
        //case TCS34725::IntegrationTime::TCS34725_INTEGRATIONTIME_24MS:   ThisThread::sleep_for(24ms); break;
        //case TCS34725::IntegrationTime::TCS34725_INTEGRATIONTIME_50MS:   ThisThread::sleep_for(50ms); break;
        //case TCS34725::IntegrationTime::TCS34725_INTEGRATIONTIME_101MS:  ThisThread::sleep_for(101ms); break;
        //case TCS34725::IntegrationTime::TCS34725_INTEGRATIONTIME_154MS:  ThisThread::sleep_for(154ms); break;
        //case TCS34725::IntegrationTime::TCS34725_INTEGRATIONTIME_700MS:  ThisThread::sleep_for(700ms); break;
    //}

    TCS34725::FormaterCouleurs(r, g, b, c);
}
 
void TCS34725::write8(uint8_t reg, uint8_t value) {
    char data[2] = {(char)(TCS34725_COMMAND_BIT | reg), (char)value};
    i2c.write(TCS34725_ADDRESS, data, 2);
}
 
uint8_t TCS34725::read8(uint8_t reg) {
    char cmd = TCS34725_COMMAND_BIT | reg;
    char value;
    i2c.write(TCS34725_ADDRESS, &cmd, 1);
    i2c.read(TCS34725_ADDRESS, &value, 1);
    return value;
}
 
uint16_t TCS34725::read16(uint8_t reg) {
    char cmd = TCS34725_COMMAND_BIT | reg;
    char data[2];
    i2c.write(TCS34725_ADDRESS, &cmd, 1);
    i2c.read(TCS34725_ADDRESS, data, 2);
    return (data[1] << 8) | data[0];
}