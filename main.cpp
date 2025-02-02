#include "mbed.h"
#include "CodeCouleur.hpp"
#include <cstdint>
#include <thread>
#include <chrono>
 
UnbufferedSerial pc(USBTX, USBRX, 9600);

FileHandle *mbed::mbed_override_console(int fd) {
    return &pc;
}

CodeCouleur codecouleur(PB_9, PB_8, PA_12, PA_11);

void envoiCouleur() {
	while(true) {
		codecouleur::envoyerTrameCode(codecouleur::CoderCouleur());
		std::this_thread::sleep_for(std::chrono::milliseconds(500));
	}
}

int main() {
    codeCouleur.Initialize();
	
	std::thread t(envoiCouleur);
	
    // Boucle infinie
    while (true) {
        if (codecouleur::recevoirTramePresence()) {
				codecouleur::envoyerTramePresence();
		}
    }
	
	return 0;
}