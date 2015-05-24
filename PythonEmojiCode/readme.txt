Use for conver from unicode string to emoji code

For a lot of place doesn't support emoji code, this would raise exceptions.
We can just convert emoji code to unicode string 
(in iOS, NSUTF16StringEncoding = NSUnicodeStringEncoding per NSString.h)
TODO: paste ios convert code here.

This python is used for convert the unicode emoji string back to emoji code.
