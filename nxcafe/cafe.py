class NxCafe():
    def __init__(SayingItNeedsAnArguemtn=False):
        #see if in right directory
        try:
            import nxcafe.cafe
        except ImportError:
            print("[NXCafe] ")
        try:
            import nxcafe.nodes.color
        except ImportError:
            print("[NXCafe] ")
        import nxcafe.nodes.color as cl
        import nxcafe.nodes.nxcs as fs
        print("\n"+cl.colors.green+"succesfully started NXCafe."+cl.colors.r+"\n")
    def CafeTestColoredText():
        import nxcafe.nodes.color as NXNode
        print(NXNode.colors.blue+"succesfully imported colored text node.",NXNode.colors.r)
class nxcs():
    def encode(file):
        import nxcafe.nodes.nxcs as NxCS
        with open(file, 'r') as F:
            data = F.read()
        if file.endswith(".nxcs"):
            lib = NxCS.V1 
        else:
            lib = NxCS.V1
        encoded_data = ''.join(lib.get(char, char) for char in data)
        return encoded_data
    def decode(file):
            import nxcafe.nodes.nxcs as NxCS
            with open(file, 'r') as F:
                data = F.read()
                encoded_string = data
            if file.endswith(".nxcs"):
                lib = NxCS.V1_
            else:
                lib = NxCS.V1_
            decoded_data = ''
            temp = ''
            for char in encoded_string:
                temp += char
                if temp in lib:
                    decoded_data += lib[temp]
                    temp = ''
            return decoded_data
    def get(array,id):
        if array.startswith("+"):
            array = array.split(';')
            return array[id]
    def getprint(array,id):
        if array.startswith("+"):
            array = array.split(';')
            print(array[id])
class utils():
    def getVersion():
        import nxcafe.cafe as self
        self.nxcs.getprint(self.nxcs.decode("nxcafe/data/nx.nxcs"),4)
    def getBranch():
        import nxcafe.cafe as self
        self.nxcs.getprint(self.nxcs.decode("nxcafe/data/nx.nxcs"),2)
    def clearScreen():
        import nxcafe.nodes.clearscreen as self
        self.clear()
    def clearNumbered(EndCount=15):
        import nxcafe.nodes.clearscreen as self
        if EndCount >= 500:
            EndCount = 500
        self.clear.numbered(EndCount)