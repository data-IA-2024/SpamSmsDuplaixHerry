import pandas as pd


class TestBinaireResult:
    def __init__(self,EvaluatedDF:pd.DataFrame,dataName:str):
        self.dataName = dataName

        self.FP = len(EvaluatedDF[(EvaluatedDF["Result"]=="spam")&(EvaluatedDF["spam"]=="ham")].index)
        self.FN = len(EvaluatedDF[(EvaluatedDF["Result"]=="ham")&(EvaluatedDF["spam"]=="spam")].index)
        self.VP = len(EvaluatedDF[(EvaluatedDF["Result"]=="ham")&(EvaluatedDF["spam"]=="ham")].index)
        self.VN = len(EvaluatedDF[(EvaluatedDF["Result"]=="spam")&(EvaluatedDF["spam"]=="spam")].index)

        self.exactitude = (self.VN+self.VP)/(self.VN+self.FN+self.FP+self.VP)
        self.rappel = self.VP /(self.VP+self.FN)
        self.rappelN = self.VN/(self.VN+self.FP)
        self.precision = self.VP/(self.VP+self.FP)
        self.precisionN = self.VN/(self.VN+self.FN)
        self.F1Score = (2 * self.precision * self.rappel) / (self.precision + self.rappel)
        self.F1ScoreN = (2 * self.precisionN * self.rappelN) / (self.precisionN + self.rappelN)

    def printValues(self):
        print(f"Exactitude : {round(self.exactitude,2)}")
        print(f"Rappel : {round(self.rappel,2)}")
        print(f"Rappel négative: {round(self.rappelN,2)}")
        print(f"Precision : {round(self.precision,2)}")
        print(f"Précision négative: {round(self.precisionN,2)}")
        print(f"F1-Score : {round(self.F1Score,2)}")
        print(f"F1-Score Négatif: {round(self.F1ScoreN,2)}")