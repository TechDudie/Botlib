class CMD:
    def __init__(self, name:str , desp:str , startMesg:bool = True , customMesg:str = f"Hi i m a") -> None:
        self.name = name
        self.desp =  desp
        self.customMesg = customMesg
        self.commands = {}
    def registerCommand(self,cmd,function=None):
        if type(cmd) == str:
            self.commands[cmd] = function
        if type(cmd) == dict:
            for i in cmd:
                self.commands[i] = cmd[i]
    def onMessage(self , ctx:str):
            for i in self.command:
                if ctx.startswith(i):
                    self.command[i](ctx.split())
                    return

    def run(self):
        while True:
            req = str(input("> "))
            if  req != "":
                self.onMessage(req)
class Discord:
    pass
class IRC:
    pass
