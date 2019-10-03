#!/bin/bash

REMOTE_DB_FOLDER="KeePass/mydb.kdbx"    #the path where your database is located on your drive
LOCAL_DB_FOLDER="/root/gdrive/"         #the path where you want pull your drive directories
RCLONE_REMOTE_NAME="remote"             #the remote name chosen during rclone installation


function usage()
{
    echo ""
    echo "keepass.sh [--push|--pull]"
    echo "  -h --help"
    echo "  --push          update local database"
    echo "  --pull          update remote database"
    echo ""
}

while [ "$1" != "" ]; do
    PARAM=`echo $1 | awk -F= '{print $1}'`
    case $PARAM in
        -h | --help)
            usage
            exit
            ;;
        --push)
            rclone -P copy "$LOCAL_DB_FOLDER $RCLONE_REMOTE_NAME:$REMOTE_DB_FOLDER" 
            ;;
        --pull)
            rclone -P copy "$RCLONE_REMOTE_NAME:$REMOTE_DB_FOLDER" "$LOCAL_DB_FOLDER"
            ;;
        *)
            echo "ERROR: unknown parameter \"$PARAM\""
            usage
            exit 1
            ;;
    esac
    shift
done
echo "Done!"
