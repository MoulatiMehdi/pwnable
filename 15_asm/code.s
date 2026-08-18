	.text
	.file	"code.c"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$1056, %rsp                     # imm = 0x420
	movl	$0, -4(%rbp)
	movl	%edi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	movabsq	$.L.str, %rdi
	xorl	%esi, %esi
	movb	$0, %al
	callq	open
	movl	%eax, -1044(%rbp)
	movl	-1044(%rbp), %edi
	leaq	-1040(%rbp), %rsi
	movl	$1024, %edx                     # imm = 0x400
	callq	read
                                        # kill: def $eax killed $eax killed $rax
	movl	%eax, -1048(%rbp)
	leaq	-1040(%rbp), %rsi
	movslq	-1048(%rbp), %rdx
	movl	$1, %edi
	callq	write
	xorl	%eax, %eax
	addq	$1056, %rsp                     # imm = 0x420
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	.L.str,@object                  # @.str
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.str:
	.asciz	"this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong"
	.size	.L.str, 232

	.ident	"Ubuntu clang version 12.0.1-19ubuntu3"
	.section	".note.GNU-stack","",@progbits
	.addrsig
	.addrsig_sym open
	.addrsig_sym read
	.addrsig_sym write
