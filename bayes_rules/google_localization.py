# Uniform distribution
p = [0.2, 0.2, 0.2, 0.2, 0.2]
# p = [0, 1, 0, 0, 0]

# Grid of world
world = ['green', 'red', 'red', 'green', 'green']

# Measurement(The robot see red in the first measurement)
measurements = ['red', 'red']
motion = [1, 1]

pHit = 0.6 # Red
pMiss= 0.2 # Green

pExact = 0.8
pOverShoot = 0.1
pUnderShoot = 0.1

def sense(p, Z):
    q = []
    for i in range(len(p)):
        if Z == world[i]:
            q.append(p[i] * pHit)
        else:
            q.append(p[i] * pMiss)
    
    total = sum(q)
    for i in range(len(q)):
        q[i] /= total
        
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i - U) % len(p)]
        s = s + pOverShoot * p[(i-U-1) % len(p)]
        s = s + pUnderShoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

# for i in range(len(measurements)):
#     p = (sense(p, measurements[i]))
for i in range(len(measurements)):
    p = sense(p, measurements[i])    
    p = move(p, motion[i])
    
print(p)
