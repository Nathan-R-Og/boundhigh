#include "types.h"

void ClearRam(u32* write_addr, u32 count, u32 write_value) {
    u32 i;
    for (i = 0; i < count; write_addr++, i++){
        *write_addr = write_value;
    }
}