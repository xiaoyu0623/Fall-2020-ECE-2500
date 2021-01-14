.globl main
.data
.text
main:	
	addi $t0, $zero, 12
	addi $t1, $zero, 780
	
	addi $t4, $zero, 1
	addi $t5, $zero, 0
	addi $t6, $zero, 1
	
	start: beq $t0, $t5, u_0				# if u = 0
	beq $t1, $0, v_0   						# if v = 0
	beq $t0, $t1, u_v  						# if u = v
	
	andi $t0, $t0, 0x01 					#check u even or odd
	beq $t0, $t5, u_even 					# if u is even
	beq $t0, $t6, u_odd 					#if u is odd

	u_even: andi $t1, $t1, 0x01 			#check v even or odd
	beq $t1, $t5, uv_even 					# if v is even 
	beq $t1, $t6, u_even_v_odd 				# if v is odd
	
	u_odd: andi $t1, $t1, 0x01 				#check v even or odd
	beq $t1, $t5, u_odd_v_even 				# if v is even 
	beq $t1, $t6, uv_odd 					# if v is odd
	
	uv_odd: slt, $t3, $t0, $t1 				#check u>v or v>u
	beq $t3, $t5, v_less 					# if u>v, $t3=0
	beq $t3, $t6, u_less 					# if u<v, $t3=1
	
	u_0: addi $t2, $t1, 0 					# if u = 0
	beq $t4, $t6, return                    # t4 = 1, not need x2
	beq $t2, $t2, multi						# t4 not equal 1, need x2	
	
	
	v_0: addi $t2, $t0, 0					# if v = 0
	beq, $t4, $t6, return					# t4 = 1, not need x2
	beq $t2, $t2, multi						# t4 not equal 1, need x2
	
	u_v: addi $t2, $t0, 0					# if u = v
	beq $t4, $t6, return					# t4 = 1, not need x2
	beq $t2, $t2, multi						# t4 not equal 1, need x2	
	
	uv_even: srl $t0, $t0, 1    			# u/2
	srl $t1, $t1, 1    						# v/2
	sll $t4, $t4, 1							# multi by 2
	beq $t2, $t2, start
	
	u_even_v_odd: srl $t0, $t0, 1 			# u = u/2
	beq $t2, $t2, start

	
	u_odd_v_even: srl $t1, $t1, 1 			# v = v/2
	beq $t2, $t2, start

	
	v_less: sub $t0, $t0, $t1 				# u = u-v
	srl $t0, $t0, 1 						# u = (u-v)/2
	beq $t2, $t2, start

	
	u_less: sub $t3, $t1, $t0 				# t3 = v-u
	srl $t3, $t3, 1							# t3 = (v-u)/2
	addi $t1, $t0, 0
	addi $t0, $t3, 0
	beq $t2, $t2, start
	
	multi: srl $t4, $t4, 1					# need v0 = v0 * 2
	sll $t2, $t2, 1							
	beq $t4, $t6, return
	beq $t4, $t4, multi
	
	
	return: done: beq $t0, $t0, done