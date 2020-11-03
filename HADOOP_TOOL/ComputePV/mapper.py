#!/usr/bin python

import sys

def func():
    for line in sys.stdin:
        pv = 0
        has_clk = 0
        sum_total_clk = 0
        pos = 0
        if line == '\n':
            line = line.strip('\n')
        line = line.strip()
        line = line.split('\0')
        
        if line[11] == '1':
            pv += 1
            sum_total_clk += int(line[33])
            if sum_total_clk > 0:
                has_clk += 1
                
            clk_detail = line[39]
            clk_detail = clk_detail.split(',')
            if len(clk_detail) >= 7:
                pos = int(clk_detail[6])
                if pos in range(1,11):
                    i = pos
                    j = 10 + pos
                    k = 20 + pos
                    print "%s\t%s" % (i, pv)
                    print "%s\t%s" % (j, has_clk)
                    print "%s\t%s" % (k, sum_total_clk)
            
        print "pv\t%s" % pv
        print "has_clk\t%s" % has_clk
        print "sum_total_clk\t%s" % sum_total_clk
    
if __name__ == "__main__":
    func()