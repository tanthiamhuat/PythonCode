# https://www.tecmint.com/convert-files-to-utf-8-encoding-in-linux/
# need to do conversion for special character £
# which convert from £ to Â£
# iconv -f ISO-8859-1 -t UTF-8//TRANSLIT SFTP_Connect.py -o SFTP_Local.py

# connect to SFTP Server
# hostname : sftp.sitr.suezsmartsolutions.com      
# Username : SINGAPORE
# Password : S1n9ap0r3PF337Â£
# Port Number: 8122
host = 'sftp.sitr.suezsmartsolutions.com'
username = 'SINGAPORE'
password = 'S1n9ap0r3PF337Â£'
sftpPath = '/SINGAPORE/Data/Output/consumption_processed/'
port = 8122
     
# http://www.machinelearningtribune.com/2017/07/06/how-to-download-file-from-sftp-using-python/
import paramiko
from stat import S_ISDIR
import os

os.chdir('D:\Python_Code\DAP')
cwd = os.getcwd()
localPath = cwd +'\\consumption'
paramiko.util.log_to_file(cwd+'\\file.txt')
sftpTransport = paramiko.Transport((host, port))
sftpTransport.connect(username = username, password = password)
sftp = paramiko.SFTPClient.from_transport(sftpTransport)
  
# https://stackoverflow.com/questions/24427283/getting-a-files-from-remote-path-to-local-dir-using-sftp-in-python
def download_dir(remote_dir, local_dir):
    import os
    os.path.exists(local_dir) or os.makedirs(local_dir)
    dir_items = sftp.listdir_attr(remote_dir)    
    for item in dir_items:
        ## to extract only 2018 data, which have first five strings as ""CC_18"
        if (item.filename[:5] =='CC_19'):        
            # assuming the local system is Windows and the remote system is Linux
            # os.path.join won't help here, so construct remote_path manually
            remote_path = remote_dir + '/' + item.filename         
            local_path = os.path.join(local_dir, item.filename)
            if S_ISDIR(item.st_mode):
                download_dir(remote_path, local_path)
            else:
                sftp.get(remote_path, local_path)

download_dir(sftpPath,localPath)

sftp.close()
sftpTransport.close()   
     
# https://techtalkontv.wordpress.com/2016/11/05/python-pramiko-sftp-copydownload-all-files-in-a-folder-recursively-from-remote-server/
