#ifndef MISC_H
#define MISC_H

#include "types.h"

//Miscellaneous Hardware
//http://perfectkiosk.net/stsvb.html#misc_hardware


#ifndef __ASSEMBLER__
// Wait Control Register
#define WCR        ((vu16*)0x02000024)



#else

#define WCR        0x02000024




#endif



#endif