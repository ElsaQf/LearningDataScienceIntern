#!/usr/bin python

import sys

res = {}

def func():
    for line in sys.stdin:
        item, count = line.split('\t')
        count = int(count)
        res[item] = res.get(item, 0) + count
        
    pv = res['pv']
    has_clk = res['has_clk']
    sum_total_clk = res['sum_total_clk']
    
    
    rate_has_clk = 0
    rate_has_clk_pos = 0
    ctr = 0
    ctr_pos = 0
    
    l_pv = [0,0,0,0,0,0,0,0,0,0]
    l_rate_has_clk = [0,0,0,0,0,0,0,0,0,0]
    l_ctr = [0,0,0,0,0,0,0,0,0,0]
    
    if pv > 0:
        rate_has_clk = float(has_clk) / float(pv)
        ctr = float(sum_total_clk) / float(pv)
    
    for i in range(1,11):
        j = str(i)
        k = str(i+10)
        t = str(i+20)
        
        pv_pos = float(res.get(j,0))
        has_clk_pos = float(res.get(k,0))
        sum_total_clk_pos = float(res.get(t,0))
        
        if pv_pos > 0:
            l_pv[i-1] = pv_pos
            l_rate_has_clk[i-1] = rate_has_clk / pv
            l_ctr[i-1] = sum_total_clk_pos / pv
    
    print "pv\t%s" % pv
    print "has_clk\t%s" % has_clk
    print "sum_total_clk\t%s" % sum_total_clk
    print "rate_has_clk\t%s" % rate_has_clk
    print "ctr\t%s" % ctr
    
    for i in l_pv:
        print "%s" % i
    for i in l_rate_has_clk:
        print "%s" % i
    for i in l_ctr:
        print "%s" % i

if __name__ == "__main__":
    func()