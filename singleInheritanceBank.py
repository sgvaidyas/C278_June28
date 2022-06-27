class Bank:
    def __init__(self):
        self.bankName = "Chase"
        self.bankMain = "Houston"
        self.bankId = 1

    def setBankData(self, bankName, bankMain, bankId):
        self.bankName = bankName
        self.bankMain = bankMain
        self.bankId = bankId

    def display(self):
        print("BankName = {0}\t BankMainLoc = {1}\t BankId = {2}".format(self.bankName,self.bankMain,self.bankId))

class HDFC(Bank):
    def __init__(self):
        super().__init__()
        self.branchId = 0
        self.branchName = ""
        self.branchLocation = ""
        self.branch_Code = 0

    def setHDFCData(self, branchId, branchName, branchLocation, branch_Code):
        self.branchId = branchId
        self.branchName = branchName
        self.branchLocation = branchLocation
        self.branch_Code = branch_Code

    def display(self):
        super().display()
        print("branchId = " ,self.branchId)
        print("branchName = " ,self.branchName)
        print("branchLocation = ", self.branchLocation)
        print("branch_Code = ",self.branch_Code)


branch = HDFC()
branch.setHDFCData("1","Branch West", "Redding","223")
branch.display()
