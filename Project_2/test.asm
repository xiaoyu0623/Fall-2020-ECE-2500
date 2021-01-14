#"u in $a0; v in $a1, final in $v0"
#"registers begin at $t0"
#"sll; srl;sub;subi;slt;or;ori;beq;bne;add;addi;and;andi;lui"
.globl main
.data
.text
main:	
	addi $a0, $zero, 12
	addi $a1, $zero, 780
	
	jal binaryGCD
	addi $s1, $v0, 0
	
	
	ori $v0, $0, 10
	syscall
	
binaryGCD: 
	beq $a0, $0, Label_u0   # "if u = 0"
	Label_u0 : addi $v0, $a0, 0   # "return v"

	beq $a1, $0, Label_v0  # "if v = 0"
	Label_v0: addi $v0, $a1, 0 # "return u"

	beq $a0, $a1, Label_uv  #"if u = v"
	Label_uv: addi $v0, $a0, 0 #"return u"


	andi $t0, $a0, 0x01 #check u even or odd
	beq $t0, $zero, Else # if u is even
	andi $t1, $a1, 0x01 #check v even or odd
	beq $t1, $zero, Else_v # if u and v is even 
	#"return 2*gcd(u/2, v/2)"
	srl $t2, $a0, 1 # u/2
	srl $t3, $a1, 1 # v/2
	addi $a0, $t2, 0 #a0 = u/2
	addi $a1, $t3, 0 #a1 = v/2
	jal binaryGCD
	sll $v0, $v0, 1 #2*(gcd)
		   
	# return gcd(u/2, v) for if u even, v odd
    Else_v: srl $t2, $a0, 1 #u/2
	addi $a0, $t2, 0 # a0 = u/2
	jal binaryGCD
	#addi $v0, $v0, 0 #return $v0

    Else: andi $t1, $a1, 0x01 #check v is even or odd
	beq $t1, $zero, Else_v2 # "v is even"
    #"return gcd(u, v/2)"
	srl $t3, $a1, 1 # v/2
	addi $a1, $t3, 0 # a1 = v/2
	jal binaryGCD
	#addi $v0, $v0, 0 #return $v0
	
	
	Else_v2: slt, $t3, $a0, $a1  #both u and v is not even
	beq, $t3, $zero, unequalu_v #a0>a1 ,u>v
	#"return gcd((u-v)/2, v)"
	sub $t4, $a0, $a1 # u-v
	srl $t4, $t4, 1 #(u-v)/2
	addi $a0, $t4, 0 # u = (u-v)/2
	jal binaryGCD
	addi $v0, $v0, 0 # return $v0
	
	#"return gcd(v-u)/2, u)" v > u
	unequalu_v: sub $t4, $a1, $a0
	srl $t4, $t4, 1 #(v-u)/2
	addi $a1, $a0, 0 # v = u
	addi $a0, $t4, 0 # u = (v-u)/2
	jal binaryGCD
	#addi $v0, $v0, 0 #return $v0
	
	jr $ra


