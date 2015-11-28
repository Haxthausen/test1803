#!/bin/bash

APP_NAME="autodl_match_save_monitor"
LOG_FILE="/home/vsantos/Applications/Torrents/$APP_NAME.log"

DOWNLOAD_HISTORY_FILE="/home/vsantos/.autodl/DownloadHistory.txt"

# Cops.S25E04.720p.HDTV.x264-BAJSKORV   1358645546000   http://thedarksyndicate.me/rssdownload.php?id=99422&authkey=q2bbs33ref5cqnfwhdl58vnb54nklmsv&torrent_pass=sw3fbqzhkga69dh6xoy1b60jnjd1n4hg  1365709564       cops s25e04 720p hdtv x264 bajskorv
# Cops S25E04 720p HDTV x264-BAJSKORV   1358645596000   http://on.iptorrents.com/download.php/761949/Cops%20S25E04%20720p%20HDTV%20x264-BAJSKORV.torrent        1365709564      cops s25e04 720p hdtv x264 bajskorv

# www.reassu.me                 RM
# stellarwinds.me               SW
# www.iptorrents.com            IPT
# torrentshack.eu               TSH
# hdts.ru                       HDTS
# thedarksyndicate.me           TDS
# www.acid-lounge.org.uk        AL
# www.beyondhd.me               BHD
# www.torrentleech.org          TL
# alpharatio.cc          	AR

function autodl_match_save_monitor {
        log_action "Restarted..."
        last_match=`date +%s`
        while [ true ]; do
                while read torrent_match; do
                        #echo $last_match
                        #echo $torrent_match

                        torrent_name=$(echo "$torrent_match" | awk -F "\t" '{print $1}')
                        #echo $torrent_name

                        match_time=$(echo "$torrent_match" | awk -F "\t" '{print $2}' | sed -e 's/000$//g')
                        #echo $match_time

                        torrent_site=$(echo "$torrent_match" | awk -F "\t" '{print $3}' | sed -e 's/^http:\/\///g' | sed -e 's/^https:\/\///g' | sed -e 's/\/.*//g' | sed -e 's/alpharatio.cc/AR/g' | sed -e 's/www.reassu.me/RM/g' | sed -e 's/www.beyondhd.me/BHD/g' | sed -e 's/www.torrentleech.org/TL/g' | sed -e 's/stellarwinds.me/SW/g' | sed -e 's/www.iptorrents.com/IPT/g' | sed -e 's/torrentshack.eu/TSH/g' | sed -e 's/hdts.ru/HDTS/g' | sed -e 's/thedarksyndicate.me/TDS/g' | sed -e 's/www.acid-lounge.org.uk/AL/g')
                        #echo $torrent_site

                        torrent_size=$(echo "$torrent_match" | awk -F "\t" '{print $4}' | awk '{ split( "KB MB GB", unit ); unit_index=0; while( $1>1024 ) { $1/=1024; unit_index++ } printf "%.2f " unit[unit_index], $1 }')
                        #echo $torrent_size

                        if [ "$match_time" -gt $last_match ]; then
                                let last_match=$match_time
                                log_action "Autodl-irssi matched & saved torrent: $torrent_site: $torrent_name, $torrent_size"
                                #echo "`date +"%b %e %T"` `hostname -s` $APP_NAME: $log_action"
                                sleep 1
                        fi
                done <<< "`tail -n 20 "$DOWNLOAD_HISTORY_FILE"`"
                sleep 5
        done
}

function log_action {
        echo "`date +"%b %e %T"` `hostname -s` $APP_NAME: $1" >> $LOG_FILE
}

autodl_match_save_monitor

# Begin of block comment ####
COMMENT_BLOCK= ##############
if [ $COMMENT_BLOCK ]; then #
# Begin of block comment ####

# End of block comment ######
sleep 1 #####################
fi ##########################
# End of block comment ######

#EOF

