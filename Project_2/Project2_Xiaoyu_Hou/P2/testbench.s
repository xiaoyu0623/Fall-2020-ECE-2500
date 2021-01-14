.globl main
.data
.text
main:	
	addi $a0, $zero,12
	addi $a1, $zero,780
	jal binaryGCD
	addi $s1, $v0, 0
	
	addi $a0, $zero,780
	addi $a1, $zero,12
	jal binaryGCD
	addi $s2, $v0, 0	
	
	addi $a0, $zero,2048
	addi $a1, $zero,16384
	jal binaryGCD
	addi $s3, $v0, 0
	
	lui $a0, 0x1DCD
	ori $a0, $a0, 0x794F
	addi $a1, $zero, 709
	jal binaryGCD
	addi $s4, $v0, 0
	
	lui $a0, 0x0008 		
	ori $a0, $a0, 0x75A0
	lui $a1, 0x0009
	ori $a1, $a1, 0xFF60
	jal binaryGCD
	addi $s5, $v0, 0		

	lui $a0, 0x0010			
	ori $a0, $a0, 0x0000
	lui $a1, 0x0002
	ori $a1, $a1, 0x0000
	jal binaryGCD
	addi $s6, $v0, 0		

	addi $a0, $zero,0		
	addi $a1, $zero,12345
	jal binaryGCD
	addi $s7, $v0, 0		
	
	ori $v0, $0, 10
	syscall
	
binaryGCD:
	addi $t4, $zero, 1
	addi $t5, $zero, 0
	addi $t6, $zero, 1
	
	start: beq $a0, $t5, u_0				# if u = 0
	beq $a1, $0, v_0   					# if v = 0
	beq $a0, $a1, u_v  					# if u = v
	
	andi $t0, $a0, 0x01 					#check u even or odd
	beq $t0, $t5, u_even 					# if u is even
	beq $t0, $t6, u_odd 					#if u is odd

	u_even: andi $t1, $a1, 0x01 				#check v even or odd
	beq $t1, $t5, uv_even 					# if v is even 
	beq $t1, $t6, u_even_v_odd 				# if v is odd
	
	u_odd: andi $t1, $a1, 0x01 				#check v even or odd
	beq $t1, $t5, u_odd_v_even 				# if v is even 
	beq $t1, $t6, uv_odd 					# if v is odd
	
	uv_odd: slt, $t2, $a0, $a1 				#check u>v or v>u
	beq $t2, $t5, v_less 					# if u>v, $t2=0
	beq $t2, $t6, u_less 					# if u<v, $t2=1
	
	u_0: addi $v0, $a1, 0 					# if u = 0
	beq $t4, $t6, return                    		# t4 = 1, not need x2
	beq $v0, $v0, multi					# t4 not equal 1, need x2	
	
	
	v_0: addi $v0, $a0, 0					# if v = 0
	beq, $t4, $t6, return					# t4 = 1, not need x2
	beq $v0, $v0, multi					# t4 not equal 1, need x2
	
	u_v: addi $v0, $a0, 0					# if u = v
	beq $t4, $t6, return					# t4 = 1, not need x2
	beq $v0, $v0, multi					# t4 not equal 1, need x2	
	
	uv_even: srl $a0, $a0, 1    				# u/2
	srl $a1, $a1, 1    					# v/2
	sll $t4, $t4, 1						# multi by 2
	beq $v0, $v0, start
	
	u_even_v_odd: srl $a0, $a0, 1 				# u = u/2
	beq $v0, $v0, start

	
	u_odd_v_even: srl $a1, $a1, 1 				# v = v/2
	beq $v0, $v0, start

	
	v_less: sub $a0, $a0, $a1 				# u = u-v
	srl $a0, $a0, 1 					# u = (u-v)/2
	beq $v0, $v0, start

	
	u_less: sub $t3, $a1, $a0 				# t3 = v-u
	srl $t3, $t3, 1						# t3 = (v-u)/2
	addi $a1, $a0, 0
	addi $a0, $t3, 0
	beq $v0, $v0, start
	
	multi: srl $t4, $t4, 1					# need v0 = v0 * 2
	sll $v0, $v0, 1							
	beq $t4, $t6, return
	beq $t4, $t4, multi
	
	
	return: jr $ra