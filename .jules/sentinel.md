# Sentinel Journal 🛡️

## 2025-05-08 - Command Injection in Makefile Project Initialization
**Vulnerability:** Command injection via the `NAME` variable in the `Makefile`. The `SOURCE` variable was defined using `$(shell echo ${NAME} | ... )`, which allows arbitrary command execution if `NAME` contains shell metacharacters or Make $(shell) syntax. Additionally, `sed` commands were using these variables unquoted.
**Learning:** Makefiles are often overlooked as a vector for command injection. When `$(shell ...)` or shell commands in targets use unquoted variables that can be overridden by the user, it creates a significant security risk.
**Prevention:** Avoid complex string manipulation and file renaming logic directly in the `Makefile` using shell commands when user input is involved. Use a dedicated script (like Python) with proper input validation and safe API calls to perform these tasks.
