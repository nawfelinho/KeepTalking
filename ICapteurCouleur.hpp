#ifndef _ICAPTEURCOULEUR_
#define _ICAPTEURCOULEUR_
#include "mbed.h"

class ICapteurCouleur{
public :
    virtual ~ICapteurCouleur() = default;
    virtual void CapterCouleur(uint16_t *r, uint16_t *g, uint16_t *b, uint16_t *c) = 0;
};

#endif