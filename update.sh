upd(){
if [ -d "$HOME/WhisperVPN.py" ];
then
cd $HOME
rm -rf WhisperVPN.py
elif [ -d "$HOME/WhisperVPN.py" ];
then
cd $HOME
rm -rf WhisperVPN.py
else
echo
exit 1
fi
cd $HOME
sleep 1
echo -e "         \e[34mUpdating WhisperVPN...\e[34m"
echo
printf "                     \e[34m["
# While process is running...
while git clone https://github.com/WhisperVPN/WhisperVPN.py 2> /dev/null; do 
    printf  "\e[34m▓▓▓▓▓▓▓▓▓▓▓▓▓\e[34m"
    sleep 1
done
printf "\e[34m]\e[34m"
echo
echo
echo
printf "\e[34m           Updated successfully to the latest version :D\e[34m"
sleep 2.0
clear
cd $HOME
cd WhisperVPN.py
bash WhisperVPN.py
}
vid(){
FILE=$HOME/WhisperVPN.py
if [ -f "$FILE" ]; then
pop
else
echo
fi
}
pop(){
clear
read p
if [ "$p" = "y" ];
then
am start -a android.intent.action.VIEW -d ERROR000 2>/dev/null
clear
banner
menu
elif [ "$p" = "t" ];
then
clear
banner
menu
elif [ "$p" = "z" ];
then
cd $HOM/WhisperVPN.py
rm noob.noob
banner
menu
else
banner
menu
exit
fi
}
banner
menu
