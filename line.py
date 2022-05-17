#coding: utf-8
import random

servers = [] 
name_str = '{\"name\":\"'
server_str = '\",\"server\":\"'
type_str ='\",\"type\"'

lines = [] 

with open("proxy2.txt","r",encoding="UTF-8") as x: 
        for line in x:
                nameaddr = line.find(name_str)
                
                if (nameaddr>=0):
                        #replace "- "
                        #print(line)
                        nameaddr += len(name_str)
                        serveraddr = line.find(server_str, nameaddr)
                        serveraddr2 = serveraddr+len(server_str)
                        typeaddr = line.find(type_str, serveraddr)

                        
                        line1 = line[0:nameaddr]+line[serveraddr2:typeaddr].strip()+str(random.randint(0,9999))+line[serveraddr:]
                else:
                        line1 = line

                lines.append(line1)
                print(line1)         
        x.close()

s = ''.join(lines)

with open("proxy.txt","w",encoding="UTF-8") as z: 
        z.write(s) 
        z.close()  
