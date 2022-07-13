import os
import sys
import random
import pykd
from pykd import *
from _datetime import datetime

VLC = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe "

#Must Try : vlc.exe your_input_file_or_stream_here --sout=file/ps:go.mpg 

#--ts-standard={auto,mpeg,dvb,arib,atsc,tdmb}
#--vc1-fps=<float [-340282346638528859811704183484516925440.000000 .. 340282346638528859811704183484516925440.000000]> Frames per Second
#--fps-fps=<string> Frame rate Frame rate
#--sharpen-sigma=<float [0.000000 .. 2.000000]> 
#--gaussianblur-sigma=<float [0.010000 .. 4096.000000]> 
#--directx-3buffering, --no-directx-3buffering 
#--sout-x264-mvrange=<integer> Maximum motion vector length Maximum motion vector length in pixels. -1 is automatic, based on level.
#   Colorspace conversion: --rendering-intent={0 (Perceptual), 1 (Relative colorimetric), 2 (Absolute colorimetric), 3 (Saturation)} Rendering intent for color conversion    


def Radamsa(f ,files):
    
    RdmArgs = ["ber", "ab", "sd","lis","fn","lds","ui","bei","bed","ber"]
    r = random.choice(RdmArgs)
    r2 = random.choice(RdmArgs)
    os.system("radamsa.exe "+f+" -o C:\\Users\\User\\Desktop\\PyFuzzer\\radamsa\\radamsa\\bin\\output\\"+files+" -m "+r+","+r2)
    


def StrmTst(stat):
#def StrmTst():
    if stat == "start":
        os.system("start powershell C:\Python27\python.exe C:\\Users\\User\\Desktop\\PyFuzzer\\radamsa\\radamsa\\bin\\output\\StmServ.py")
#        os.system("start powershell && cd \\output\\ && python -m http.server")

    else:
        pykd.killAllProcesses()




class Handler(eventHandler):
    def __init__(self):
        eventHandler.__init__(self)

    def onException(Handle, exceptionInfo):
#        print(hex(exceptionInfo.exceptionCode))
        

        if exceptionInfo.exceptionCode == 0xc0000005:
        
             print("[X]Access Violation : " +hex(exceptionInfo.exceptionCode))


             file1 = open('my_hash.txt', 'a')

             hash = dbgCommand("!exploitable").split("(")[1].split(")")[0].split("=")[1]

             file1.write(hash + "\n")

             with open("my_hash.txt",'r') as f:
                 crash1 = f.readlines()
                 f.close()

             a = [f.strip() for f in crash1]

             if hash in a:
                 print("\n\n   >>>EXIT<<<\n\n          ==Unique crashes==\n\n")
                 exit()

             if hash not in a :
                 print("\n\n   <<<TRUE>>>\n\n           !!!Different Crash!!!\n\n")

                 now = datetime.now()

                 str_date_time = now.strftime("%d-%m-%Y_%H-%M")

                 nfile = str(str_date_time)+'___logfile.txt'
                 file = open(nfile, 'a')
                 file.write(dbgCommand("k"))
                 file.write(dbgCommand("r"))
                 file.write(dbgCommand("u"))
                 file.write(dbgCommand("lm"))
                 file.write(dbgCommand("!exploitable"))

                 file1.close()
                 file.close()
#                 exit()
                 pykd.killAllProcesses()
                 StrmTst("stop")
#                 exit()
                 
        else :
#            pykd.killAllProcesses()
            exit()
     

def ProcTest(VLCs):


    ts_Rnd= ["auto","mpeg","dvb","arib","atsc","tdmb"]
    ri = random.randint(-1, 1000)
    rf = random.uniform(-340282346638528859811704183484516925440.000000, 340282346638528859811704183484516925440.000000)
    rf2 = random.uniform(0.000000, 2.000000)
    tr = random.choice(ts_Rnd)
    sINT = random.randint(-3, 10)
#    rrr = [ri,rf,rf2,sINT]
    dad=[ri,rf,rf2,sINT]
    rrr = random.choice(dad)
#    ArgRand = [" --fps-fps="+str(ri)," --rendering-intent="+str(sINT)," --target-prim="+str(sINT)," --vc1-fps="+str(rf)," --ts-standard="+str(tr)," --no-directx-3buffering"," --directx-3buffering"," --no-directx-use-sysmem"," --no-directx-overlay"," --sharpen-sigma="+str(rf2)," --sout-x264-keyint="+str(ri)," --sout-x264-mvrange="+str(ri)]
#    ArgR = random.choice(ArgRand)
#    mRAN = ["visual","projectm","goom","glspectrum","wall","clone","yuv","inhibit","wingdi","wgl","vmem","vdummy","gl","glwin32","flaschen","drawable","directdraw","freeze","fps"]
#    run = random.choice(mRAN)
#    ArgR =" --imem-fps="+str(rrr)
    ArgR =" --imem-size="+str(rrr)
#    ArgR = random.choice(ArgRand)
    
    
    
    pykd.startProcess(VLC+" --rate=10.0 --play-and-exit"+" http://127.0.0.1:8000/output/"+VLCs+str(ArgR), pykd.ProcessDebugOptions.BreakOnStart | pykd.ProcessDebugOptions.DebugChildren)

#    pykd.startProcess(VLC+" --play-and-exit"+" http://127.0.0.1:8000/output/"+VLCs+str(ArgR), pykd.ProcessDebugOptions.BreakOnStart | pykd.ProcessDebugOptions.DebugChildren)



    print("[+] Arg Used  :"+ str(ArgR))
    pykd.loadExt("C:\\Program Files (x86)\\Windows Kits\\10\\Debuggers\\x86\\MSEC.dll")
    a = Handler()
#    pykd.go()
    GoStat = pykd.go()
#    print("[+] Process Stat:", str(GoStat))
    pykd.killAllProcesses()
#    print("[+] Process Killed")

def Main(Dir):
    StrmTst("start")
    Count = 0
    while True :
        for files in os.listdir(Dir):
            print(files)
            f = os.path.join(Dir, files)
            Radamsa(f ,files)
            Count = Count + 1
            print("[+] Test Case Number : ",Count)
            ProcTest(files)

        

Main("C:\\Users\\User\\Desktop\\VLC_Media\\Test_Cases")

#Radamsa(sys.argv[1])