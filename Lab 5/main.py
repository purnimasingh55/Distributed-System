''''
global clock:
Physical clock:
    syncronising the clocks with diff time
    there are demerits

clocks tells the time msg is recvd
all clocks are not syncronised properly

we need to create logical/relative clock :
    two mwthods:
        1. Logiical lempered clock



             try to understand when the event occured
             a->b means a happened before b
             for single machine no syncronization is required bcoz they run independantly
             rule to get correct ordering
                 1.Cp1(a)<Cp1(b) here a and b events had already occured bcoz time can't be reversed
                 2.Cp1(a)<Cp2(b) will always be true
             for computing the events of teo machine':
                 Cp(b) = max(Cp1(a),Cp2(b))+1
        2. Vector clock

'''