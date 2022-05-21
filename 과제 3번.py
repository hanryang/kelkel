port_1 = []
port_2 = []
port = {}

# 수정을 했어요

while True :
    a = input().split(" ")
    port_1 += a
    if int(port_1[len(port_1) - 1]) == 0 :
        break
while True :
    b = input().split(" ")
    port_2 += b
    if int(port_2[len(port_2) - 1]) == 0 :
        break
    
print(port_1)
print(port_2)

# 여기도 수정했어요

for i in range (0, len(port_1) - 1, 2) :
    port[int(port_1[i + 1])] = int(port_1[i])
for i in range (0, len(port_2) - 1, 2) :
    if int(port_2[i + 1]) in port :
        port[int(port_2[i + 1])] += int(port_2[i])
    else :
       port[int(port_2[i + 1])] = int(port_2[i])

print(port)

sorted_port = sorted(port.items())

print(sorted_port)

print("%dx^%d " %(int(sorted_port[len(port) - 1][1]), int(sorted_port[len(port) - 1][0])), end = '')
for i in range (len(port) - 2, -1, -1) :
    if sorted_port[i][0] != 0 :
        print("+ %dx^%d " %(int(sorted_port[i][1]), int(sorted_port[i][0])), end = '')
    elif sorted_port[i][0] == 0 :
        if sorted_port[i][1] != 0 :
            print("+ %d" %(int(sorted_port[i][1])))

    
    
