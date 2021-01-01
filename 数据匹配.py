sat_igr = []
sat_ssr =[]
sat_out =[]
y=m=d=h=min=s=""
#read datas for list
f  = open('E:/DataSets/广域差分实验数据/SSR/igr21381.sp3/igr21381.sp3','r')
f1 = open('E:/DataSets/广域差分实验数据/SSR/ALaasPPP/SatPOS_SSR.txt','r')

for lines in f:
    if(lines[0]=="*" or lines[0]=="P"):
        if (lines[0] == "*"):
            y = lines[3:7]
            m = lines[8:10]
            if  m[0]==' ':
                m[0]='0'
            d = lines[11:13]
            if  d[0]==' ':
                d[0]='0'

            if lines[14]==' ':
                h = '0'+lines[15:16]
            else:
                h = lines[14:16]
            if lines[17] == ' ':
                min = '0' + lines[18:19]
            else:
                min = lines[17:19]
            if lines[20]==' ':
                s = '0'+lines[21:22]
            else:
                s = lines[20:22]

        if(lines[0]=="P"):
            prn = lines[2:4]
            sat_x = lines[5:18]
            sat_y = lines[19: 32]
            sat_z = lines[33:46]
            sat_dt = lines[49:60]
            time =y+"/"+ m+"/"+ d+" "+h+":"+min+":"+s+"    sat:"+prn+"     X="+sat_x+"    Y="+sat_y+"    Z="+sat_z+"    dts="+sat_dt
            sat_igr.append(time)
f.close()
for lines in f1:
    sat_ssr.append(lines.replace('\n', ''))
f1.close()
#匹配
for lines_igr in sat_igr:
    igr = lines_igr.strip()
    for lines_ssr in sat_ssr:
        ssr= lines_ssr.strip()
        if (igr[0:19] == ssr[0:19] and int(igr[27:29]) == int(ssr[27:29])):
            dx=format(float(ssr[36:49])-float(igr[36:49])*1e3,'.6f')
            dy=format(float(ssr[55:68])-float(igr[55:68])*1e3,'.6f')
            dz=format(float(ssr[74:87])-float(igr[74:87])*1e3,'.6f')
            dt=format(float(ssr[95:107])*1e6-float(igr[95:107]),'.6f')
            time1=igr[0:19]+"    sat:"+igr[27:29]+"    DX="+"{:>12}".format(dx)+"    DY="+"{:>12}".format(dy) + "    DZ="+"{:>12}".format(dz)+"    Dts="+"{:>12}".format(dt)
            sat_out.append(time1)
#std rms computer
count = [0]*32
dx = [0.0]*32
dy = [0.0]*32
dz = [0.0]*32
dt = [0.0]*32
rmsx = [0.0]*32
rmsy = [0.0]*32
rmsz = [0.0]*32
rmsdt = [0.0]*32
std1 = [0.0]*32
std = [0.0]*32
for lines_out in sat_out:
    out = lines_out.strip()
    i = int(out[27:29])-1
    dx[i] += float(out[36:48])*float(out[36:48])
    dy[i] += float(out[55:67])*float(out[55:67])
    dz[i] += float(out[74:86])*float(out[74:86])
    dt[i] += float(out[94:106])*float(out[94:106])
    count[i]=count[i]+1
for k in 32:
    rmsx[k] = pow(dx[k]/count[k],0.5)
    rmsy[k] = pow(dy[k]/count[k],0.5)
    rmsz[k] = pow(dz[k]/count[k],0.5)
    rmsdt[k] = pow(dt[k]/count[k],0.5)

#write results
f2 = open('E:/DataSets/广域差分实验数据/SSR/ALaasPPP/DeltaSsr.txt','w')
for j in sat_out:
    f2.write(j+'\n')
f2.close()

#write results rms
f3 = open('E:/DataSets/广域差分实验数据/SSR/ALaasPPP/DeltaSsrRms.txt','w')
for e in rmsx:
    f3.write("G"+(e+1)+":"+rmsx[e]++rmsy[e]+rmsz[e]+rmsdt[e]+'\n')
f3.close()

