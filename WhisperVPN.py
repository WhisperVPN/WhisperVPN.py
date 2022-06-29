import os, time

try:
  import colorama
except:
  os.system('python3 -m pip install colorama')
  
import colorama

class Whisper:
  def __init__(self, keys, server, port):
    self.keys = keys
    self.server = server
    self.port = port
  
  def Menu(self):
    os.system('clear')
    print('')
    print(f'''{colorama.Fore.BLUE} █     █░ ██░ ██  ██▓  ██████  ██▓███  ▓█████  ██▀███   ██▒   █▓ ██▓███   ███▄    █    
▓█░ █ ░█░▓██░ ██▒▓██▒▒██    ▒ ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▓██░   █▒▓██░  ██▒ ██ ▀█   █    
▒█░ █ ░█ ▒██▀▀██░▒██▒░ ▓██▄   ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒ ▓██  █▒░▓██░ ██▓▒▓██  ▀█ ██▒   
░█░ █ ░█ ░▓█ ░██ ░██░  ▒   ██▒▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄    ▒██ █░░▒██▄█▓▒ ▒▓██▒  ▐▌██▒   
░░██▒██▓ ░▓█▒░██▓░██░▒██████▒▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒   ▒▀█░  ▒██▒ ░  ░▒██░   ▓██░   
░ ▓░▒ ▒   ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▐░  ▒▓▒░ ░  ░░ ▒░   ▒ ▒    
  ▒ ░ ░   ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░   ░ ░░  ░▒ ░     ░ ░░   ░ ▒░   
  ░   ░   ░  ░░ ░ ▒ ░░  ░  ░  ░░          ░     ░░   ░      ░░  ░░          ░   ░ ░    
    ░     ░  ░  ░ ░        ░              ░  ░   ░           ░                    ░    
                                                            ░                         
  
                            {colorama.Fore.MAGENTA} © 2022 WhisperVPN LTD.
                        {colorama.Fore.MAGENTA}＞＞＞＞>>>＞{colorama.Fore.BLUE} [Menu]{colorama.Fore.MAGENTA} ＜<<<＜＜＜＜
                                 {colorama.Fore.BLUE}➡ {colorama.Fore.MAGENTA}[1]{colorama.Fore.BLUE} Start VPN
                                 {colorama.Fore.BLUE}➡ {colorama.Fore.MAGENTA}[2]{colorama.Fore.BLUE} About Us
                                 {colorama.Fore.BLUE}➡ {colorama.Fore.MAGENTA}[3]{colorama.Fore.BLUE} Update
                                 {colorama.Fore.BLUE}➡ {colorama.Fore.MAGENTA}[4]{colorama.Fore.BLUE} Report Issues
                                 {colorama.Fore.BLUE}➡ {colorama.Fore.MAGENTA}[5]{colorama.Fore.BLUE} Install Dependencies (Only for Apt)
                                 {colorama.Fore.BLUE}➡ {colorama.Fore.MAGENTA}[6]{colorama.Fore.BLUE} Exit
    {colorama.Fore.RESET}''')
    
  def Update(self):
    print(f'{colorama.Fore.MAGENTA}Updating...{colorama.Fore.RESET}')
    os.system('cd ..; rm -rf WhisperVPN; git clone https://github.com/WhisperVPN/WhisperVPN')
    print(f'{colorama.Fore.MAGENTA}Please press any key and restart VPN...')
    input()
    exit()
    
  def Start(self):
    self.Menu()
    options = int(input(f'                        {colorama.Fore.BLUE}➡ {colorama.Fore.MAGENTA}Option:{colorama.Fore.BLUE} '))
    os.system('clear')
    if options == 1:
      print(f'{colorama.Fore.MAGENTA}Starting WhisperVPN...')
      time.sleep(1)
      print(f'{colorama.Fore.MAGENTA}Please start Tor in other terminal window using command "tor", then press any key (Just for now) ...')
      input()
      print(f'{colorama.Fore.MAGENTA}Starting FTP Server...')
      os.system('bftpd -d')
      time.sleep(1)
      print(f'{colorama.Fore.MAGENTA}Connecting to our server...')
      time.sleep(3)
      print(f'{colorama.Fore.MAGENTA}Connected!')
      os.system(f'ssh -i {self.keys} {self.server} -p {self.port}')
    elif options == 2:
      os.system('am start -a android.intent.action.VIEW -d https://whispervpn.company.site/ > /dev/null 2>&1')
      self.Start()
    elif options == 3:
      self.Update()
      self.Start()
    elif options == 4:
      os.system('am start -a android.intent.action.VIEW -d https://github.com/WhisperVPN/WhisperVPN/issues > /dev/null 2>&1')
      self.Start()
    elif options == 5:
      print(f'{colorama.Fore.MAGENTA}Installing dependecies...{colorama.Fore.RESET}')
      os.system('apt install bftpd tor git openssh')
      self.Start()
    else:
      exit(123)
    
W = Whisper('keypairs.pem', 'linux@ec2-18-236-156-226.us-west-2.compute.amazonaws.com', '32513')
W.Start()
