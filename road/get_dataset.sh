
#Downloading the videos zip
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1YQ9ap3o9pqbD0Pyei68rlaMDcRpUn-qz' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1YQ9ap3o9pqbD0Pyei68rlaMDcRpUn-qz" -O videos.zip

#Unzipping the videos
unzip videos.zip

#Removing the zip file
rm videos.zip

#Downloading annotation file for training and validation in json format
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1HAJpdS76TVK56Qvq1jXr-5hfFCXKHRZo' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1HAJpdS76TVK56Qvq1jXr-5hfFCXKHRZo" -O road_trainval_v1.0.json 

#Downloading the instance counts file in json format
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1NfSoI1yVTA46YY7AwVIGRolAqtWfoa8V' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1NfSoI1yVTA46YY7AwVIGRolAqtWfoa8V" -O instance_counts.json 
