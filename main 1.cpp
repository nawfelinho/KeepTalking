#include "mbed.h"
#define FREQUENCY 20000
#define ENIGME_TRAM_ID 0x020 
#define ID_PRESENT 0x720
#define MASK 0x7FF
 
 
InterruptIn Nord(D4);
InterruptIn Sud(D7);
InterruptIn Est(D8);

 
DigitalOut led(LED1);
 
CAN can(PA_11,PA_12);

 
//CANMessage enigme(ENIGME_TRAM_ID, "01", 2, CANData, CANStandard);
CANMessage enigme{}; //(ENIGME_TRAM_ID, nullptr, 0, CANData, CANStandard);
 
void eni1();
void eni2();
void eni3();
// Volatile flag for ISR communication
volatile bool send_enigme = false;
volatile bool received = false;
 
void sendID(uint8_t ID){
    switch (ID) {
        case 1:
            enigme.id = ENIGME_TRAM_ID;
            enigme.len = 1;
            enigme.data[0] = 0x01;
            enigme.format = CANStandard;
            enigme.type = CANData;
            if(can.write(enigme)==1){
                printf("Send succes\n");
            }
            else{
                printf("Send Fail\n");
            } break;
        case 2:
            enigme.id = ENIGME_TRAM_ID;
            enigme.len = 1;
            enigme.data[0] = 0x02;
            enigme.format = CANStandard;
            enigme.type = CANData;
            if(can.write(enigme)==1){
                printf("Send succes\n");
            }
            else{
                printf("Send Fail\n");
            }
            break;
        case 3:
            enigme.id = ENIGME_TRAM_ID;
            enigme.len = 1;
            enigme.data[0] = 0x03;
            enigme.format = CANStandard;
            enigme.type = CANData;
            if(can.write(enigme)==1){
                printf("Send succes\n");
            }
            else{
                printf("Send Fail\n");
            }
            break;
        default:
            printf("error--wrong isr trigger");
            break;
    }
}
 
void onCanReceived() {
   received = true;
}
 
void init(){
    can.frequency(FREQUENCY);
    can.filter(ID_PRESENT, MASK, CANStandard);
    can.attach(&onCanReceived, CAN::RxIrq);
    Nord.fall(&eni1);
    Sud.fall(&eni2);
    Est.fall(&eni3);
}
 
// ISR-safe handler - just sets a flag
void eni1() {
    led = !led;
    send_enigme = 1;
}
void eni2() {
    led = !led;
    send_enigme = 2;
}
void eni3() {
    led = !led;
    send_enigme = 3;
}
 
int main()
{
    init();
 
    while (true) {
        // Handle the flag in main loop where it's safe
        if (send_enigme!=0) {
            sendID(1);
            send_enigme = false;
        }
        if(received==1){
            CANMessage msg{};
            
            if (can.read(msg)) {
                if (msg.id == ID_PRESENT) {
                    msg.id = ID_PRESENT;
                    msg.len = 0;
                    //enigme.data[0] = 0x03;
                    msg.format = CANStandard;
                    msg.type = CANData;
                printf("Trame reçue avec ID 0x%X : ", msg.id);
                can.write(msg);
                }
            }
            received = false;
        }
        ThisThread::sleep_for(100ms);
    }
}