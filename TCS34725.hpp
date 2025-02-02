#ifndef _TCS34725_H_
#define _TCS34725_H_
 
#include "ICapteurCouleur.hpp"
#include "mbed.h"
 
// I2C address
#define TCS34725_ADDRESS          (0x29 << 1)
#define TCS34725_COMMAND_BIT      (0x80)
 
// Register definitions
#define TCS34725_ENABLE           (0x00)
#define TCS34725_ENABLE_PON       (0x01)
#define TCS34725_ENABLE_AEN       (0x02)
#define TCS34725_ATIME            (0x01)
#define TCS34725_CONTROL          (0x0F)
#define TCS34725_ID               (0x12)
#define TCS34725_CDATAL           (0x14)
#define TCS34725_RDATAL           (0x16)
#define TCS34725_GDATAL           (0x18)
#define TCS34725_BDATAL           (0x1A)
 
class TCS34725 : public ICapteurCouleur {
public:
    enum class IntegrationTime {
    TCS34725_INTEGRATIONTIME_2_4MS  = 0xFF,
    TCS34725_INTEGRATIONTIME_24MS   = 0xF6,
    TCS34725_INTEGRATIONTIME_50MS   = 0xEB,
    TCS34725_INTEGRATIONTIME_101MS  = 0xD5,
    TCS34725_INTEGRATIONTIME_154MS  = 0xC0,
    TCS34725_INTEGRATIONTIME_700MS  = 0x00
    };

    enum class Gain {
    TCS34725_GAIN_1X                = 0x00,
    TCS34725_GAIN_4X                = 0x01,
    TCS34725_GAIN_16X               = 0x02,
    TCS34725_GAIN_60X               = 0x03
    };

private:
    I2C &i2c;
    IntegrationTime integrationTime{IntegrationTime::TCS34725_INTEGRATIONTIME_2_4MS};
    Gain gain{Gain::TCS34725_GAIN_1X};
    bool initialized{false};

    void write8(uint8_t reg, uint8_t value);
    uint8_t read8(uint8_t reg);
    uint16_t read16(uint8_t reg);
    void FormaterCouleur(uint16_t *r, uint16_t *g, uint16_t *b, uint16_t *c);
    uint16_t Normalize(uint16_t value);

public:
    TCS34725(I2C &i2c, IntegrationTime = IntegrationTime::TCS34725_INTEGRATIONTIME_2_4MS, Gain = Gain::TCS34725_GAIN_1X);
    virtual ~TCS34725() override = default;
 
    bool Initialize();
    void setIntegrationTime(IntegrationTime it);
    void setGain(Gain gain);
    void CapterCouleur(uint16_t *r, uint16_t *g, uint16_t *b, uint16_t *c) override;
};
 
#endif