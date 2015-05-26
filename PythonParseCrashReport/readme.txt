Use for parse shrink crash report.

How to get shrink crash report
1. 使用 _dyld_register_func_for_add_image 来获取模块加载地址
2. 使用 NSSetUncaughtExceptionHandler 来获取未捕获异常的 NSException
3. 使用 NSException 的 callStackSymbols 来获得异常的 call stack
4. 使用 ([^\\s]*)\\s+(0x[0-9a-f]*) 正则表达式来获得 call stack 的模块名和地址
5. 使用 strtoull 来将获得地址转换为16进制数并进行运算
6. 将新的地址填入之前的地址中
7. 使用 [[[NSBundle mainBundle] infoDictionary] objectForKey:@"CFBundleShortVersionString"]获得软件 Build Version
8. 使用 [[UIDevice currentDevice] systemVersion] 获得系统版本
9. 使用 struct utsname systemInfo; uname(&systemInfo); systemInfo.machine 获得设备信息
10. 使用 sysctl({CTL_KERN, KERN_OSVERSION}) 获得 osBuildVersion
11. 用 Call stack address 减去 load address, 这样能够获取到基于 load address 的真实的 call stack 的地址

This python is doing:
12. atos -arch arcitecture -o executable -l loadAddress(0x1) address(Call stack address - load address) + 0x1
