class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res  = []
        for i in operations:
            if i!="C" and i!="D" and i!="+":
                res.append(int(i))
            else:
                match i:
                    case "C":
                        res.pop()
                    case "D":
                        res.append(res[-1]*2)
                    case "+":
                        res.append(res[-1] + res[-2])

        return sum(res)