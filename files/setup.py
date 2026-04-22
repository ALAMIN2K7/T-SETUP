#__________________| SCRIPT INFO |__________________#
# SCRIPT RE-MAKED & BUG FIX BY MOHAMMAD ALAMIN
# PYTHON VERSION : 3.11
# GITHUB : ALAMIN2K7
#_______________| IMPORT MODULES |________________#
import os
os.system('pip install requests');os.system('pip install rich')
import os,time,sys,datetime,rich,requests 
from rich.console import Console
from rich import print
from rich.panel import Panel
from time import localtime as lt
console = Console()

# আপনার অরিজিনাল ক্লিয়ার ফাংশন
def _clear_():
    os.system("clear" if os.name == "posix" else "cls")

# লোগো ফাংশন (যেটি প্রতিবার মেনু কল করার সময় ক্লিয়ার করবে)
def logo():
    _clear_()
    print(" ")
    print(Panel("[bold red]● [bold yellow]● [bold green]●\n[green1]        ╺┳╸┏━╸┏━┓┏┳┓╻ ╻╻ ╻   ┏━┓┏━╸╺┳╸╻ ╻┏━┓\n[spring_green2]         ┃ ┣╸ ┣┳┛┃┃┃┃ ┃┏╋┛   ┗━┓┣╸  ┃ ┃ ┃┣━┛\n[spring_green11]         ╹ ┗━╸╹┗╸╹ ╹┗━┛╹ ╹   ┗━┛┗━╸ ╹ ┗━┛╹  ", style="bold bright_black",title="<[bold white reverse] AUTHOR - MOHAMMAD ALAMIN [/bold white reverse]>"))
    print(Panel("[bold black]【[white]•[bold black]】[bold yellow] AUTHOR      [white]➤ [dark_olive_green2]MOHAMMAD ALAMIN\n[bold black]【[white]•[bold black]】[bold yellow] GITHUB      [white]➤ [dark_olive_green2]ALAMIN2K7\n[bold black]【[white]•[bold black]】[bold yellow] VERSION     [white]➤ [dark_olive_green2]1.0\n[bold black]【[white]•[bold black]】[bold yellow] TELEGRAM    [white]➤ [dark_olive_green2]t.me/ALAMIN2K7\n[bold black]【[white]•[bold black]】[bold yellow] TOOL'S NAME [white]➤ [bold purple reverse] TERMUX SETUP TOOL", style="bold bright_black"))

#__________________| SETUP DONE LOGO |__________________#
def logo2():
    print(" ");print(Panel("[bold red]● [bold yellow]● [bold green]●\n\n[dark_orange3]          ╺┳╸┏━╸┏━┓┏┳┓╻ ╻╻╻   ┏━┓┏━╸╺┳╸╻ ╻┏━┓\n[indian_red]           ┃ ┣╸ ┣┳┛┃┃┃┃ ┃┏╋┛  ┗━┓┣╸  ┃ ┃ ┃┣━┛\n[hot_pink3]           ╹ ┗━╸╹┗╸╹ ╹┗━┛╹ ╹  ┗━┛┗━╸ ╹ ┗━┛╹\n\n[hot_pink2]          ┏━╸╻ ╻╻  ╻     ┏━╸╻┏┓╻╻┏━┓╻ ╻┏━╸╺┳┓\n[orchid]          ┣╸ ┃ ┃┃  ┃     ┣╸ ┃┃┗┫┃┗━┓┣━┫┣╸  ┃┃\n[orange3]          ╹  ┗━┛┗━╸┗━╸   ╹  ╹╹ ╹╹┗━┛╹ ╹┗━╸╺┻┛", style="bold bright_black"))
# আইপি এবং তারিখ ডিটেইলস
try:
    ip = requests.get("https://api.ipify.org", timeout=5).text
except:
    ip = "No Internet Connection"

def __details__():
    dic = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August','9': 'September', '10': 'October', '11': 'November', '12': 'December'}
    now = datetime.datetime.now()
    tgl = now.day
    bln = dic[str(now.month)]
    thn = now.year
    date = f"{tgl}/{bln}/{thn}"
    
    ltx = int(lt()[3])
    if ltx > 12:
        a = ltx - 12
        tag = "PM"
    else:
        a = ltx
        tag = "AM"
    times = f"{a}:{now.strftime('%M')} {tag}"
    
    print(Panel(f"[bold black]【[white]•[bold black]】[dark_cyan]YOUR IP      [white]➤  [steel_blue1]{ip} \n[bold black]【[white]•[bold black]】[dark_cyan]TODAY TIME   [white]➤  [steel_blue1]{times} \n[bold black]【[white]•[bold black]】[dark_cyan]TODAY DATE   [white]➤  [steel_blue1]{date}",style="bold bright_black",title="<[bold white reverse] YOUR INFO [/bold white reverse]>"))

#__________________| MAIN MENU |__________________#
def menu():
    logo() # প্রথমে স্ক্রিন ক্লিয়ার হবে এবং লোগো আসবে
    __details__() # তারপর ডিটেইলস আসবে
    print(Panel("[bold black]【[white]01[bold yellow]/[white]A[bold black]】[dark_slate_gray3]TERMUX PKG SETUP\n[bold black]【[white]02[bold yellow]/[white]B[bold black]】[dark_slate_gray3]ADD BANNER IN TERMUX \n[bold black]【[white]03[bold yellow]/[white]C[bold black]】[dark_slate_gray3]REPORT FOR ANY BUGS\n[bold black]【[white]00[bold yellow]/[white]X[bold black]】[red1]EXIT PROGRAMME", style="bold bright_black",title="<[bold white reverse] MAIN MENU [/bold white reverse]>"))
    
    option = console.input("[bold bright_black]   ╰─>[white] ")
    
    if option in ['1','01','A','a']:
        set_up()
    elif option in ['2','02','B','b']:
        _clear_()
        print(Panel("[bold yellow]BANNER SETUP IS STARTING OUTSIDE THIS TOOL...", style="bold bright_black"))
        
        # এই কমান্ডটি টারমাক্স হোমে গিয়ে ব্যানার টুল নামাবে এবং বর্তমান স্ক্রিপ্টটি বন্ধ করে দিবে
        os.system('cd $HOME && rm -rf T-BANNER && git clone https://github.com/ALAMIN2K7/T-BANNER.git && cd T-BANNER && python2 banner.py')
        
        # সেটআপ কমান্ড রান হওয়ার পর এই স্ক্রিপ্ট থেকে পাকাপাকিভাবে বেরিয়ে যাওয়ার জন্য
        sys.exit() 

    elif option in ['3','03','C','c']:
        os.system('xdg-open https://t.me/ALAMIN2K7')
        menu()
    elif option in ['00','0','X','x']:
        _clear_()
        print(Panel("[bold red]EXIT DONE! THANKS FOR USING.", title="EXIT"))
        sys.exit()
    else:
        menu()

#__________________| SETUP MENU |__________________#
def set_up():
    logo();__details__()
    print(Panel("[bold black]【[white]01[bold yellow]/[white]A[bold black]】[medium_purple1]TERMUX BASIC SETUP\n[bold black]【[white]02[bold yellow]/[white]B[bold black]】[medium_purple1]TERMUX FULL SETUP\n[bold black]【[white]00[bold yellow]/[white]X[bold black]】[red1]BACK TO MAIN MENU", style="bold bright_black",title="<[bold white reverse] SETUP MENU [/bold white reverse]>"))
    option = Console().input("[bold bright_black]   ╰─>[white] ")
    if option in ['1','01','A','a']:basic_setup()
    elif option in ['2','02','B','b']:full_setup()
    elif option in ['00','0','X','x']:menu()
    else:
        print(Panel("[bold black]【[white]=[bold black]】 [bold blue]OPTION NOT FOUND IN MENU..",title="<[bold white reverse] EXIT ~ [/bold white reverse]>"));menu()
#__________________| BASIC SETUP |__________________#
def basic_setup():
    print(Panel("[bold black]【[white]•[bold black]】[blue_violet]INSTALLING START IN 3 SEC...",style="bold bright_black"));time.sleep(3)
    print("\n\n");print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2] PKG[light_green] UPDATE ",style="bold bright_black"))
    os.system("pkg update -y")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2] PKG[light_green] UPGRADE ",style="bold bright_black"))
    os.system("pkg upgrade -y")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PYTHON ",style="bold bright_black"))
    os.system("pkg install python -y")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PYTHON2 ",style="bold bright_black"))
    os.system("pkg install python2 -y")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PYTHON3 ",style="bold bright_black"))
    os.system("pkg install python3")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] LSD ",style="bold bright_black"))
    os.system("pkg install lsd -y")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] TSU ",style="bold bright_black"))
    os.system("pkg install tsu -y")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] TMUX ",style="bold bright_black"))
    os.system("apt install tmux")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] REQUESTS ",style="bold bright_black"))
    os.system("pip install requests")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] REQUESTS ",style="bold bright_black"))
    os.system("pip2 install requests")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PYCURL ",style="bold bright_black"))
    os.system("pip install pycurl")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] MECHANIZE ",style="bold bright_black"))
    os.system("pip2 install mechanize")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] BS4 ",style="bold bright_black"))
    os.system("pip install bs4")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] BS4 ",style="bold bright_black"))
    os.system("pip2 install bs4")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] RICH ",style="bold bright_black"))
    os.system("pip install rich")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] RUBY ",style="bold bright_black"))
    os.system("pip install pycurl")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] LOLCAT ",style="bold bright_black"))
    os.system("gem install lolcat")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PHP ",style="bold bright_black"))
    os.system("pip install php")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] LOLCAT ",style="bold bright_black"))
    os.system("pip install lolcat")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] FETURES ",style="bold bright_black"))
    os.system("pip install futures")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] HTTPX ",style="bold bright_black"))
    os.system("pkg install httpx")
    _clear_();logo();logo2()
#__________________| FULL SETUP |__________________#
def full_setup():
    print(Panel("[bold black]【[white]•[bold black]】[blue_violet]INSTALLING START IN 3 SEC...",style="bold bright_black"));time.sleep(3)
    print("\n\n");print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2] PKG[light_green] UPDATE ",style="bold bright_black"))
    os.system("pkg update")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2] PKG[light_green] UPGRADE ",style="bold bright_black"))
    os.system("pkg upgrade")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PYTHON ",style="bold bright_black"))
    os.system("pkg install python")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PYTHON2 ",style="bold bright_black"))
    os.system("pkg install python2")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PYTHON3 ",style="bold bright_black"))
    os.system("pkg install python3")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] LSD ",style="bold bright_black"))
    os.system("pkg install lsd -y")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] TSU ",style="bold bright_black"))
    os.system("pkg install tsu -y")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] WGET ",style="bold bright_black"))
    os.system("pkg install wget")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PYTHON PIP ",style="bold bright_black"))
    os.system("pkg install python-pip")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] FISH ",style="bold bright_black"))
    os.system("pkg install fish")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] RUBY ",style="bold bright_black"))
    os.system("pkg install ruby")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] HELP ",style="bold bright_black"))
    os.system("pkg install help")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] DNSUTILS ",style="bold bright_black"))
    os.system("pkg install dnsutils  ")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PHP ",style="bold bright_black"))
    os.system("pkg install php")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PERL ",style="bold bright_black"))
    os.system("pkg install perl")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] LUA ",style="bold bright_black"))
    os.system("pkg install lua")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PARALLEL ",style="bold bright_black"))
    os.system("pkg install parallel")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] NMAP ",style="bold bright_black"))
    os.system("pkg install nmap")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] BASH ",style="bold bright_black"))
    os.system("pkg install bash")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] CLANG ",style="bold bright_black"))
    os.system("pkg install clang")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] NANO ",style="bold bright_black"))
    os.system("pkg install nano")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] W3M ",style="bold bright_black"))
    os.system("pkg install w3m")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] HYDRA ",style="bold bright_black"))
    os.system("pkg install hydra")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] COWSAY ",style="bold bright_black"))
    os.system("pkg install cowsay")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] CURL ",style="bold bright_black"))
    os.system("pkg install curl")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] TAR ",style="bold bright_black"))
    os.system("pkg install tar")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] ZIP ",style="bold bright_black"))
    os.system("pkg install zip")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] UNZIP ",style="bold bright_black"))
    os.system("pkg install unzip")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] TOR ",style="bold bright_black"))
    os.system("pkg install tor")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] NET-TOOLS ",style="bold bright_black"))
    os.system("pkg install net-tools")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] SUDO ",style="bold bright_black"))
    os.system("pkg install sudo")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] WIRESHARK ",style="bold bright_black"))
    os.system("pkg install wireshark")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] TMUX ",style="bold bright_black"))
    os.system("apt install tmux")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] CRUNCH ",style="bold bright_black"))
    os.system("pkg install crunch")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] WGETRC ",style="bold bright_black"))
    os.system("pkg install wgetrc")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] WCALC ",style="bold bright_black"))
    os.system("pkg install wcalc")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] OPENSSL ",style="bold bright_black"))
    os.system("pkg install openssl")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] OPENSSL-TOOL ",style="bold bright_black"))
    os.system("pkg install openssl-tool")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] BMON ",style="bold bright_black"))
    os.system("pkg install bmon")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] VPN ",style="bold bright_black"))
    os.system("pkg install vpn")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] UNRAR ",style="bold bright_black"))
    os.system("pkg install unrar")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] TOILET ",style="bold bright_black"))
    os.system("pkg install toilet")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PROOT ",style="bold bright_black"))
    os.system("pkg install proot")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] NET TOOLS ",style="bold bright_black"))
    os.system("pkg install net-tools")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] VIM ",style="bold bright_black"))
    os.system("pkg install vim")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] VIN PYTHON ",style="bold bright_black"))
    os.system("pkg install vim-python")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] IRED ",style="bold bright_black"))
    os.system("pkg install ired")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] GOACCESS ",style="bold bright_black"))
    os.system("pkg install goaccess")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] GOLAND ",style="bold bright_black"))
    os.system("pkg install golang")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] KIBI ",style="bold bright_black"))
    os.system("pkg install kibi")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] TSU ",style="bold bright_black"))
    os.system("pkg install tsu")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] MTOOLS ",style="bold bright_black"))
    os.system("pkg install mtools")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] FILE ",style="bold bright_black"))
    os.system("pkg install file")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] VIS ",style="bold bright_black"))
    os.system("pkg install vis")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PASS ",style="bold bright_black"))
    os.system("pkg install pass")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PIC ",style="bold bright_black"))
    os.system("pkg install pick")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] CHROOT ",style="bold bright_black"))
    os.system("pkg install chroot")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] MACCHANGER ",style="bold bright_black"))
    os.system("pkg install macchanger")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] NINJA ",style="bold bright_black"))
    os.system("pkg install ninja")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] ELIXIR ",style="bold bright_black"))
    os.system("pkg install elixir")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] SWIFT ",style="bold bright_black"))
    os.system("pkg install swift")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] XMLSTARLET ",style="bold bright_black"))
    os.system("pkg install xmlstarlet")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] FAKEROOT ",style="bold bright_black"))
    os.system("pkg install fakeroot")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] TEXTINFO ",style="bold bright_black"))
    os.system("pkg install texinfo")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] NETCET ",style="bold bright_black"))
    os.system("pkg install netcat")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] WREN ",style="bold bright_black"))
    os.system("pkg install wren")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] GETLING ",style="bold bright_black"))
    os.system("pkg install gatling")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] CVS ",style="bold bright_black"))
    os.system("pkg install cvs")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] FFMPEG ",style="bold bright_black"))
    os.system("pkg install ffmpeg")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] SCREEN ",style="bold bright_black"))
    os.system("pkg install screen")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] NEOFETCH ",style="bold bright_black"))
    os.system("pkg install neofetch")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] MARIADB ",style="bold bright_black"))
    os.system("pkg install mariadb")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PIOLISP ",style="bold bright_black"))
    os.system("pkg install picolisp")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] CMATRIX ",style="bold bright_black"))
    os.system("pkg install cmatrix")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] DROPBEAR ",style="bold bright_black"))
    os.system("pkg install dropbear")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] OPENSSH ",style="bold bright_black"))
    os.system("pkg install openssh")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PYTHON PIP ",style="bold bright_black"))
    os.system("pkg install python-pip")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] WGET ",style="bold bright_black"))
    os.system("pip2 install wget")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] BS4 ",style="bold bright_black"))
    os.system("pip install bs4")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] BS4 ",style="bold bright_black"))
    os.system("pip2 install bs4")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] REQUESTS ",style="bold bright_black"))
    os.system("pip install requests")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] REQUESTS ",style="bold bright_black"))
    os.system("pip2 install requests")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] MECHANIZE ",style="bold bright_black"))
    os.system("pip install mechanize")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PIP2 MECHANIZE ",style="bold bright_black"))
    os.system("pip2 install mechanize")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PHP ",style="bold bright_black"))
    os.system("pip install php")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PIP2 PHP ",style="bold bright_black"))
    os.system("pip2 install php")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] LOLCAT ",style="bold bright_black"))
    os.system("gem install lolcat")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] WGETRC ",style="bold bright_black"))
    os.system('pip insall pytube')
    _clear_();logo();logo2()
    
menu()
#__________________| FINISHED |__________________#