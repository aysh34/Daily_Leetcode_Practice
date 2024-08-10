class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        op = {
            "+" : lambda x,y :x+y ,            
            "-" : lambda x,y :x-y ,            
            "*" : lambda x,y :x*y ,            
            "/" : lambda x,y :x/y            
        }
        for i in tokens:
            if i != "+" and i != "-" and i != "*" and i != "/":
                s.append(int(i))           
            elif s and i == "+":
                v1 = s.pop()
                v2 = s.pop()
                # sm = v2 + v1
                # s.append(sm)
                s.append(op["+"](v2,v1))
            elif s and i == "*":
                v1 = s.pop()
                v2 = s.pop()
                ml = v2 * v1
                s.append(ml)
            elif s and i == "-":
                v1 = s.pop()
                v2 = s.pop()
                mn = v2 - v1
                s.append(mn)
            elif s and i == "/":
                v1 = s.pop()
                v2 = s.pop()
                dv = int(v2 / v1)  # int() --> for truncating towards zero
                s.append(dv)
        return s[0]

                
