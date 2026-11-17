    # game pad interrupt
    .section .int_game_pad_interrupt, "ax"

    # timer zero interrupt
    .section .int_timer_zero_interrupt, "ax"
    add -4, sp
    st.w r1, 0[sp]
    movhi hi(Timer_Zero), r0, r1
    movea lo(Timer_Zero), r1, r1
    jmp [r1]

    # game pak interrupt
    .section .int_game_pak_interrupt, "ax"

    # communication interrupt
    .section .int_communication_interrupt, "ax"

    # VIP interrupt
    .section .int_vip_interrupt, "ax"
    add -4, sp
    st.w r1, 0[sp]
    movhi hi(VIP_Interrupt), r0, r1
    movea lo(VIP_Interrupt), r1, r1
    jmp [r1]

    # unused
    .section .int_unused1, "ax"

    # unused
    .section .int_unused2, "ax"

    # floating point exception
    .section .int_floating_point_exception, "ax"

    # unused
    .section .int_unused3, "ax"

    # zero division exception
    .section .int_zero_division_exception, "ax"

    # ;illegal opcode exception
    .section .int_illegal_opcode_exception, "ax"

    # trap < 16
    .section .int_trap_instruction_less, "ax"

    movhi hi(Reset), r0, r1
    movea lo(Reset), r1, r1
    jmp [r1]

    # trap instruction (vector ≥ 16)
    .section .int_trap_instruction_greater, "ax"

    # address trap
    .section .int_address_trap, "ax"

    # duplexed exception
    .section .int_duplexed_exception, "ax"

    # unused
    .section .int_unused4, "ax"

    # reset
    .section .int_reset, "ax"

    movhi hi(Reset), r0, r1
    movea lo(Reset), r1, r1
    jmp [r1]
