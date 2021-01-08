class Solution:
    def interpret(self, command: str) -> str:
        l = len(command)
        new = ''
        for i in range(l):
            if command[i]=='(' and command[i+1]==')':
                new += 'o'
            elif command[i]=='(' or command[i]==')':
                pass
            else:
                new += command[i]
        return new