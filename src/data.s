.section .rodata
.align 1
    # actual strings???
    .incbin "baserom.vb", 0x40000, 0x79C

.section .rodata2
.align 1

    .incbin "baserom.vb", 0x41000, 0x4c1b4-0x41000

    # し   ゛   ゅ    う   よ   う   ：
    # 2205 6905 2A05 4005 4705 4005 4407

    #0x4c1b4
.global gfx1
gfx1:
    .incbin "build/split/gfx1.2bpp"
    #0x541B4
    .incbin "baserom.vb", 0x541B4, 0x54764-0x541B4

    #0x54764
.global gfx2
gfx2:
    .incbin "build/split/gfx2.2bpp"
    #0x5C764
    .incbin "baserom.vb", 0x5C764, 0x5f518-0x5C764

    #0x5f518
.global bios_important_tiles
bios_important_tiles:
    .incbin "split/bios_important_tiles.bin"
.global bios_important_tiles_load
bios_important_tiles_load:
    .word bios_important_tiles

    #0x5ff9c
.global bios_logo_tiles
bios_logo_tiles:
    .incbin "split/bios_logo_tiles.bin"
    .word 0x07C107C0
    #0x60A20
    .incbin "baserom.vb", 0x60A20, 0x6cdb0-0x60A20

    #0x6cdb0
.global gfx3
gfx3:
    .incbin "build/split/gfx3.2bpp"
    #0x74db0
    .incbin "baserom.vb", 0x74db0, 0x76cdc-0x74db0

    #0x76cdc
.global gfx4
gfx4:
    .incbin "build/split/gfx4.2bpp"
    #0x7ECDC
    .incbin "baserom.vb", 0x7ECDC, 0x8476c-0x7ECDC

    #0x8476c
.global gfx5
gfx5:
    .incbin "build/split/gfx5.2bpp"
    #0x8C76c
    .incbin "baserom.vb", 0x8C76c, 0x93948-0x8C76c

    #0x93948
.global gfx6
gfx6:
    .incbin "build/split/gfx6.2bpp"
    #0xa3948
    .incbin "baserom.vb", 0xa3948, 0xa7dac-0xa3948

    #0xa7dac
.global gfx8
gfx8:
    .incbin "build/split/gfx8.2bpp"
    #0xB7DAC
    .incbin "baserom.vb", 0xB7DAC, 0xb98b8-0xB7DAC

    #0xb98b8
.global bios_gfx
bios_gfx:
    .incbin "build/split/bios_gfx.2bpp"
    #0xBA0B8
.global bios_gfx_end
bios_gfx_end:
    .incbin "baserom.vb", 0xBA0B8, 0xC2250-0xBA0B8

    #0xC2250
.global gfx10
gfx10:
    .incbin "build/split/gfx10.2bpp"
    #0x142250


    .incbin "baserom.vb", 0x142250, 0x15bf00-0x142250
