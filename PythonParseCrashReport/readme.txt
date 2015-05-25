Use for parse shrink crash report.

How to get shrink crash report
1. Use "_dyld_register_func_for_add_image" to get all image load address
2. Use NSException:callStackSymbols to get call stack
3. Call stack address minus load address, and get rid of all load image address from crash report
