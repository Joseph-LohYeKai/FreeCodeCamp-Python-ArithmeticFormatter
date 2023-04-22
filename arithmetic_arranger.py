


def arithmetic_arranger(problems,Results=False):
    NoOfProblems=len(problems)
    if NoOfProblems>5:
        return "Error: Too many problems."
    First=[]
    Second=[]
    Lines=[]
    Total=[]

    for problem in problems:
        List=problem.split(" ")
        FirstNumber=List[0]
        Symbol=List[1]
        SecondNumber=List[2]
        if FirstNumber.isnumeric()==False or SecondNumber.isnumeric()==False:
            return "Error: Numbers must only contain digits."
            break
        if Symbol not in "+-":
            return "Error: Operator must be '+' or '-'."
            break
        if len(FirstNumber)>=5 or len(SecondNumber)>=5:
            return "Error: Numbers cannot be more than four digits."
            break
        TotalNo=eval(problem)
        #Getting the spaces infront, First line always got one more extra space to account for the operator
        DifferenceInLength=len(FirstNumber)-len(SecondNumber)
        if DifferenceInLength<0:
            DifferenceInLength=abs(DifferenceInLength)
            FirstNumber=' '*(DifferenceInLength+2)+FirstNumber
            SecondNumber=' '+SecondNumber
        elif DifferenceInLength>0:
            FirstNumber='  '+FirstNumber
            SecondNumber=' '*(DifferenceInLength+1)+SecondNumber
        
        else:
            FirstNumber='  '+FirstNumber
            SecondNumber=' '+SecondNumber
        

        SecondLine=Symbol+SecondNumber
        NoOfLines='-'*len(SecondLine)
        DifferenceInLengthTotal=len(SecondLine)-len(str(TotalNo))
        TotalNo=' '*(DifferenceInLengthTotal)+str(TotalNo)

        First.append(FirstNumber)
        Second.append(SecondLine)
        Lines.append(NoOfLines)
        Total.append(TotalNo)
    First='    '.join(First)
    Second='    '.join(Second)
    Lines='    '.join(Lines)
    ArrangedProblem=First+ '\n' +Second+ '\n'+ Lines
    if Results==True:
        Total='    '.join(Total)
        ArrangedProblem=ArrangedProblem+'\n'+Total
    return ArrangedProblem

    
        
    



print(arithmetic_arranger(['24 + 21', '3801 - 2', '45 + 43', '123 + 49']))
