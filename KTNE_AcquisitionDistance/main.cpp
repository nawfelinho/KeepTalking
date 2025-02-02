#include "mbed.h"
#include <cstdint>

Ticker ticker;
DigitalOut led1(LED1);
DigitalOut led2(LED2);
CAN can1(p9, p10);
char counter = 0;

uint16_t DistanceTemp = 0;
uint8_t Distance[2] = {0, 0};

void send() {
    if("ID trame ok")
    {

    }
    else
    {

    }
}

int main() {

    CapteurDistance CapteurDistance1();

    ticker.attach(&send, 1);

    while(1) {

        DistanceTemp = CapteurDistance1.getDistance();
        Distance[0] = DistanceTemp & 0x00FF;
        Distance[1] = (DistanceTemp >> 8) & 0x00FF;

        this_thread::sleep_for(100ms);
    }
}