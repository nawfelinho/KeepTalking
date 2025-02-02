#include "CodeCouleur.hpp"
#include "mbed.h"
 
void CodeCouleur::Initialize() {
    tcs34725.Initialize();
	can.frequency(FREQUENCY);
}

int CodeCouleur::CoderCouleur(){
    uint16_t r, g, b, c;
    tcs34725.CapterCouleur(&r, &g, &b, &c);
    if (r == 0){
        if (g == 0) {
            if (b == 0)
                return 0;
            else if (b == 128)
                return 11;
            else
                return 4;
        }
        else if (g == 128) {
            if (b == 0)
                return 10;
            else if (b == 128)
                return 14;
            else
                return 21;
        }
        else {
            if (b == 0)
                return 3;
            else if (b == 128)
                return 22;
            else
                return 7;
        }
    }
    else if (r == 128) {
        if (g == 0) {
            if (b == 0)
                return 9;
            else if (b == 128)
                return 13;
            else
                return 23;
        }
        else if (g == 128) {
            if (b == 0)
                return 12;
            else if (b == 128)
                return 8;
            else
                return 18;
        }
        else {
            if (b == 0)
                return 24;
            else if (b == 128)
                return 19;
            else
                return 15;
        }
    }
    else {
        if (g == 0) {
            if (b == 0)
                return 2;
            else if (b == 128)
                return 26;
            else
                return 6;
        }
        else if (g == 128) {
            if (b == 0)
                return 25;
            else if (b == 128)
                return 20;
            else
                return 16;
        }
        else {
            if (b == 0)
                return 5;
            else if (b == 128)
                return 17;
            else
                return 1;
        }
    }
}

bool CodeCouleur::recevoirTramePresence() {
	CANMessage msg;
	if(can.read(msg)) {
		return msg.id == TRAME_PRESENCE_ID;
	}
	return false;
}

void CodeCouleur::envoyerTramePresence() {
	CANMessage msg(TRAME_PRESENCE_ID, CANStandard);
	can.write(msg);
}

void CodeCouleur::envoyerTrameCode(int codeCouleur) {
	CANMessage msg;
	msg.id = TRAME_COULEUR_ID;
	msg.len = 1;
	msg.data[0] = 0x01;
	msg.format = CANStandard;
	msg.type = CANData;
	can.write(msg);
}