pnum=`ps -ef | grep random_login.py | grep -v grep| wc -l`
cd /home/pi/git/UCAS
if [ $pnum -gt 1 ]; then
    ps -ef | grep random_login.py | grep -v grep |awk  '{print "kill -9 " $2}' | sh
    nohup python random_login.py &
elif [ $pnum -eq 1 ]; then
    echo `ps -ef | grep random_login.py | grep -v grep`
elif [ $pnum -eq 0 ]; then
    nohup python random_login.py &
fi


