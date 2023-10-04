class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        i = 0
        while i < len(command):
            if command[i] == "G":
                res += "G"
                i += 1
            elif i < len(command) - 1 and command[i:i + 2] == "()":
                res += "o"
                i += 2
            elif command[i] == ")":
                i += 1
            elif i < len(command) - 3 and command[i:i + 4] == "(al)":
                res += "al"
                i += 4
            else:
                res += command[i]
                i += 1

        return res

