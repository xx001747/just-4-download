#coding: utf-8
import time

servers = [] 
servername = []
start_str = '{\"name\":\"'
end_str = '\",\"server\"'
cn_str  = 'CN_'
hk_str  = 'HK_'
with open("proxy.txt","r",encoding="UTF-8") as x: 
        for line in x:
                cnCN_sp = line.find(cn_str)
                hkHK_sp = line.find(hk_str)
                start = line.find(start_str)
                if (start>=0 and cnCN_sp<0 and hkHK_sp<0):
                        #replace "- "
                        #print(line)
                        line1 = ' '+' '+line
                        servers.append(line1)
                        start += len(start_str)
                        #append server name
                        end = line.find(end_str, start)
                        if end >= 0:
                                #print(line[start:end].strip())
                                servername.append(line[start:end].strip())
        x.close() 
        
'''
for line in servers:
        print(line)
        
for line in servername:
        print(line)
'''
        
#======================================================================
lines = [] 
with open("proxy50.yml","r",encoding="UTF-8") as x: 
        for line in x: 
                lines.append(line) 
        x.close() 
        

#find start line
line = lines.index('external-controller: :9090\n')
#insert servers
for s in servers:
        lines.insert(line+2,s)
        
line = lines.index('  - name: 🔰 节点选择\n')
#insert servernae
for s in servername:
        lines.insert(line+4,'      - '+s+'\n')
        
line = lines.index('  - name: ♻️ 自动选择\n')
#insert servernae
for s in servername:
        lines.insert(line+5,'      - '+s+'\n')

'''     
line = lines.index('  - name: 🌍 国外媒体\n')
#insert servernae
for s in servername:
        lines.insert(line+6,'      - '+s+'\n')
        
line = lines.index('  - name: 🌏 国内媒体\n')
#insert servernae
for s in servername:
        lines.insert(line+5,'      - '+s+'\n')

line = lines.index('  - name: Ⓜ️ 微软服务\n')
#insert servernae
for s in servername:
        lines.insert(line+5,'      - '+s+'\n')  
        
line = lines.index('  - name: 📲 电报信息\n')
#insert servernae
for s in servername:
        lines.insert(line+5,'      - '+s+'\n')  
        
line = lines.index('  - name: 🍎 苹果服务\n')
#insert servernae
for s in servername:
        lines.insert(line+5,'      - '+s+'\n')  
        
line = lines.index('  - name: 🎯 全球直连\n')
#insert servernae
for s in servername:
        lines.insert(line+4,'      - '+s+'\n')  

line = lines.index('  - name: 🐟 漏网之鱼\n')
#insert servernae
for s in servername:
        lines.insert(line+5,'      - '+s+'\n')          

'''
#====================================================================== 
#join： 
s = ''.join(lines) 
#print(s)

#write swc.swcd：
mytime =(time.strftime("%Y%m%d_%H_%M_%S", time.localtime()))
with open(mytime+'.yml',"w",encoding="UTF-8") as z: 
        z.write(s) 
        z.close()       
