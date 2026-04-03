---
id: github.com-dtrupenn-tetris-954961ee-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:45.329642
---

# KNOWLEDGE EXTRACT: github.com_dtrupenn_Tetris_954961ee
> **Extracted on:** 2026-04-01 09:28:24
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007520197/github.com_dtrupenn_Tetris_954961ee

---

## File: `README`
```
Instructions:
Run Pennsim in double buffer mode and then run tetris script by inputing to the Pennsim command prompt (script tetris_script.txt). For a guide on how to use PennSim go to: http://www.cis.upenn.edu/~milom/cse240-Fall06/pennsim/pennsim-guide.html
```

## File: `lc4libc.h`
```c
/*
 * lc4libc.h
 */

typedef int lc4int; 
typedef unsigned int lc4uint;
typedef char lc4char;

#define TRUE  1
#define FALSE 0

#define NULL (void*)0

#define BLACK  0x0000U
#define WHITE  0xFFFFU
#define YELLOW 0x7FF0U
#define RED    0x7C00U
#define ORANGE 0xF600U
#define BLUE   0x0033U
#define GREEN  0x3300U
#define CYAN   0x0770U

lc4uint lc4_rand_power2(lc4uint max);
void lc4_utoa(lc4uint u, lc4char *str, lc4uint size);

void lc4_draw_8x8(lc4int x, lc4int y, lc4uint color);
void lc4_draw_1(lc4int x, lc4int y, lc4uint color);
void lc4_draw_4x4_wrapped(lc4int x, lc4int y, lc4uint color, lc4uint bmp);
lc4int lc4_get_event();
void lc4_puts(lc4uint *str);

void lc4_halt();
void lc4_reset_vmem();
void lc4_blt_vmem();
```

## File: `libc.asm`
```
USER_STACK_ADDR .UCONST x7FFF
USER_STACK_SIZE .UCONST x1000
USER_HEAP_SIZE .UCONST x3000	
;;; Reserve space for heap and stack so that assembler will not try to
;;; place data in these regions
	
.DATA
.ADDR x4000
USER_HEAP	.BLKW x3000
.ADDR x7000			
USER_STACK	.BLKW x1000

.CODE
.ADDR x0000	
.FALIGN
__start
	LC R6, USER_STACK_ADDR	; Init the Stack Pointer
	LEA R7, main		; Invoke the main routine
	JSRR R7
	TRAP x25		; HALT

;;; Wrappers for the traps.  Marshall the arguments from stack to 
;;; registers and return value from register to stack

	
.FALIGN		
lc4_draw_8x8
	;; prologue
	ADD R6, R6, #-2	
	STR R5, R6, #0
	STR R7, R6, #1
	;; marshall arguments
	LDR R0, R6, #2
	LDR R1, R6, #3
	LDR R2, R6, #4
	TRAP x3F
	;; epilogue
	LDR R7, R6, #1
	LDR R5, R6, #0
	ADD R6, R6, #2
	RET

.FALIGN		
lc4_draw_1
	;; prologue
	ADD R6, R6, #-2	
	STR R5, R6, #0
	STR R7, R6, #1
	;; marshall arguments
	LDR R0, R6, #2
	LDR R1, R6, #3
	LDR R2, R6, #4
	TRAP x40
	;; epilogue
	LDR R7, R6, #1
	LDR R5, R6, #0
	ADD R6, R6, #2
	RET

.FALIGN	
lc4_draw_4x4_wrapped
	;; prologue
	ADD R6, R6, #-2	
	STR R5, R6, #0
	STR R7, R6, #1
	;; marshall arguments
	LDR R0, R6, #2
	LDR R1, R6, #3
	LDR R2, R6, #4
	LDR R3, R6, #5
	TRAP x42
	;; epilogue
	LDR R7, R6, #1
	LDR R5, R6, #0
	ADD R6, R6, #2
	RET

.FALIGN
lc4_puts
	;; prologue
	ADD R6, R6, #-2
	STR R5, R6, #0
	STR R7, R6, #1
	;; marshall arguments
	LDR R0, R6, #2
	TRAP x60
	;; epilogue
	LDR R7, R6, #1
	LDR R5, R6, #0
	ADD R6, R6, #2
	RET
	
.FALIGN
lc4_get_event 
	;; R5 is the base pointer as well as the 
	;; TRAP return register.  If the trap returns
	;; a value, we have to save and restore the user's
	;; base-pointer
	ADD R6, R6, #-2	
	STR R5, R6, #0
	STR R7, R6, #1
	TRAP x50
	LDR R7, R6, #1
	;; save TRAP return value on stack
	STR R5, R6, #1
	;; restore user base-pointer
	LDR R5, R6, #0
	ADD R6, R6, #2
	RET

.FALIGN	
lc4_halt
	;; prologue
	ADD R6, R6, #-2
	LDR R5, R6, #0
	STR R7, R6, #1
	;; no arguments
	TRAP x25
	;; epilogue
	LDR R7, R6, #1
	LDR R5, R6, #0
	ADD R6, R6, #2
	RET			

void .FALIGN
lc4_reset_vmem
	;; prologue
	ADD R6, R6, #-2
	STR R5, R6, #0
	STR R7, R6, #1
	;; no arguments
	TRAP x4E
	;; epilogue
	LDR R5, R6, #0
	LDR R7, R6, #1
	ADD R6, R6, #2
	RET

.FALIGN
lc4_blt_vmem
	;; prologue
	ADD R6, R6, #-2
	STR R5, R6, #0
	STR R7, R6, #1
	;; no arguments
	TRAP x4F
	;; epilogue
	LDR R5, R6, #0
	LDR R7, R6, #1
	ADD R6, R6, #2
	RET

;;; Other library data will start at x2000
.DATA
.ADDR x2000
		.DATA
L2_lc4libc 		.FILL #17767
		.FILL #9158
		.FILL #39017
		.FILL #18547
		.FILL #56401
		.FILL #23807
		.FILL #37962
		.FILL #22764
		.FILL #7977
		.FILL #31949
		.FILL #22714
		.FILL #55211
		.FILL #16882
		.FILL #7931
		.FILL #43491
		.FILL #57670
		.FILL #124
		.FILL #25282
		.FILL #2132
		.FILL #10232
		.FILL #8987
		.FILL #59880
		.FILL #52711
		.FILL #17293
		.FILL #3958
		.FILL #9562
		.FILL #63790
		.FILL #29283
		.FILL #49715
		.FILL #55199
		.FILL #50377
		.FILL #1946
		.FILL #64358
		.FILL #23858
		.FILL #20493
		.FILL #55223
		.FILL #47665
		.FILL #58456
		.FILL #12451
		.FILL #55642
		.FILL #24869
		.FILL #35165
		.FILL #45317
		.FILL #41751
		.FILL #43096
		.FILL #23273
		.FILL #33886
		.FILL #43220
		.FILL #48555
		.FILL #36018
		.FILL #53453
		.FILL #57542
		.FILL #30363
		.FILL #40628
		.FILL #9300
		.FILL #34321
		.FILL #50190
		.FILL #7554
		.FILL #63604
		.FILL #34369
		.FILL #62753
		.FILL #48445
		.FILL #36316
		.FILL #61575
		.FILL #6768
		.FILL #56809
		.FILL #51262
		.FILL #54433
		.FILL #49729
		.FILL #63713
		.FILL #44540
		.FILL #9063
		.FILL #33342
		.FILL #24321
		.FILL #50814
		.FILL #10903
		.FILL #47594
		.FILL #19164
		.FILL #54123
		.FILL #30614
		.FILL #55183
		.FILL #42040
		.FILL #22620
		.FILL #20010
		.FILL #17132
		.FILL #31920
		.FILL #54331
		.FILL #1787
		.FILL #39474
		.FILL #52399
		.FILL #36156
		.FILL #36692
		.FILL #35308
		.FILL #6936
		.FILL #32731
		.FILL #42076
		.FILL #63746
		.FILL #18458
		.FILL #30974
		.FILL #47939
		.FILL #16635
		.FILL #9978
		.FILL #57002
		.FILL #49978
		.FILL #34299
		.FILL #42281
		.FILL #60881
		.FILL #16358
		.FILL #61445
		.FILL #49468
		.FILL #46972
		.FILL #51092
		.FILL #25973
		.FILL #4056
		.FILL #5566
		.FILL #43105
		.FILL #35977
		.FILL #59897
		.FILL #44892
		.FILL #9915
		.FILL #46760
		.FILL #15513
		.FILL #46607
		.FILL #16533
		.FILL #22449
		.FILL #13803
		.FILL #58609
		.FILL #20659
		.FILL #32261
		.FILL #24047
		.FILL #3063
		.FILL #48896
		.FILL #34025
		.FILL #60065
		.FILL #33338
		.FILL #2789
		.FILL #36810
		.FILL #28683
		.FILL #19147
		.FILL #32720
		.FILL #12616
		.FILL #583
		.FILL #18276
		.FILL #38589
		.FILL #4639
		.FILL #23843
		.FILL #16158
		.FILL #40616
		.FILL #18204
		.FILL #61051
		.FILL #50532
		.FILL #64965
		.FILL #11028
		.FILL #31603
		.FILL #15962
		.FILL #33477
		.FILL #45406
		.FILL #9035
		.FILL #54137
		.FILL #12131
		.FILL #33083
		.FILL #57200
		.FILL #61028
		.FILL #1572
		.FILL #51729
		.FILL #28830
		.FILL #4361
		.FILL #23004
		.FILL #57514
		.FILL #23508
		.FILL #55724
		.FILL #4594
		.FILL #24091
		.FILL #8464
		.FILL #43183
		.FILL #28731
		.FILL #32307
		.FILL #59341
		.FILL #3811
		.FILL #50512
		.FILL #54856
		.FILL #54343
		.FILL #49941
		.FILL #348
		.FILL #20411
		.FILL #367
		.FILL #33826
		.FILL #281
		.FILL #9402
		.FILL #22427
		.FILL #12413
		.FILL #42485
		.FILL #14091
		.FILL #7905
		.FILL #44058
		.FILL #284
		.FILL #36735
		.FILL #48419
		.FILL #23288
		.FILL #28713
		.FILL #6392
		.FILL #13476
		.FILL #33307
		.FILL #30483
		.FILL #21941
		.FILL #10954
		.FILL #59214
		.FILL #54248
		.FILL #4760
		.FILL #63026
		.FILL #39224
		.FILL #59616
		.FILL #51833
		.FILL #23629
		.FILL #59965
		.FILL #6708
		.FILL #23996
		.FILL #28255
		.FILL #6990
		.FILL #33399
		.FILL #50682
		.FILL #19403
		.FILL #10348
		.FILL #64773
		.FILL #27308
		.FILL #54406
		.FILL #65057
		.FILL #64043
		.FILL #37290
		.FILL #22810
		.FILL #27221
		.FILL #43682
		.FILL #36286
		.FILL #60528
		.FILL #8629
		.FILL #58227
		.FILL #5947
		.FILL #2308
		.FILL #46940
		.FILL #10707
		.FILL #65334
		.FILL #20628
		.FILL #4787
		.FILL #51631
		.FILL #44258
		.FILL #64752
		.FILL #58340
		.FILL #2718
		.FILL #27471
		.FILL #65330
		.FILL #36117
		.FILL #12617
		.FILL #19197
		.FILL #46466
		.FILL #11854
		.FILL #46505
		.DATA
L3_lc4libc 		.FILL #0
;;;;;;;;;;;;;;;;;;;;;;;;;;;;lc4_rand_power2;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		.CODE
		.FALIGN
lc4_rand_power2
	;; prologue
	STR R7, R6, #-2	;; save return address
	STR R5, R6, #-3	;; save base pointer
	ADD R6, R6, #-3
	ADD R5, R6, #0
	ADD R6, R6, #-1	;; allocate stack space for local variables
	;; function body
	LDR R7, R5, #3
	ADD R3, R7, #-1
	LEA R2, L3_lc4libc
	LDR R2, R2, #0
	LEA R1, L2_lc4libc
	ADD R2, R2, R1
	LDR R2, R2, #0
	AND R2, R2, R3
	ADD R7, R2, R7
	AND R7, R7, R3
	STR R7, R5, #-1
	LEA R7, L3_lc4libc
	LDR R3, R7, #0
	ADD R3, R3, #1
	CONST R2, #255
	AND R3, R3, R2
	STR R3, R7, #0
	LDR R7, R5, #-1
L1_lc4libc
	;; epilogue
	ADD R6, R5, #0	;; pop locals off stack
	ADD R6, R6, #3	;; free space for return address, base pointer, and return value
	STR R7, R6, #-1	;; store return value
	LDR R5, R6, #-3	;; restore base pointer
	LDR R7, R6, #-2	;; restore return address
	RET

;;;;;;;;;;;;;;;;;;;;;;;;;;;;lc4_utoa;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		.CODE
		.FALIGN
lc4_utoa
	;; prologue
	STR R7, R6, #-2	;; save return address
	STR R5, R6, #-3	;; save base pointer
	ADD R6, R6, #-3
	ADD R5, R6, #0
	ADD R6, R6, #-3	;; allocate stack space for local variables
	;; function body
	CONST R7, #0
	STR R7, R5, #-2
	LDR R7, R5, #5
	CONST R3, #6
	CMPU R7, R3
	BRzp L5_lc4libc
	JMP L4_lc4libc
L5_lc4libc
	CONST R7, #16
	HICONST R7, #39
	STR R7, R5, #-1
	JMP L10_lc4libc
L7_lc4libc
	LDR R7, R5, #3
	LDR R3, R5, #-1
	DIV R7, R7, R3
	STR R7, R5, #-3
	LDR R7, R5, #-3
	CONST R3, #0
	CMP R7, R3
	BRnp L13_lc4libc
	LDR R7, R5, #-2
	CONST R3, #0
	CMP R7, R3
	BRz L11_lc4libc
L13_lc4libc
	LDR R7, R5, #4
	LDR R3, R5, #-3
	CONST R2, #48
	ADD R3, R3, R2
	STR R3, R7, #0
	LDR R7, R5, #4
	ADD R7, R7, #1
	STR R7, R5, #4
	LDR R7, R5, #3
	LDR R3, R5, #-3
	LDR R2, R5, #-1
	MUL R3, R3, R2
	SUB R7, R7, R3
	STR R7, R5, #3
	CONST R7, #1
	STR R7, R5, #-2
L11_lc4libc
L8_lc4libc
	LDR R7, R5, #-1
	CONST R3, #10
	DIV R7, R7, R3
	STR R7, R5, #-1
L10_lc4libc
	LDR R7, R5, #-1
	CONST R3, #0
	CMP R7, R3
	BRnp L7_lc4libc
	LDR R7, R5, #4
	CONST R3, #0
	STR R3, R7, #0
L4_lc4libc
	;; epilogue
	ADD R6, R5, #0	;; pop locals off stack
	ADD R6, R6, #3	;; free space for return address, base pointer, and return value
	STR R7, R6, #-1	;; store return value
	LDR R5, R6, #-3	;; restore base pointer
	LDR R7, R6, #-2	;; restore return address
	RET

```

## File: `os.asm`
```
;;; This version of os.asm by Amir Roth ammended by CJT 8.11.10 and again 4.11.11
		.OS
		.CODE
		.ADDR x8000
; the TRAP vector table
	JMP BAD_TRAP	; x00
	JMP BAD_TRAP	; x01
	JMP BAD_TRAP	; x02
	JMP BAD_TRAP	; x03
	JMP BAD_TRAP	; x04
	JMP BAD_TRAP	; x05
	JMP BAD_TRAP	; x06
	JMP BAD_TRAP	; x07
	JMP BAD_TRAP	; x08
	JMP BAD_TRAP	; x09
	JMP BAD_TRAP	; x0A
	JMP BAD_TRAP	; x0B
	JMP BAD_TRAP	; x0C
	JMP BAD_TRAP	; x0D
	JMP BAD_TRAP	; x0E
	JMP BAD_TRAP	; x0F
	JMP BAD_TRAP	; x10
	JMP BAD_TRAP	; x11
	JMP BAD_TRAP	; x12
	JMP BAD_TRAP	; x13
	JMP BAD_TRAP	; x14
	JMP BAD_TRAP	; x15
	JMP BAD_TRAP	; x16
	JMP BAD_TRAP	; x17
	JMP BAD_TRAP	; x18
	JMP BAD_TRAP	; x19
	JMP BAD_TRAP	; x1A
	JMP BAD_TRAP	; x1B
	JMP BAD_TRAP	; x1C
	JMP BAD_TRAP	; x1D
	JMP BAD_TRAP	; x1E
	JMP BAD_TRAP	; x1F
	JMP BAD_TRAP	; x20
	JMP BAD_TRAP	; x21
	JMP BAD_TRAP	; x22
	JMP BAD_TRAP	; x23
	JMP BAD_TRAP	; x24
	JMP TRAP_HALT	; x25
	JMP BAD_TRAP	; x26
	JMP BAD_TRAP	; x27
	JMP BAD_TRAP	; x28
	JMP BAD_TRAP	; x29
	JMP BAD_TRAP	; x2A
	JMP BAD_TRAP	; x2B
	JMP BAD_TRAP	; x2C
	JMP BAD_TRAP	; x2D
	JMP BAD_TRAP	; x2E
	JMP BAD_TRAP	; x2F
	JMP BAD_TRAP	; x30
	JMP BAD_TRAP	; x31
	JMP BAD_TRAP	; x32
	JMP BAD_TRAP	; x33
	JMP BAD_TRAP	; x34
	JMP BAD_TRAP	; x35
	JMP BAD_TRAP	; x36
	JMP BAD_TRAP	; x37
	JMP BAD_TRAP	; x38
	JMP BAD_TRAP	; x39
	JMP BAD_TRAP	; x3A
	JMP BAD_TRAP	; x3B
	JMP BAD_TRAP	; x3C
	JMP BAD_TRAP	; x3D
	JMP BAD_TRAP	; x3E
	JMP TRAP_DRAW_8x8 ; x3F
	JMP TRAP_DRAW_1 ; x40
	JMP BAD_TRAP
	JMP TRAP_DRAW_4X4W; x42
	JMP BAD_TRAP	; x43
	JMP BAD_TRAP	; x44
	JMP BAD_TRAP	; x45
	JMP BAD_TRAP	; x46
	JMP BAD_TRAP	; x47
	JMP BAD_TRAP	; x48
	JMP BAD_TRAP	; x49
	JMP BAD_TRAP	; x4A
	JMP BAD_TRAP	; x4B
	JMP BAD_TRAP	; x4C
	JMP BAD_TRAP	; x4D
	JMP TRAP_RESET_VMEM; x4E
	JMP TRAP_BLT_VMEM; x4F
	JMP TRAP_GET_EVENT; x50
	JMP BAD_TRAP	; x51
	JMP BAD_TRAP	; x52
	JMP BAD_TRAP	; x53
	JMP BAD_TRAP	; x54
	JMP BAD_TRAP	; x55
	JMP BAD_TRAP	; x56
	JMP BAD_TRAP	; x57
	JMP BAD_TRAP	; x58
	JMP BAD_TRAP	; x59
	JMP BAD_TRAP	; x5A
	JMP BAD_TRAP	; x5B
	JMP BAD_TRAP	; x5C
	JMP BAD_TRAP	; x5D
	JMP BAD_TRAP	; x5E
	JMP BAD_TRAP	; x5F
	JMP TRAP_PUTS	; x60
	JMP BAD_TRAP	; x61
	JMP BAD_TRAP	; x62
	JMP BAD_TRAP	; x63
	JMP BAD_TRAP	; x64
	JMP BAD_TRAP	; x65
	JMP BAD_TRAP	; x66
	JMP BAD_TRAP	; x67
	JMP BAD_TRAP	; x68
	JMP BAD_TRAP	; x69
	JMP BAD_TRAP	; x6A
	JMP BAD_TRAP	; x6B
	JMP BAD_TRAP	; x6C
	JMP BAD_TRAP	; x6D
	JMP BAD_TRAP	; x6E
	JMP BAD_TRAP	; x6F
	JMP BAD_TRAP	; x70
	JMP BAD_TRAP	; x71
	JMP BAD_TRAP	; x72
	JMP BAD_TRAP	; x73
	JMP BAD_TRAP	; x74
	JMP BAD_TRAP	; x75
	JMP BAD_TRAP	; x76
	JMP BAD_TRAP	; x77
	JMP BAD_TRAP	; x78
	JMP BAD_TRAP	; x79
	JMP BAD_TRAP	; x7A
	JMP BAD_TRAP	; x7B
	JMP BAD_TRAP	; x7C
	JMP BAD_TRAP	; x7D
	JMP BAD_TRAP	; x7E
	JMP BAD_TRAP	; x7F
	JMP BAD_TRAP	; x80
	JMP BAD_TRAP	; x81
	JMP BAD_TRAP	; x82
	JMP BAD_TRAP	; x83
	JMP BAD_TRAP	; x84
	JMP BAD_TRAP	; x85
	JMP BAD_TRAP	; x86
	JMP BAD_TRAP	; x87
	JMP BAD_TRAP	; x88
	JMP BAD_TRAP	; x89
	JMP BAD_TRAP	; x8A
	JMP BAD_TRAP	; x8B
	JMP BAD_TRAP	; x8C
	JMP BAD_TRAP	; x8D
	JMP BAD_TRAP	; x8E
	JMP BAD_TRAP	; x8F
	JMP BAD_TRAP	; x90
	JMP BAD_TRAP	; x91
	JMP BAD_TRAP	; x92
	JMP BAD_TRAP	; x93
	JMP BAD_TRAP	; x94
	JMP BAD_TRAP	; x95
	JMP BAD_TRAP	; x96
	JMP BAD_TRAP	; x97
	JMP BAD_TRAP	; x98
	JMP BAD_TRAP	; x99
	JMP BAD_TRAP	; x9A
	JMP BAD_TRAP	; x9B
	JMP BAD_TRAP	; x9C
	JMP BAD_TRAP	; x9D
	JMP BAD_TRAP	; x9E
	JMP BAD_TRAP	; x9F
	JMP BAD_TRAP	; xA0
	JMP BAD_TRAP	; xA1
	JMP BAD_TRAP	; xA2
	JMP BAD_TRAP	; xA3
	JMP BAD_TRAP	; xA4
	JMP BAD_TRAP	; xA5
	JMP BAD_TRAP	; xA6
	JMP BAD_TRAP	; xA7
	JMP BAD_TRAP	; xA8
	JMP BAD_TRAP	; xA9
	JMP BAD_TRAP	; xAA
	JMP BAD_TRAP	; xAB
	JMP BAD_TRAP	; xAC
	JMP BAD_TRAP	; xAD
	JMP BAD_TRAP	; xAE
	JMP BAD_TRAP	; xAF
	JMP BAD_TRAP	; xB0
	JMP BAD_TRAP	; xB1
	JMP BAD_TRAP	; xB2
	JMP BAD_TRAP	; xB3
	JMP BAD_TRAP	; xB4
	JMP BAD_TRAP	; xB5
	JMP BAD_TRAP	; xB6
	JMP BAD_TRAP	; xB7
	JMP BAD_TRAP	; xB8
	JMP BAD_TRAP	; xB9
	JMP BAD_TRAP	; xBA
	JMP BAD_TRAP	; xBB
	JMP BAD_TRAP	; xBC
	JMP BAD_TRAP	; xBD
	JMP BAD_TRAP	; xBE
	JMP BAD_TRAP	; xBF
	JMP BAD_TRAP	; xC0
	JMP BAD_TRAP	; xC1
	JMP BAD_TRAP	; xC2
	JMP BAD_TRAP	; xC3
	JMP BAD_TRAP	; xC4
	JMP BAD_TRAP	; xC5
	JMP BAD_TRAP	; xC6
	JMP BAD_TRAP	; xC7
	JMP BAD_TRAP	; xC8
	JMP BAD_TRAP	; xC9
	JMP BAD_TRAP	; xCA
	JMP BAD_TRAP	; xCB
	JMP BAD_TRAP	; xCC
	JMP BAD_TRAP	; xCD
	JMP BAD_TRAP	; xCE
	JMP BAD_TRAP	; xCF
	JMP BAD_TRAP	; xD0
	JMP BAD_TRAP	; xD1
	JMP BAD_TRAP	; xD2
	JMP BAD_TRAP	; xD3
	JMP BAD_TRAP	; xD4
	JMP BAD_TRAP	; xD5
	JMP BAD_TRAP	; xD6
	JMP BAD_TRAP	; xD7
	JMP BAD_TRAP	; xD8
	JMP BAD_TRAP	; xD9
	JMP BAD_TRAP	; xDA
	JMP BAD_TRAP	; xDB
	JMP BAD_TRAP	; xDC
	JMP BAD_TRAP	; xDD
	JMP BAD_TRAP	; xDE
	JMP BAD_TRAP	; xDF
	JMP BAD_TRAP	; xE0
	JMP BAD_TRAP	; xE1
	JMP BAD_TRAP	; xE2
	JMP BAD_TRAP	; xE3
	JMP BAD_TRAP	; xE4
	JMP BAD_TRAP	; xE5
	JMP BAD_TRAP	; xE6
	JMP BAD_TRAP	; xE7
	JMP BAD_TRAP	; xE8
	JMP BAD_TRAP	; xE9
	JMP BAD_TRAP	; xEA
	JMP BAD_TRAP	; xEB
	JMP BAD_TRAP	; xEC
	JMP BAD_TRAP	; xED
	JMP BAD_TRAP	; xEE
	JMP BAD_TRAP	; xEF
	JMP BAD_TRAP	; xF0
	JMP BAD_TRAP	; xF1
	JMP BAD_TRAP	; xF2
	JMP BAD_TRAP	; xF3
	JMP BAD_TRAP	; xF4
	JMP BAD_TRAP	; xF5
	JMP BAD_TRAP	; xF6
	JMP BAD_TRAP	; xF7
	JMP BAD_TRAP	; xF8
	JMP BAD_TRAP	; xF9
	JMP BAD_TRAP	; xFA
	JMP BAD_TRAP	; xFB
	JMP BAD_TRAP	; xFC
	JMP BAD_TRAP	; xFD
	JMP BAD_TRAP	; xFE
	JMP BAD_TRAP	; xFF

;;; OS_START - operating system entry point (always starts at x8200)

		.CODE
		.ADDR x8200
OS_START
	;; initialize timer
	LC R0, TIM_INIT
	LC R1, OS_TIR_ADDR
	STR R0, R1, #0

	;; R7 <- User code address (x0000)
	LC R7, USER_CODE_ADDR 
	RTI			; RTI removes the privilege bit

;;; OS memory address constants
USER_CODE_ADDR 	.UCONST x0000
OS_CODE_ADDR 	.UCONST x8000
		
OS_STACK_ADDR 	.UCONST xBFFF
OS_VIDEO_ADDR 	.UCONST xC000
				
OS_KBSR_ADDR	.UCONST xFE00		; keyboard status register
OS_KBDR_ADDR	.UCONST xFE02		; keyboard data register
OS_ADSR_ADDR	.UCONST xFE04		; display status register
OS_ADDR_ADDR	.UCONST xFE06		; display data register
OS_TSR_ADDR	.UCONST xFE08		; timer register
OS_TIR_ADDR	.UCONST xFE0A		; timer interval register
OS_VDCR_ADDR	.UCONST xFE0C	        ; video display control register
OS_MCR_ADDR	.UCONST xFFEE		; machine control register

TIM_INIT 	.UCONST #200		; Timer Interval in milliseconds

MASK_L15 	.UCONST x7FFF
MASK_H4		.UCONST xF000
			
.DATA
.ADDR xC000	
OS_VIDEO_MEM .BLKW x3E00

OS_VIDEO_NUM_COLS .UCONST #128
OS_VIDEO_NUM_ROWS .UCONST #124		
	
;;; TRAP_HALP - trap handler for halting machine

;;; BAD_TRAP - code to execute for undefined trap
.CODE
BAD_TRAP
	JMP TRAP_HALT	; execute HALT

;;; TRAP_HALT - halts the program and jumps to OS_START
.CODE
TRAP_HALT	
	; clear run bit in MCR
	LC R3, OS_MCR_ADDR
	LDR R0, R3, #0
	LC R1, MASK_L15
	AND R0,R0,R1
	STR R0, R3, #0
	JMP OS_START 	; restart machine

	
.CODE
;;; TRAP_DRAW_8x8
;;; Input
;;;   r0 - video column (left)
;;;   r1 - video row (upper) 
;;;   r2 - color
;;; Output
;;;   video memory will be updated to place block of approriate color
TRAP_DRAW_8x8
	LC R4, OS_STACK_ADDR	; OS stack pointer (x7FFF) -> R4
	STR R6, R4, #0		; save USER stack pointer
	ADD R6, R4, #0		; begin using general stack pointer (R6) here

;;; Register allocation
;;;  r3 - loop counter
;;;  r4 - address in video memory
;;;  r5 - scratch variable
	

	LEA R4, OS_VIDEO_MEM
	LC  R5, OS_VIDEO_NUM_COLS
	MUL R5, R5, R1		; Multiply row by 128 (VIDEO_COL_NUM)
	ADD R5, R5, R0		; Add col
	ADD R4, R4, R5		; Add to base address

	LC  R5, OS_VIDEO_NUM_COLS ; This value is used to increment the address on each iteration

	CONST R3, 0		; i = 0
	JMP TEST

;;;  Note the loop unrolling to fill in 8 entries on each row
LOOP	STR R2, R4, #0
	STR R2, R4, #1
	STR R2, R4, #2
	STR R2, R4, #3

	STR R2, R4, #4
	STR R2, R4, #5
	STR R2, R4, #6
	STR R2, R4, #7

	ADD R4, R4, R5		; Update the address by adding OS_VIDEO_NUM_COLS
	ADD R3, R3, #1		; Increment the loop counter

TEST	CMPI R3, #8
	BRn LOOP

;;; If you initialized the loop counter to 8 and decremented on each iteration you could eliminate the CMPI
;;;  and just do a BRp test since JMP doesn't change the NZP

	LDR R6, R6, #0		; Restore user stack pointer

	RTI 

.CODE
;;; TRAP_DRAW_1
;;; Input
;;;   r0 - video column (left)
;;;   r1 - video row (upper) 
;;;   r2 - color
;;; Output
;;;   video memory will be updated to place block of approriate color
TRAP_DRAW_1
	LC R4, OS_STACK_ADDR	; OS stack pointer (x7FFF) -> R4
	STR R6, R4, #0		; save USER stack pointer
	ADD R6, R4, #0		; begin using general stack pointer (R6) here

	LC R5, OS_VIDEO_NUM_COLS
	MUL R5, R1, R5		; Multiply row by 128 (VIDEO_COL_NUM)
	ADD R5, R5, R0		; Add col
	LEA R4, OS_VIDEO_MEM
	ADD R5, R5, R4		; Add video mem begin
	STR R2, R5, #0
	
	LDR R6, R6, #0
	RTI 

;;; TRAP_DRAW_4X4W - draws with 4x4 bitmap with screen "wraparound",
;;; i.e., if part of the bitmap is "off the screen" it wraps around to
;;; the other side of the screen.
;;; Input
;;;   r0 - video column (left)
;;;   r1 - video row (upper) 
;;;   r2 - color
;;;   r3 - bitmap
;;; Output
;;;   video memory will be updated to place block of approriate color
.CODE
TRAP_DRAW_4x4W
	LC R4, OS_STACK_ADDR	; OS stack pointer (x7FFF) -> R4
	STR R6, R4, #0		; save USER stack pointer
	ADD R6, R4, #0		; begin using general stack pointer (R6) here

	;; need to save some registers because we need a lot of temporaries
	STR R7, R6, #-1
	STR R0, R6, #-2
	STR R1, R6, #-3

	;; R7 is i
	CONST R7, #0
D4X4W_ROW_LOOP
	CMPI R7, #4
	BRzp D4X4W_ROW_LOOP_EXIT

	LC R4, MASK_H4
	AND R4, R3, R4
	BRnp D4X4W_DO_ROW
	SLL R3, R3, #4
	JMP D4X4W_ROW_LOOP_IND
D4X4W_DO_ROW	
	;; R5 is j
	CONST R5, #0
D4X4W_COL_LOOP
	CMPI R5, #4
	BRzp D4X4W_COL_LOOP_EXIT
	
	CMPI R3, #0
	BRzp D4X4W_SKIP_PIXEL

	;; compute post-mod y
	LDR R1, R6, #-3
	ADD R1, R7, R1
	LC R4, OS_VIDEO_NUM_ROWS
	ADD R1, R1, R4
	MOD R1, R1, R4
	;; scale y by number of columns
	LC R4, OS_VIDEO_NUM_COLS
	MUL R1, R1, R4

	;; compute post-mod x
	LDR R0, R6, #-2
	ADD R0, R5, R0
	ADD R0, R0, R4
	MOD R0, R0, R4

	ADD R0, R0, R1
	LEA R4, OS_VIDEO_MEM
	ADD R4, R0, R4
	STR R2, R4, #0
D4X4W_SKIP_PIXEL
	
	SLL R3, R3, #1
	ADD R5, R5, #1
	JMP D4X4W_COL_LOOP
D4X4W_COL_LOOP_EXIT

D4X4W_ROW_LOOP_IND	
	ADD R7, R7, #1
	JMP D4X4W_ROW_LOOP
D4X4W_ROW_LOOP_EXIT		
	;; epilogue
	LDR R1, R6, #-3
	LDR R0, R6, #-2
	LDR R7, R6, #-1
	LDR R6, R6, #0		; Restore user stack pointer
	RTI 
	
;;; TRAP_GET_EVENT - for getting a keyboard or timer event
;;; Input
;;;   none
;;; Output
;;;   r5 - an integer indicating what event has happened
;;;        0 (timer) 
;;;        non-0 (keyboard character)

.CODE
TRAP_GET_EVENT			
	LC R4, OS_STACK_ADDR	; OS stack pointer (x7FFF) -> R4
	STR R6, R4, #0		; save USER stack pointer
	ADD R6, R4, #0		; begin using general stack pointer (R6) here

	;; no need to save anything (or even switch stacks really)

GE_LOOP
	LC R0, OS_KBSR_ADDR
	LDR R0, R0, #0
	BRz GE_CHK_TIMER	; If status = 0 (unchanged) check timer
	LC R0, OS_KBDR_ADDR	; else load the character
	LDR R5, R0, #0
	JMP GE_EXIT

GE_CHK_TIMER			; Check timer register MSB
	LC R0, OS_TSR_ADDR
	LDR R0, R0, #0
	BRz GE_LOOP		; If not on (TR=0) 
	CONST R5, #0

GE_EXIT
	LDR R6, R6, #0		; Restore user stack pointer
	RTI

;;; TRAP_RESET_VMEM - In double-buffered video mode, resets the video
;;; display, i.e., turns it to black.
;;; Inputs - none
;;; Outputs - none
.CODE
TRAP_RESET_VMEM
	LC R4, OS_VDCR_ADDR
	CONST R5, #1
	STR R5, R4, #0
	RTI

;;; TRAP_BLT_VMEM - In double-buffered video mode, copies the contents
;;; of video memory to the video display.
;;; Inputs - none
;;; Outputs - none
		.CODE
TRAP_BLT_VMEM
	LC R4, OS_VDCR_ADDR
	CONST R5, #2
	STR R5, R4, #0
	RTI
	
		.CODE
TRAP_PUTS
	LC R4, OS_STACK_ADDR	; OS stack pointer (x7FFF) -> R4
	STR R6, R4, #0		; save USER stack pointer
	ADD R6, R4, #0		; begin using general stack pointer (R6) here

PUTS_CHARLOOP
	LDR R1, R0, #0
	BRz PUTS_EXIT

PUTS_ADSRLOOP
	LC R2, OS_ADSR_ADDR
	LDR R2, R2, #0
	BRzp PUTS_ADSRLOOP
	LC R2, OS_ADDR_ADDR
	STR R1, R2, #0
	
	ADD R0, R0, #1		; goto next character
	JMP PUTS_CHARLOOP
PUTS_EXIT
	LDR R6, R6, #0
	RTI


	





	

	
```

## File: `tetris.asm`
```
		.DATA
shapes 		.FILL #1632
		.FILL #1632
		.FILL #1632
		.FILL #1632
		.FILL #61440
		.FILL #17476
		.FILL #61440
		.FILL #17476
		.FILL #36352
		.FILL #25664
		.FILL #3616
		.FILL #17600
		.FILL #11776
		.FILL #17504
		.FILL #3712
		.FILL #50240
		.FILL #50688
		.FILL #19584
		.FILL #50688
		.FILL #19584
		.FILL #27648
		.FILL #35904
		.FILL #27648
		.FILL #35904
		.FILL #19968
		.FILL #17984
		.FILL #3648
		.FILL #19520
		.DATA
colors 		.FILL #31744
		.FILL #51
		.FILL #13056
		.FILL #32752
		.FILL #62976
		.FILL #1904
		.FILL #65535
		.DATA
score 		.FILL #0
;;;;;;;;;;;;;;;;;;;;;;;;;;;;print_num;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		.CODE
		.FALIGN
print_num
	;; prologue
	STR R7, R6, #-2	;; save return address
	STR R5, R6, #-3	;; save base pointer
	ADD R6, R6, #-3
	ADD R5, R6, #0
	ADD R6, R6, #-6	;; allocate stack space for local variables
	;; function body
	LDR R7, R5, #3
	CONST R3, #0
	CMP R7, R3
	BRnp L2_tetris
	LEA R7, L4_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
	JMP L3_tetris
L2_tetris
	CONST R7, #6
	ADD R6, R6, #-1
	STR R7, R6, #0
	ADD R7, R5, #-6
	ADD R6, R6, #-1
	STR R7, R6, #0
	LDR R7, R5, #3
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_utoa
	ADD R6, R6, #3	;; free space for arguments
	ADD R7, R5, #-6
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
	LEA R7, L5_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
L3_tetris
L1_tetris
	;; epilogue
	ADD R6, R5, #0	;; pop locals off stack
	ADD R6, R6, #3	;; free space for return address, base pointer, and return value
	STR R7, R6, #-1	;; store return value
	LDR R5, R6, #-3	;; restore base pointer
	LDR R7, R6, #-2	;; restore return address
	RET

;;;;;;;;;;;;;;;;;;;;;;;;;;;;clear_tetris_array;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		.CODE
		.FALIGN
clear_tetris_array
	;; prologue
	STR R7, R6, #-2	;; save return address
	STR R5, R6, #-3	;; save base pointer
	ADD R6, R6, #-3
	ADD R5, R6, #0
	ADD R6, R6, #-2	;; allocate stack space for local variables
	;; function body
	CONST R7, #0
	STR R7, R5, #-2
L7_tetris
	CONST R7, #0
	STR R7, R5, #-1
L11_tetris
	LDR R7, R5, #-1
	LDR R3, R5, #-2
	SLL R3, R3, #4
	LEA R2, cells
	ADD R3, R3, R2
	ADD R7, R7, R3
	CONST R3, #0
	STR R3, R7, #0
L12_tetris
	LDR R7, R5, #-1
	ADD R7, R7, #1
	STR R7, R5, #-1
	LDR R7, R5, #-1
	CONST R3, #16
	CMP R7, R3
	BRn L11_tetris
L8_tetris
	LDR R7, R5, #-2
	ADD R7, R7, #1
	STR R7, R5, #-2
	LDR R7, R5, #-2
	CONST R3, #15
	CMP R7, R3
	BRn L7_tetris
L6_tetris
	;; epilogue
	ADD R6, R5, #0	;; pop locals off stack
	ADD R6, R6, #3	;; free space for return address, base pointer, and return value
	STR R7, R6, #-1	;; store return value
	LDR R5, R6, #-3	;; restore base pointer
	LDR R7, R6, #-2	;; restore return address
	RET

;;;;;;;;;;;;;;;;;;;;;;;;;;;;draw_cells;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		.CODE
		.FALIGN
draw_cells
	;; prologue
	STR R7, R6, #-2	;; save return address
	STR R5, R6, #-3	;; save base pointer
	ADD R6, R6, #-3
	ADD R5, R6, #0
	ADD R6, R6, #-2	;; allocate stack space for local variables
	;; function body
	CONST R7, #0
	STR R7, R5, #-2
L16_tetris
	CONST R7, #0
	STR R7, R5, #-1
L20_tetris
	LDR R7, R5, #-1
	LDR R3, R5, #-2
	SLL R2, R3, #4
	LEA R1, cells
	ADD R2, R2, R1
	ADD R2, R7, R2
	LDR R2, R2, #0
	ADD R6, R6, #-1
	STR R2, R6, #0
	SLL R3, R3, #3
	ADD R3, R3, #4
	ADD R6, R6, #-1
	STR R3, R6, #0
	SLL R7, R7, #3
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_draw_8x8
	ADD R6, R6, #3	;; free space for arguments
L21_tetris
	LDR R7, R5, #-1
	ADD R7, R7, #1
	STR R7, R5, #-1
	LDR R7, R5, #-1
	CONST R3, #16
	CMP R7, R3
	BRn L20_tetris
L17_tetris
	LDR R7, R5, #-2
	ADD R7, R7, #1
	STR R7, R5, #-2
	LDR R7, R5, #-2
	CONST R3, #15
	CMP R7, R3
	BRn L16_tetris
L15_tetris
	;; epilogue
	ADD R6, R5, #0	;; pop locals off stack
	ADD R6, R6, #3	;; free space for return address, base pointer, and return value
	STR R7, R6, #-1	;; store return value
	LDR R5, R6, #-3	;; restore base pointer
	LDR R7, R6, #-2	;; restore return address
	RET

;;;;;;;;;;;;;;;;;;;;;;;;;;;;redraw;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		.CODE
		.FALIGN
redraw
	;; prologue
	STR R7, R6, #-2	;; save return address
	STR R5, R6, #-3	;; save base pointer
	ADD R6, R6, #-3
	ADD R5, R6, #0
	;; function body
	JSR lc4_reset_vmem
	ADD R6, R6, #0	;; free space for arguments
	JSR draw_cells
	ADD R6, R6, #0	;; free space for arguments
	JSR lc4_blt_vmem
	ADD R6, R6, #0	;; free space for arguments
L24_tetris
	;; epilogue
	ADD R6, R5, #0	;; pop locals off stack
	ADD R6, R6, #3	;; free space for return address, base pointer, and return value
	STR R7, R6, #-1	;; store return value
	LDR R5, R6, #-3	;; restore base pointer
	LDR R7, R6, #-2	;; restore return address
	RET

;;;;;;;;;;;;;;;;;;;;;;;;;;;;test_for_collision;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		.CODE
		.FALIGN
test_for_collision
	;; prologue
	STR R7, R6, #-2	;; save return address
	STR R5, R6, #-3	;; save base pointer
	ADD R6, R6, #-3
	ADD R5, R6, #0
	ADD R6, R6, #-6	;; allocate stack space for local variables
	;; function body
	CONST R7, #0
	STR R7, R5, #-3
	LDR R7, R5, #4
	STR R7, R5, #-2
	JMP L29_tetris
L26_tetris
	LDR R7, R5, #5
	STR R7, R5, #-1
	JMP L33_tetris
L30_tetris
	LDR R7, R5, #-2
	STR R7, R5, #-4
	CONST R3, #15
	CMP R7, R3
	BRzp L38_tetris
	CONST R7, #0
	STR R7, R5, #-5
	LDR R3, R5, #-4
	CMP R3, R7
	BRn L38_tetris
	LDR R7, R5, #-1
	STR R7, R5, #-6
	LDR R3, R5, #-5
	CMP R7, R3
	BRn L38_tetris
	CONST R7, #16
	LDR R3, R5, #-6
	CMP R3, R7
	BRn L34_tetris
L38_tetris
	LDR R7, R5, #3
	CONST R3, #0
	HICONST R3, #128
	AND R7, R7, R3
	CONST R3, #0
	CMP R7, R3
	BRz L34_tetris
	CONST R7, #1
	JMP L25_tetris
L34_tetris
	CONST R7, #0
	LDR R3, R5, #3
	CONST R2, #0
	HICONST R2, #128
	AND R3, R3, R2
	CMP R3, R7
	BRz L39_tetris
	LDR R3, R5, #-1
	LDR R2, R5, #-2
	SLL R2, R2, #4
	LEA R1, cells
	ADD R2, R2, R1
	ADD R3, R3, R2
	LDR R3, R3, #0
	CMP R3, R7
	BRz L39_tetris
	CONST R7, #1
	JMP L25_tetris
L39_tetris
	LDR R7, R5, #3
	SLL R7, R7, #1
	STR R7, R5, #3
L31_tetris
	LDR R7, R5, #-1
	ADD R7, R7, #1
	STR R7, R5, #-1
L33_tetris
	LDR R7, R5, #-1
	LDR R3, R5, #5
	ADD R3, R3, #4
	CMP R7, R3
	BRn L30_tetris
L27_tetris
	LDR R7, R5, #-2
	ADD R7, R7, #1
	STR R7, R5, #-2
L29_tetris
	LDR R7, R5, #-2
	LDR R3, R5, #4
	ADD R3, R3, #4
	CMP R7, R3
	BRn L26_tetris
	LDR R7, R5, #-3
L25_tetris
	;; epilogue
	ADD R6, R5, #0	;; pop locals off stack
	ADD R6, R6, #3	;; free space for return address, base pointer, and return value
	STR R7, R6, #-1	;; store return value
	LDR R5, R6, #-3	;; restore base pointer
	LDR R7, R6, #-2	;; restore return address
	RET

;;;;;;;;;;;;;;;;;;;;;;;;;;;;draw_shape;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		.CODE
		.FALIGN
draw_shape
	;; prologue
	STR R7, R6, #-2	;; save return address
	STR R5, R6, #-3	;; save base pointer
	ADD R6, R6, #-3
	ADD R5, R6, #0
	ADD R6, R6, #-2	;; allocate stack space for local variables
	;; function body
	LDR R7, R5, #4
	STR R7, R5, #-2
	JMP L45_tetris
L42_tetris
	LDR R7, R5, #5
	STR R7, R5, #-1
	JMP L49_tetris
L46_tetris
	LDR R7, R5, #3
	CONST R3, #0
	HICONST R3, #128
	AND R7, R7, R3
	CONST R3, #0
	CMP R7, R3
	BRz L50_tetris
	LDR R7, R5, #-1
	LDR R3, R5, #-2
	SLL R3, R3, #4
	LEA R2, cells
	ADD R3, R3, R2
	ADD R7, R7, R3
	LDR R3, R5, #6
	STR R3, R7, #0
L50_tetris
	LDR R7, R5, #3
	SLL R7, R7, #1
	STR R7, R5, #3
L47_tetris
	LDR R7, R5, #-1
	ADD R7, R7, #1
	STR R7, R5, #-1
L49_tetris
	LDR R7, R5, #-1
	LDR R3, R5, #5
	ADD R3, R3, #4
	CMP R7, R3
	BRn L46_tetris
L43_tetris
	LDR R7, R5, #-2
	ADD R7, R7, #1
	STR R7, R5, #-2
L45_tetris
	LDR R7, R5, #-2
	LDR R3, R5, #4
	ADD R3, R3, #4
	CMP R7, R3
	BRn L42_tetris
L41_tetris
	;; epilogue
	ADD R6, R5, #0	;; pop locals off stack
	ADD R6, R6, #3	;; free space for return address, base pointer, and return value
	STR R7, R6, #-1	;; store return value
	LDR R5, R6, #-3	;; restore base pointer
	LDR R7, R6, #-2	;; restore return address
	RET

;;;;;;;;;;;;;;;;;;;;;;;;;;;;remove_filled_rows;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		.CODE
		.FALIGN
remove_filled_rows
	;; prologue
	STR R7, R6, #-2	;; save return address
	STR R5, R6, #-3	;; save base pointer
	ADD R6, R6, #-3
	ADD R5, R6, #0
	ADD R6, R6, #-5	;; allocate stack space for local variables
	;; function body
	CONST R7, #14
	STR R7, R5, #-3
L53_tetris
	CONST R7, #0
	STR R7, R5, #-1
	STR R7, R5, #-4
	STR R7, R5, #-5
	JMP L60_tetris
L57_tetris
	LDR R7, R5, #-1
	LDR R3, R5, #-3
	SLL R3, R3, #4
	LEA R2, cells
	ADD R3, R3, R2
	ADD R7, R7, R3
	LDR R7, R7, #0
	CONST R3, #0
	CMP R7, R3
	BRz L61_tetris
	LDR R7, R5, #-4
	ADD R7, R7, #1
	STR R7, R5, #-4
L61_tetris
L58_tetris
	LDR R7, R5, #-1
	ADD R7, R7, #1
	STR R7, R5, #-1
L60_tetris
	LDR R7, R5, #-1
	CONST R3, #16
	CMP R7, R3
	BRn L57_tetris
	LDR R7, R5, #-4
	CONST R3, #16
	CMP R7, R3
	BRnp L63_tetris
	CONST R7, #1
	STR R7, R5, #-5
L63_tetris
	LDR R7, R5, #-5
	CONST R3, #0
	CMP R7, R3
	BRz L65_tetris
	LEA R7, score
	LDR R3, R7, #0
	ADD R3, R3, #1
	STR R3, R7, #0
	LDR R7, R5, #-3
	STR R7, R5, #-2
	JMP L70_tetris
L67_tetris
	CONST R7, #0
	STR R7, R5, #-1
L71_tetris
	LDR R7, R5, #-1
	LDR R3, R5, #-2
	SLL R3, R3, #4
	LEA R2, cells
	ADD R1, R3, R2
	ADD R1, R7, R1
	ADD R2, R2, #-16
	ADD R3, R3, R2
	ADD R7, R7, R3
	LDR R7, R7, #0
	STR R7, R1, #0
L72_tetris
	LDR R7, R5, #-1
	ADD R7, R7, #1
	STR R7, R5, #-1
	LDR R7, R5, #-1
	CONST R3, #16
	CMP R7, R3
	BRn L71_tetris
L68_tetris
	LDR R7, R5, #-2
	ADD R7, R7, #-1
	STR R7, R5, #-2
L70_tetris
	LDR R7, R5, #-2
	CONST R3, #0
	CMP R7, R3
	BRp L67_tetris
	LDR R7, R5, #-3
	ADD R7, R7, #1
	STR R7, R5, #-3
L65_tetris
L54_tetris
	LDR R7, R5, #-3
	ADD R7, R7, #-1
	STR R7, R5, #-3
	LDR R7, R5, #-3
	CONST R3, #-1
	CMP R7, R3
	BRp L53_tetris
L52_tetris
	;; epilogue
	ADD R6, R5, #0	;; pop locals off stack
	ADD R6, R6, #3	;; free space for return address, base pointer, and return value
	STR R7, R6, #-1	;; store return value
	LDR R5, R6, #-3	;; restore base pointer
	LDR R7, R6, #-2	;; restore return address
	RET

;;;;;;;;;;;;;;;;;;;;;;;;;;;;main;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		.CODE
		.FALIGN
main
	;; prologue
	STR R7, R6, #-2	;; save return address
	STR R5, R6, #-3	;; save base pointer
	ADD R6, R6, #-3
	ADD R5, R6, #0
	ADD R6, R6, #-12	;; allocate stack space for local variables
	;; function body
	CONST R7, #0
	STR R7, R5, #-3
	JSR clear_tetris_array
	ADD R6, R6, #0	;; free space for arguments
	JSR redraw
	ADD R6, R6, #0	;; free space for arguments
	LEA R7, L76_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
	LEA R7, L77_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
	LEA R7, L78_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
	LEA R7, L79_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
	LEA R7, L80_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
	LEA R7, L81_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
	CONST R7, #-1
	STR R7, R5, #-1
	JMP L83_tetris
L82_tetris
	JSR lc4_get_event
	LDR R7, R6, #-1	;; grab return value
	ADD R6, R6, #0	;; free space for arguments
	STR R7, R5, #-2
	LDR R7, R5, #-3
	CONST R3, #0
	CMP R7, R3
	BRnp L85_tetris
	LDR R7, R5, #-2
	CONST R3, #32
	CMP R7, R3
	BRnp L85_tetris
	JSR clear_tetris_array
	ADD R6, R6, #0	;; free space for arguments
	CONST R7, #-1
	STR R7, R5, #-1
	CONST R7, #1
	STR R7, R5, #-3
	LEA R7, L87_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
L85_tetris
	LDR R7, R5, #-3
	CONST R3, #0
	CMP R7, R3
	BRz L88_tetris
	LDR R7, R5, #-1
	CONST R3, #-1
	CMP R7, R3
	BRnp L90_tetris
	CONST R7, #0
	STR R7, R5, #-1
	CONST R7, #8
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_rand_power2
	LDR R7, R6, #-1	;; grab return value
	ADD R6, R6, #1	;; free space for arguments
	STR R7, R5, #-10
	CONST R3, #4
	ADD R6, R6, #-1
	STR R3, R6, #0
	JSR lc4_rand_power2
	LDR R7, R6, #-1	;; grab return value
	ADD R6, R6, #1	;; free space for arguments
	STR R7, R5, #-11
	CONST R3, #2
	ADD R6, R6, #-1
	STR R3, R6, #0
	JSR lc4_rand_power2
	LDR R7, R6, #-1	;; grab return value
	ADD R6, R6, #1	;; free space for arguments
	LDR R3, R5, #-10
	LDR R2, R5, #-11
	ADD R3, R3, R2
	ADD R7, R3, R7
	STR R7, R5, #-4
	CONST R7, #4
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_rand_power2
	LDR R7, R6, #-1	;; grab return value
	ADD R6, R6, #1	;; free space for arguments
	STR R7, R5, #-12
	CONST R3, #4
	ADD R6, R6, #-1
	STR R3, R6, #0
	JSR lc4_rand_power2
	LDR R7, R6, #-1	;; grab return value
	ADD R6, R6, #1	;; free space for arguments
	LDR R3, R5, #-12
	ADD R7, R3, R7
	STR R7, R5, #-5
	CONST R7, #4
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_rand_power2
	LDR R7, R6, #-1	;; grab return value
	ADD R6, R6, #1	;; free space for arguments
	STR R7, R5, #-6
	LDR R7, R5, #-4
	ADD R6, R6, #-1
	STR R7, R6, #0
	LDR R7, R5, #-1
	ADD R6, R6, #-1
	STR R7, R6, #0
	LDR R7, R5, #-5
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR test_for_collision
	LDR R7, R6, #-1	;; grab return value
	ADD R6, R6, #3	;; free space for arguments
	CONST R3, #0
	CMP R7, R3
	BRz L92_tetris
	CONST R7, #0
	STR R7, R5, #-3
	LEA R7, L94_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
	LEA R7, score
	LDR R7, R7, #0
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR print_num
	ADD R6, R6, #1	;; free space for arguments
	LEA R7, L95_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
L92_tetris
L90_tetris
	LDR R7, R5, #-4
	STR R7, R5, #-7
	LDR R7, R5, #-1
	STR R7, R5, #-9
	LDR R7, R5, #-6
	STR R7, R5, #-8
	LDR R7, R5, #-2
	CONST R3, #106
	CMP R7, R3
	BRnp L96_tetris
	LDR R7, R5, #-4
	ADD R7, R7, #-1
	STR R7, R5, #-7
	JMP L97_tetris
L96_tetris
	LDR R7, R5, #-2
	CONST R3, #107
	CMP R7, R3
	BRnp L98_tetris
	LDR R7, R5, #-4
	ADD R7, R7, #1
	STR R7, R5, #-7
	JMP L99_tetris
L98_tetris
	LDR R7, R5, #-2
	CONST R3, #97
	CMP R7, R3
	BRnp L100_tetris
	LDR R7, R5, #-6
	ADD R7, R7, #-1
	AND R7, R7, #3
	STR R7, R5, #-8
	JMP L101_tetris
L100_tetris
	LDR R7, R5, #-2
	CONST R3, #115
	CMP R7, R3
	BRnp L102_tetris
	LDR R7, R5, #-6
	ADD R7, R7, #1
	AND R7, R7, #3
	STR R7, R5, #-8
	JMP L103_tetris
L102_tetris
	LDR R7, R5, #-1
	ADD R7, R7, #1
	STR R7, R5, #-9
L103_tetris
L101_tetris
L99_tetris
L97_tetris
	CONST R7, #0
	ADD R6, R6, #-1
	STR R7, R6, #0
	LDR R7, R5, #-4
	ADD R6, R6, #-1
	STR R7, R6, #0
	LDR R7, R5, #-1
	ADD R6, R6, #-1
	STR R7, R6, #0
	LDR R7, R5, #-6
	LDR R3, R5, #-5
	SLL R3, R3, #2
	LEA R2, shapes
	ADD R3, R3, R2
	ADD R7, R7, R3
	LDR R7, R7, #0
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR draw_shape
	ADD R6, R6, #4	;; free space for arguments
	LDR R7, R5, #-7
	ADD R6, R6, #-1
	STR R7, R6, #0
	LDR R7, R5, #-9
	ADD R6, R6, #-1
	STR R7, R6, #0
	LDR R7, R5, #-8
	LDR R3, R5, #-5
	SLL R3, R3, #2
	LEA R2, shapes
	ADD R3, R3, R2
	ADD R7, R7, R3
	LDR R7, R7, #0
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR test_for_collision
	LDR R7, R6, #-1	;; grab return value
	ADD R6, R6, #3	;; free space for arguments
	CONST R3, #0
	CMP R7, R3
	BRnp L104_tetris
	LDR R7, R5, #-9
	STR R7, R5, #-1
	LDR R7, R5, #-7
	STR R7, R5, #-4
	LDR R7, R5, #-8
	STR R7, R5, #-6
	LDR R7, R5, #-5
	LEA R3, colors
	ADD R3, R7, R3
	LDR R3, R3, #0
	ADD R6, R6, #-1
	STR R3, R6, #0
	LDR R3, R5, #-4
	ADD R6, R6, #-1
	STR R3, R6, #0
	LDR R3, R5, #-1
	ADD R6, R6, #-1
	STR R3, R6, #0
	LDR R3, R5, #-6
	SLL R7, R7, #2
	LEA R2, shapes
	ADD R7, R7, R2
	ADD R7, R3, R7
	LDR R7, R7, #0
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR draw_shape
	ADD R6, R6, #4	;; free space for arguments
	JMP L105_tetris
L104_tetris
	LDR R7, R5, #-5
	LEA R3, colors
	ADD R3, R7, R3
	LDR R3, R3, #0
	ADD R6, R6, #-1
	STR R3, R6, #0
	LDR R3, R5, #-4
	ADD R6, R6, #-1
	STR R3, R6, #0
	LDR R3, R5, #-1
	ADD R6, R6, #-1
	STR R3, R6, #0
	LDR R3, R5, #-6
	SLL R7, R7, #2
	LEA R2, shapes
	ADD R7, R7, R2
	ADD R7, R3, R7
	LDR R7, R7, #0
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR draw_shape
	ADD R6, R6, #4	;; free space for arguments
	LDR R7, R5, #-2
	CONST R3, #0
	CMP R7, R3
	BRnp L106_tetris
	JSR remove_filled_rows
	ADD R6, R6, #0	;; free space for arguments
	CONST R7, #-1
	STR R7, R5, #-1
L106_tetris
L105_tetris
	JSR redraw
	ADD R6, R6, #0	;; free space for arguments
L88_tetris
L83_tetris
	JMP L82_tetris
	CONST R7, #0
L75_tetris
	;; epilogue
	ADD R6, R5, #0	;; pop locals off stack
	ADD R6, R6, #3	;; free space for return address, base pointer, and return value
	STR R7, R6, #-1	;; store return value
	LDR R5, R6, #-3	;; restore base pointer
	LDR R7, R6, #-2	;; restore return address
	RET

		.DATA
cells 		.BLKW 240
		.DATA
L95_tetris 		.STRINGZ "Game Over\n"
		.DATA
L94_tetris 		.STRINGZ "Score:\n"
		.DATA
L87_tetris 		.STRINGZ "Game On!\n"
		.DATA
L81_tetris 		.STRINGZ "Press space bar to start\n"
		.DATA
L80_tetris 		.STRINGZ "Press a to rotate counter-clockwise\n"
		.DATA
L79_tetris 		.STRINGZ "Press s to rotate clockwise\n"
		.DATA
L78_tetris 		.STRINGZ "Press k to go right\n"
		.DATA
L77_tetris 		.STRINGZ "Press j to go left\n"
		.DATA
L76_tetris 		.STRINGZ "!!! Welcome to Tetris !!!\n"
		.DATA
L5_tetris 		.STRINGZ "\n"
		.DATA
L4_tetris 		.STRINGZ "0\n"
```

## File: `tetris.c`
```c
/*
 * Tetris.c : Camillo J. Taylor Nov. 4, 2011
 */

#include "lc4libc.h"

/*
 * #############  DATA STRUCTURES THAT STORE THE GAME STATE ######################
 */

// Number of rows and columns in the tetris array
#define NROWS     15
#define NCOLS     16

#define NSHAPES    7

// Array specifying the configuration of the game pieces - for every shape there are 4 entries
// correspoinding to the 4 possible orientations. Each configuration is captured by a 16 bit field
// where each bit corresponds to a cell. The MSB corresponds to the top left cell, the next bit to the
// cell next to that etc.

lc4uint shapes[NSHAPES][4] = { 
  { 0x0660U, 0x0660U, 0x0660U, 0x0660U},
  { 0xF000U, 0x4444U, 0xF000U, 0x4444U},
  { 0x8E00U, 0x6440U, 0x0E20U, 0x44C0U},
  { 0x2E00U, 0x4460U, 0x0E80U, 0xC440U},
  { 0xC600U, 0x4C80U, 0xC600U, 0x4C80U},
  { 0x6C00U, 0x8C40U, 0x6C00U, 0x8C40U},
  { 0x4E00U, 0x4640U, 0x0E40U, 0x4C40U}
 };

// Each shape has an associated color - these colors are defined in lc4libc.h
lc4uint colors[NSHAPES] = {RED, BLUE, GREEN, YELLOW, ORANGE, CYAN, WHITE};

//Game Score
int score = 0;

// This 2D array contains the current state of the tetris array each entry indicates the color
// currently stored in the corresponding block. Zero entries indicate unoccupied blocks.
lc4uint cells[NROWS][NCOLS];
/*lc4uint cells[NROWS][NCOLS] = {
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{WHITE, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, WHITE},
{RED, RED, RED, RED, RED, RED, RED, RED, RED, RED, RED, RED, RED, RED, RED, RED},
{RED, BLUE, GREEN, YELLOW, ORANGE, CYAN, RED, RED, RED, BLUE, GREEN, YELLOW, ORANGE, CYAN, WHITE, BLUE}};
*/

/*
 * ###############################################################################
 */

void print_num(lc4uint num)
{
	// Max value of num is 2**16-1=65535 which has 5 characters + 1 for null
	// Don't need space for minus sign, because number is unsigned
	char s[6];
	if (num == 0) {
		lc4_puts((lc4uint*)"0\n");
	} else {
		lc4_utoa(num, s, 6);
		lc4_puts((lc4uint*)s);
		lc4_puts((lc4uint*)"\n");
	}
}

// Clear the tetris array
void clear_tetris_array ()
{

  /// YOUR CODE HERE
	int i, j;
	for (i = 0; i < NROWS; i++)
		for (j = 0; j < NCOLS; j++)
			cells[i][j] = 0;

}

/*
 * ################# CODE FOR DRAWING THE SCENE ##########################
 */

//
// Draw the cells on the screen using the lc4_draw_8x8 routine.
// Remember to skip the top 4 rows in the display since a 15x16 array of 8x8 pixel blocks
// will take 120x128 pixels while our display has 124 rows.
//
void draw_cells ()
{
	int i, j;
	for (i = 0; i < NROWS; i++){
		for (j = 0; j < NCOLS; j++){
			lc4_draw_8x8(j*8, i*8 + 4, cells[i][j]);
		}
	}
}

void redraw ()
{
  // This function assumes that PennSim is being run in double buffered mode
  // In this mode we first clear the video memory buffer with lc4_reset_vmem,
  // then draw the scene, then call lc4_blt_vmem to swap the buffer to the screen
  // NOTE that you need to run PennSim with the following command:
  // java -jar PennSim.jar -d

  lc4_reset_vmem();

  draw_cells ();

  lc4_blt_vmem();
}

/*
 * ################# CODE FOR UPDATNG THE GAME STATE ##########################
 */

// Tests whether the pattern specified in the bitvector shape can be drawn without
// collision in the current array. If there is a collision return 1 else return 0.
// This function also tests whether any of the filled cells would be drawn outside
// the bounds of the array which would also be considered a collision.
int test_for_collision (lc4uint shape, int row, int col)
{

  /// YOUR CODE HERE
	int coll = 0, i, j;
	for (i = row; i < row + 4; i++) {
		for (j = col; j <  col + 4; j++) {
			if ((i >= NROWS || i < 0  || j < 0 || j >= NCOLS) && (shape & 0x8000U) != 0) {
				return 1;
			}
			else {
				if ((shape & 0x8000U) != 0 && cells[i][j] != 0) {
					return 1;
				}
			}
			shape = shape << 1;
		}
	}
	return coll;
}

// draw the specified shape into the array - you can assume that you have already
// called test_for_collision so there shouldn't be any illegal memory accesses.
void draw_shape (lc4uint shape, int row, int col, lc4uint color)
{
	int i, j;
	for (i = row; i < row+4; i++) {
		for (j = col; j < col+4; j++) {
			if ((shape & 0x8000U) != 0)
				cells[i][j] = color;
			shape = shape << 1;
		}
	}

}

// Iterate through the tetris array from bottom to top removing any rows that
// are completely filled.
void remove_filled_rows ()
{
  /// YOUR CODE HERE
	int i, j, k, fsum, check;
	for (i = NROWS - 1; i > -1; i--) {
		for (j = 0, fsum = 0, check = 0; j < NCOLS; j++)
			if (cells[i][j] != 0)
				fsum++;
		if (fsum == NCOLS)
			check = 1;
		if (check){
			score += 1;
			for (k = i; k > 0; k--)
				for (j = 0; j < NCOLS; j++)
					cells[k][j] = cells[k - 1][j];
			i++;
		}
		
	}
}


/*
 * ############################### MAIN FUNCTION #############################
 */


int main ()
{
  lc4uint event, collision;
  int game_started = 0;   // game mode
  int row, col, shape_idx, orientation;
  int new_row, new_col, new_orientation;
  clear_tetris_array ();
  redraw ();

  lc4_puts ((lc4uint*)"!!! Welcome to Tetris !!!\n");
  lc4_puts ((lc4uint*)"Press j to go left\n");
  lc4_puts ((lc4uint*)"Press k to go right\n");
  lc4_puts ((lc4uint*)"Press s to rotate clockwise\n");
  lc4_puts ((lc4uint*)"Press a to rotate counter-clockwise\n");

  lc4_puts ((lc4uint*)"Press space bar to start\n");

  row = -1;
  // MAIN LOOP

  while (1) {
    /// YOUR CODE HERE
	  
	  event = lc4_get_event();
	  if (!game_started && event == 0x00020) {
		  clear_tetris_array();
		  row = -1;
		  game_started = 1;
		  lc4_puts ((lc4uint*)"Game On!\n");
	  }
	  if (game_started) {
		  if (row == -1) {
			  row = 0;
			  col = lc4_rand_power2(8) + lc4_rand_power2(4) + lc4_rand_power2(2);
			  shape_idx = lc4_rand_power2(4) + lc4_rand_power2(4);
			  orientation = lc4_rand_power2(4);
			  if(test_for_collision(shape_idx, row, col)){
				  game_started = 0;
				  lc4_puts ((lc4uint*)"Score:\n");
				  print_num(score);
				  lc4_puts ((lc4uint*)"Game Over\n");
			  }
		  }
		  new_col = col;
		  new_row = row;
		  new_orientation = orientation;
		  if (event == 0x0006A) 
			  new_col = col - 1;
		  else {
			  if (event == 0x0006B)
				  new_col = col + 1;
			  else {
				  if (event == 0x00061)
					  new_orientation = (orientation - 1) & 0x3;
				  else {
					  if (event == 0x00073)
						  new_orientation = (orientation + 1) & 0x3;
					  else
						  new_row = row + 1;
				  }
			  }
		  }
		  
		  draw_shape(shapes[shape_idx][orientation], row, col, 0);
		  if (!test_for_collision(shapes[shape_idx][new_orientation], new_row, new_col)) {
			  row = new_row;
			  col = new_col;
			  orientation = new_orientation;
			  draw_shape(shapes[shape_idx][orientation], row, col, colors[shape_idx]);
		  }
		  else {
			  draw_shape(shapes[shape_idx][orientation], row, col, colors[shape_idx]);
			  if (event == 0) {
				  remove_filled_rows();
				  row = -1;
			  }
		  }
		  redraw();
	  } 
  }

  return 0;
}

```

## File: `tetris2.asm`
```
		.DATA
shapes 		.FILL #1632
		.FILL #1632
		.FILL #1632
		.FILL #1632
		.FILL #61440
		.FILL #17476
		.FILL #61440
		.FILL #17476
		.FILL #36352
		.FILL #25664
		.FILL #3616
		.FILL #17600
		.FILL #11776
		.FILL #17504
		.FILL #3712
		.FILL #50240
		.FILL #50688
		.FILL #19584
		.FILL #50688
		.FILL #19584
		.FILL #27648
		.FILL #35904
		.FILL #27648
		.FILL #35904
		.FILL #19968
		.FILL #17984
		.FILL #3648
		.FILL #19520
		.DATA
colors 		.FILL #31744
		.FILL #51
		.FILL #13056
		.FILL #32752
		.FILL #62976
		.FILL #1904
		.FILL #65535
uconst
		.UCONST #239
		.DATA
score 		.FILL #0
;;;;;;;;;;;;;;;;;;;;;;;;;;;;print_num;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		.CODE
		.FALIGN
print_num
	;; prologue
	STR R7, R6, #-2	;; save return address
	STR R5, R6, #-3	;; save base pointer
	ADD R6, R6, #-3
	ADD R5, R6, #0
	ADD R6, R6, #-6	;; allocate stack space for local variables
	;; function body
	LDR R7, R5, #3
	CONST R3, #0
	CMP R7, R3
	BRnp L2_tetris
	LEA R7, L4_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
	JMP L3_tetris
L2_tetris
	CONST R7, #6
	ADD R6, R6, #-1
	STR R7, R6, #0
	ADD R7, R5, #-6
	ADD R6, R6, #-1
	STR R7, R6, #0
	LDR R7, R5, #3
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_utoa
	ADD R6, R6, #3	;; free space for arguments
	ADD R7, R5, #-6
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
	LEA R7, L5_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
L3_tetris
L1_tetris
	;; epilogue
	ADD R6, R5, #0	;; pop locals off stack
	ADD R6, R6, #3	;; free space for return address, base pointer, and return value
	STR R7, R6, #-1	;; store return value
	LDR R5, R6, #-3	;; restore base pointer
	LDR R7, R6, #-2	;; restore return address
	RET

;;;;;;;;;;;;;;;;;;;;;;;;;;;;clear_tetris_array;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		.CODE
		.FALIGN
clear_tetris_array
	LEA R2, cells
	CONST R3, #0
	CONST R7, #0
	LC R5, uconst, #0
LOOP
	CMP R3, R5
	BRp  END_LOOP
	STR  R2, R7 ,#0
	ADD R3, R3, #1
	ADD R2, R2, #1
	JMP LOOP
END_LOOP
	RET

;;;;;;;;;;;;;;;;;;;;;;;;;;;;draw_cells;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		.CODE
		.FALIGN
draw_cells
	;; prologue
	STR R7, R6, #-2	;; save return address
	STR R5, R6, #-3	;; save base pointer
	ADD R6, R6, #-3
	ADD R5, R6, #0
	ADD R6, R6, #-2	;; allocate stack space for local variables
	;; function body
	CONST R7, #0
	STR R7, R5, #-2
L16_tetris
	CONST R7, #0
	STR R7, R5, #-1
L20_tetris
	LDR R7, R5, #-1
	LDR R3, R5, #-2
	SLL R2, R3, #4
	LEA R1, cells
	ADD R2, R2, R1
	ADD R2, R7, R2
	LDR R2, R2, #0
	ADD R6, R6, #-1
	STR R2, R6, #0
	SLL R3, R3, #3
	ADD R3, R3, #4
	ADD R6, R6, #-1
	STR R3, R6, #0
	SLL R7, R7, #3
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_draw_8x8
	ADD R6, R6, #3	;; free space for arguments
L21_tetris
	LDR R7, R5, #-1
	ADD R7, R7, #1
	STR R7, R5, #-1
	LDR R7, R5, #-1
	CONST R3, #16
	CMP R7, R3
	BRn L20_tetris
L17_tetris
	LDR R7, R5, #-2
	ADD R7, R7, #1
	STR R7, R5, #-2
	LDR R7, R5, #-2
	CONST R3, #15
	CMP R7, R3
	BRn L16_tetris
L15_tetris
	;; epilogue
	ADD R6, R5, #0	;; pop locals off stack
	ADD R6, R6, #3	;; free space for return address, base pointer, and return value
	STR R7, R6, #-1	;; store return value
	LDR R5, R6, #-3	;; restore base pointer
	LDR R7, R6, #-2	;; restore return address
	RET

;;;;;;;;;;;;;;;;;;;;;;;;;;;;redraw;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		.CODE
		.FALIGN
redraw
	;; prologue
	STR R7, R6, #-2	;; save return address
	STR R5, R6, #-3	;; save base pointer
	ADD R6, R6, #-3
	ADD R5, R6, #0
	;; function body
	JSR lc4_reset_vmem
	ADD R6, R6, #0	;; free space for arguments
	JSR draw_cells
	ADD R6, R6, #0	;; free space for arguments
	JSR lc4_blt_vmem
	ADD R6, R6, #0	;; free space for arguments
L24_tetris
	;; epilogue
	ADD R6, R5, #0	;; pop locals off stack
	ADD R6, R6, #3	;; free space for return address, base pointer, and return value
	STR R7, R6, #-1	;; store return value
	LDR R5, R6, #-3	;; restore base pointer
	LDR R7, R6, #-2	;; restore return address
	RET

;;;;;;;;;;;;;;;;;;;;;;;;;;;;test_for_collision;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		.CODE
		.FALIGN
test_for_collision
	;; prologue
	STR R7, R6, #-2	;; save return address
	STR R5, R6, #-3	;; save base pointer
	ADD R6, R6, #-3
	ADD R5, R6, #0
	ADD R6, R6, #-6	;; allocate stack space for local variables
	;; function body
	CONST R7, #0
	STR R7, R5, #-3
	LDR R7, R5, #4
	STR R7, R5, #-2
	JMP L29_tetris
L26_tetris
	LDR R7, R5, #5
	STR R7, R5, #-1
	JMP L33_tetris
L30_tetris
	LDR R7, R5, #-2
	STR R7, R5, #-4
	CONST R3, #15
	CMP R7, R3
	BRzp L38_tetris
	CONST R7, #0
	STR R7, R5, #-5
	LDR R3, R5, #-4
	CMP R3, R7
	BRn L38_tetris
	LDR R7, R5, #-1
	STR R7, R5, #-6
	LDR R3, R5, #-5
	CMP R7, R3
	BRn L38_tetris
	CONST R7, #16
	LDR R3, R5, #-6
	CMP R3, R7
	BRn L34_tetris
L38_tetris
	LDR R7, R5, #3
	CONST R3, #0
	HICONST R3, #128
	AND R7, R7, R3
	CONST R3, #0
	CMP R7, R3
	BRz L34_tetris
	CONST R7, #1
	JMP L25_tetris
L34_tetris
	CONST R7, #0
	LDR R3, R5, #3
	CONST R2, #0
	HICONST R2, #128
	AND R3, R3, R2
	CMP R3, R7
	BRz L39_tetris
	LDR R3, R5, #-1
	LDR R2, R5, #-2
	SLL R2, R2, #4
	LEA R1, cells
	ADD R2, R2, R1
	ADD R3, R3, R2
	LDR R3, R3, #0
	CMP R3, R7
	BRz L39_tetris
	CONST R7, #1
	JMP L25_tetris
L39_tetris
	LDR R7, R5, #3
	SLL R7, R7, #1
	STR R7, R5, #3
L31_tetris
	LDR R7, R5, #-1
	ADD R7, R7, #1
	STR R7, R5, #-1
L33_tetris
	LDR R7, R5, #-1
	LDR R3, R5, #5
	ADD R3, R3, #4
	CMP R7, R3
	BRn L30_tetris
L27_tetris
	LDR R7, R5, #-2
	ADD R7, R7, #1
	STR R7, R5, #-2
L29_tetris
	LDR R7, R5, #-2
	LDR R3, R5, #4
	ADD R3, R3, #4
	CMP R7, R3
	BRn L26_tetris
	LDR R7, R5, #-3
L25_tetris
	;; epilogue
	ADD R6, R5, #0	;; pop locals off stack
	ADD R6, R6, #3	;; free space for return address, base pointer, and return value
	STR R7, R6, #-1	;; store return value
	LDR R5, R6, #-3	;; restore base pointer
	LDR R7, R6, #-2	;; restore return address
	RET

;;;;;;;;;;;;;;;;;;;;;;;;;;;;draw_shape;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		.CODE
		.FALIGN
draw_shape
	;; prologue
	STR R7, R6, #-2	;; save return address
	STR R5, R6, #-3	;; save base pointer
	ADD R6, R6, #-3
	ADD R5, R6, #0
	ADD R6, R6, #-2	;; allocate stack space for local variables
	;; function body
	LDR R7, R5, #4
	STR R7, R5, #-2
	JMP L45_tetris
L42_tetris
	LDR R7, R5, #5
	STR R7, R5, #-1
	JMP L49_tetris
L46_tetris
	LDR R7, R5, #3
	CONST R3, #0
	HICONST R3, #128
	AND R7, R7, R3
	CONST R3, #0
	CMP R7, R3
	BRz L50_tetris
	LDR R7, R5, #-1
	LDR R3, R5, #-2
	SLL R3, R3, #4
	LEA R2, cells
	ADD R3, R3, R2
	ADD R7, R7, R3
	LDR R3, R5, #6
	STR R3, R7, #0
L50_tetris
	LDR R7, R5, #3
	SLL R7, R7, #1
	STR R7, R5, #3
L47_tetris
	LDR R7, R5, #-1
	ADD R7, R7, #1
	STR R7, R5, #-1
L49_tetris
	LDR R7, R5, #-1
	LDR R3, R5, #5
	ADD R3, R3, #4
	CMP R7, R3
	BRn L46_tetris
L43_tetris
	LDR R7, R5, #-2
	ADD R7, R7, #1
	STR R7, R5, #-2
L45_tetris
	LDR R7, R5, #-2
	LDR R3, R5, #4
	ADD R3, R3, #4
	CMP R7, R3
	BRn L42_tetris
L41_tetris
	;; epilogue
	ADD R6, R5, #0	;; pop locals off stack
	ADD R6, R6, #3	;; free space for return address, base pointer, and return value
	STR R7, R6, #-1	;; store return value
	LDR R5, R6, #-3	;; restore base pointer
	LDR R7, R6, #-2	;; restore return address
	RET

;;;;;;;;;;;;;;;;;;;;;;;;;;;;remove_filled_rows;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		.CODE
		.FALIGN
remove_filled_rows
	;; prologue
	STR R7, R6, #-2	;; save return address
	STR R5, R6, #-3	;; save base pointer
	ADD R6, R6, #-3
	ADD R5, R6, #0
	ADD R6, R6, #-5	;; allocate stack space for local variables
	;; function body
	CONST R7, #14
	STR R7, R5, #-3
L53_tetris
	CONST R7, #0
	STR R7, R5, #-1
	STR R7, R5, #-4
	STR R7, R5, #-5
	JMP L60_tetris
L57_tetris
	LDR R7, R5, #-1
	LDR R3, R5, #-3
	SLL R3, R3, #4
	LEA R2, cells
	ADD R3, R3, R2
	ADD R7, R7, R3
	LDR R7, R7, #0
	CONST R3, #0
	CMP R7, R3
	BRz L61_tetris
	LDR R7, R5, #-4
	ADD R7, R7, #1
	STR R7, R5, #-4
L61_tetris
L58_tetris
	LDR R7, R5, #-1
	ADD R7, R7, #1
	STR R7, R5, #-1
L60_tetris
	LDR R7, R5, #-1
	CONST R3, #16
	CMP R7, R3
	BRn L57_tetris
	LDR R7, R5, #-4
	CONST R3, #16
	CMP R7, R3
	BRnp L63_tetris
	CONST R7, #1
	STR R7, R5, #-5
L63_tetris
	LDR R7, R5, #-5
	CONST R3, #0
	CMP R7, R3
	BRz L65_tetris
	LEA R7, score
	LDR R3, R7, #0
	ADD R3, R3, #1
	STR R3, R7, #0
	LDR R7, R5, #-3
	STR R7, R5, #-2
	JMP L70_tetris
L67_tetris
	CONST R7, #0
	STR R7, R5, #-1
L71_tetris
	LDR R7, R5, #-1
	LDR R3, R5, #-2
	SLL R3, R3, #4
	LEA R2, cells
	ADD R1, R3, R2
	ADD R1, R7, R1
	ADD R2, R2, #-16
	ADD R3, R3, R2
	ADD R7, R7, R3
	LDR R7, R7, #0
	STR R7, R1, #0
L72_tetris
	LDR R7, R5, #-1
	ADD R7, R7, #1
	STR R7, R5, #-1
	LDR R7, R5, #-1
	CONST R3, #16
	CMP R7, R3
	BRn L71_tetris
L68_tetris
	LDR R7, R5, #-2
	ADD R7, R7, #-1
	STR R7, R5, #-2
L70_tetris
	LDR R7, R5, #-2
	CONST R3, #0
	CMP R7, R3
	BRp L67_tetris
	LDR R7, R5, #-3
	ADD R7, R7, #1
	STR R7, R5, #-3
L65_tetris
L54_tetris
	LDR R7, R5, #-3
	ADD R7, R7, #-1
	STR R7, R5, #-3
	LDR R7, R5, #-3
	CONST R3, #-1
	CMP R7, R3
	BRp L53_tetris
L52_tetris
	;; epilogue
	ADD R6, R5, #0	;; pop locals off stack
	ADD R6, R6, #3	;; free space for return address, base pointer, and return value
	STR R7, R6, #-1	;; store return value
	LDR R5, R6, #-3	;; restore base pointer
	LDR R7, R6, #-2	;; restore return address
	RET

;;;;;;;;;;;;;;;;;;;;;;;;;;;;main;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		.CODE
		.FALIGN
main
	;; prologue
	STR R7, R6, #-2	;; save return address
	STR R5, R6, #-3	;; save base pointer
	ADD R6, R6, #-3
	ADD R5, R6, #0
	ADD R6, R6, #-12	;; allocate stack space for local variables
	;; function body
	CONST R7, #0
	STR R7, R5, #-3
	JSR clear_tetris_array
	ADD R6, R6, #0	;; free space for arguments
	JSR redraw
	ADD R6, R6, #0	;; free space for arguments
	LEA R7, L76_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
	LEA R7, L77_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
	LEA R7, L78_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
	LEA R7, L79_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
	LEA R7, L80_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
	LEA R7, L81_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
	CONST R7, #-1
	STR R7, R5, #-1
	JMP L83_tetris
L82_tetris
	JSR lc4_get_event
	LDR R7, R6, #-1	;; grab return value
	ADD R6, R6, #0	;; free space for arguments
	STR R7, R5, #-2
	LDR R7, R5, #-3
	CONST R3, #0
	CMP R7, R3
	BRnp L85_tetris
	LDR R7, R5, #-2
	CONST R3, #32
	CMP R7, R3
	BRnp L85_tetris
	JSR clear_tetris_array
	ADD R6, R6, #0	;; free space for arguments
	CONST R7, #-1
	STR R7, R5, #-1
	CONST R7, #1
	STR R7, R5, #-3
	LEA R7, L87_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
L85_tetris
	LDR R7, R5, #-3
	CONST R3, #0
	CMP R7, R3
	BRz L88_tetris
	LDR R7, R5, #-1
	CONST R3, #-1
	CMP R7, R3
	BRnp L90_tetris
	CONST R7, #0
	STR R7, R5, #-1
	CONST R7, #8
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_rand_power2
	LDR R7, R6, #-1	;; grab return value
	ADD R6, R6, #1	;; free space for arguments
	STR R7, R5, #-10
	CONST R3, #4
	ADD R6, R6, #-1
	STR R3, R6, #0
	JSR lc4_rand_power2
	LDR R7, R6, #-1	;; grab return value
	ADD R6, R6, #1	;; free space for arguments
	STR R7, R5, #-11
	CONST R3, #2
	ADD R6, R6, #-1
	STR R3, R6, #0
	JSR lc4_rand_power2
	LDR R7, R6, #-1	;; grab return value
	ADD R6, R6, #1	;; free space for arguments
	LDR R3, R5, #-10
	LDR R2, R5, #-11
	ADD R3, R3, R2
	ADD R7, R3, R7
	STR R7, R5, #-4
	CONST R7, #4
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_rand_power2
	LDR R7, R6, #-1	;; grab return value
	ADD R6, R6, #1	;; free space for arguments
	STR R7, R5, #-12
	CONST R3, #4
	ADD R6, R6, #-1
	STR R3, R6, #0
	JSR lc4_rand_power2
	LDR R7, R6, #-1	;; grab return value
	ADD R6, R6, #1	;; free space for arguments
	LDR R3, R5, #-12
	ADD R7, R3, R7
	STR R7, R5, #-5
	CONST R7, #4
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_rand_power2
	LDR R7, R6, #-1	;; grab return value
	ADD R6, R6, #1	;; free space for arguments
	STR R7, R5, #-6
	LDR R7, R5, #-4
	ADD R6, R6, #-1
	STR R7, R6, #0
	LDR R7, R5, #-1
	ADD R6, R6, #-1
	STR R7, R6, #0
	LDR R7, R5, #-5
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR test_for_collision
	LDR R7, R6, #-1	;; grab return value
	ADD R6, R6, #3	;; free space for arguments
	CONST R3, #0
	CMP R7, R3
	BRz L92_tetris
	CONST R7, #0
	STR R7, R5, #-3
	LEA R7, L94_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
	LEA R7, score
	LDR R7, R7, #0
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR print_num
	ADD R6, R6, #1	;; free space for arguments
	LEA R7, L95_tetris
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR lc4_puts
	ADD R6, R6, #1	;; free space for arguments
L92_tetris
L90_tetris
	LDR R7, R5, #-4
	STR R7, R5, #-7
	LDR R7, R5, #-1
	STR R7, R5, #-9
	LDR R7, R5, #-6
	STR R7, R5, #-8
	LDR R7, R5, #-2
	CONST R3, #106
	CMP R7, R3
	BRnp L96_tetris
	LDR R7, R5, #-4
	ADD R7, R7, #-1
	STR R7, R5, #-7
	JMP L97_tetris
L96_tetris
	LDR R7, R5, #-2
	CONST R3, #107
	CMP R7, R3
	BRnp L98_tetris
	LDR R7, R5, #-4
	ADD R7, R7, #1
	STR R7, R5, #-7
	JMP L99_tetris
L98_tetris
	LDR R7, R5, #-2
	CONST R3, #97
	CMP R7, R3
	BRnp L100_tetris
	LDR R7, R5, #-6
	ADD R7, R7, #-1
	AND R7, R7, #3
	STR R7, R5, #-8
	JMP L101_tetris
L100_tetris
	LDR R7, R5, #-2
	CONST R3, #115
	CMP R7, R3
	BRnp L102_tetris
	LDR R7, R5, #-6
	ADD R7, R7, #1
	AND R7, R7, #3
	STR R7, R5, #-8
	JMP L103_tetris
L102_tetris
	LDR R7, R5, #-1
	ADD R7, R7, #1
	STR R7, R5, #-9
L103_tetris
L101_tetris
L99_tetris
L97_tetris
	CONST R7, #0
	ADD R6, R6, #-1
	STR R7, R6, #0
	LDR R7, R5, #-4
	ADD R6, R6, #-1
	STR R7, R6, #0
	LDR R7, R5, #-1
	ADD R6, R6, #-1
	STR R7, R6, #0
	LDR R7, R5, #-6
	LDR R3, R5, #-5
	SLL R3, R3, #2
	LEA R2, shapes
	ADD R3, R3, R2
	ADD R7, R7, R3
	LDR R7, R7, #0
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR draw_shape
	ADD R6, R6, #4	;; free space for arguments
	LDR R7, R5, #-7
	ADD R6, R6, #-1
	STR R7, R6, #0
	LDR R7, R5, #-9
	ADD R6, R6, #-1
	STR R7, R6, #0
	LDR R7, R5, #-8
	LDR R3, R5, #-5
	SLL R3, R3, #2
	LEA R2, shapes
	ADD R3, R3, R2
	ADD R7, R7, R3
	LDR R7, R7, #0
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR test_for_collision
	LDR R7, R6, #-1	;; grab return value
	ADD R6, R6, #3	;; free space for arguments
	CONST R3, #0
	CMP R7, R3
	BRnp L104_tetris
	LDR R7, R5, #-9
	STR R7, R5, #-1
	LDR R7, R5, #-7
	STR R7, R5, #-4
	LDR R7, R5, #-8
	STR R7, R5, #-6
	LDR R7, R5, #-5
	LEA R3, colors
	ADD R3, R7, R3
	LDR R3, R3, #0
	ADD R6, R6, #-1
	STR R3, R6, #0
	LDR R3, R5, #-4
	ADD R6, R6, #-1
	STR R3, R6, #0
	LDR R3, R5, #-1
	ADD R6, R6, #-1
	STR R3, R6, #0
	LDR R3, R5, #-6
	SLL R7, R7, #2
	LEA R2, shapes
	ADD R7, R7, R2
	ADD R7, R3, R7
	LDR R7, R7, #0
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR draw_shape
	ADD R6, R6, #4	;; free space for arguments
	JMP L105_tetris
L104_tetris
	LDR R7, R5, #-5
	LEA R3, colors
	ADD R3, R7, R3
	LDR R3, R3, #0
	ADD R6, R6, #-1
	STR R3, R6, #0
	LDR R3, R5, #-4
	ADD R6, R6, #-1
	STR R3, R6, #0
	LDR R3, R5, #-1
	ADD R6, R6, #-1
	STR R3, R6, #0
	LDR R3, R5, #-6
	SLL R7, R7, #2
	LEA R2, shapes
	ADD R7, R7, R2
	ADD R7, R3, R7
	LDR R7, R7, #0
	ADD R6, R6, #-1
	STR R7, R6, #0
	JSR draw_shape
	ADD R6, R6, #4	;; free space for arguments
	LDR R7, R5, #-2
	CONST R3, #0
	CMP R7, R3
	BRnp L106_tetris
	JSR remove_filled_rows
	ADD R6, R6, #0	;; free space for arguments
	CONST R7, #-1
	STR R7, R5, #-1
L106_tetris
L105_tetris
	JSR redraw
	ADD R6, R6, #0	;; free space for arguments
L88_tetris
L83_tetris
	JMP L82_tetris
	CONST R7, #0
L75_tetris
	;; epilogue
	ADD R6, R5, #0	;; pop locals off stack
	ADD R6, R6, #3	;; free space for return address, base pointer, and return value
	STR R7, R6, #-1	;; store return value
	LDR R5, R6, #-3	;; restore base pointer
	LDR R7, R6, #-2	;; restore return address
	RET

		.DATA
cells 		.BLKW 240
		.DATA
L95_tetris 		.STRINGZ "Game Over\n"
		.DATA
L94_tetris 		.STRINGZ "Score:\n"
		.DATA
L87_tetris 		.STRINGZ "Game On!\n"
		.DATA
L81_tetris 		.STRINGZ "Press space bar to start\n"
		.DATA
L80_tetris 		.STRINGZ "Press a to rotate counter-clockwise\n"
		.DATA
L79_tetris 		.STRINGZ "Press s to rotate clockwise\n"
		.DATA
L78_tetris 		.STRINGZ "Press k to go right\n"
		.DATA
L77_tetris 		.STRINGZ "Press j to go left\n"
		.DATA
L76_tetris 		.STRINGZ "!!! Welcome to Tetris !!!\n"
		.DATA
L5_tetris 		.STRINGZ "\n"
		.DATA
L4_tetris 		.STRINGZ "0\n"
```

## File: `tetris_script`
```
clear
reset
as os os
as tetris libc tetris
ld os
ld tetris
```

## File: `tetris_script2`
```
clear
reset
as os os
as tetris2 libc tetris2
ld os
ld tetris2
```

