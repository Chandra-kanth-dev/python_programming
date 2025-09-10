from collections import Counter
def sort_string(s):
    d=Counter(s)
    d=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
    res=""
    for i in d:
        res+=i*d[i]
    print(res)
    
    
sort_string("chaaaannnnnnnnnnnnnnndddddddddddddddddddddddddpppppppppppppppppppppp")

    