#!bin/sh

# export SECRET_ID='test-kerberos-location'
# kerberos_location = $(python3 akv_get_secret.py)
# echo "Got value for test-kerberos-location: ${kerberos_location}"

if [ $1 != " " ] ; then
    kerberos_location="$1"
    sed -ie "s%<<base_url>>%${kerberos_location}%g" config.json
else
  echo "Need Kerberos Location argument to continue"
  exit 1
fi


# if [ $2 != " " ] ; then
#     kerberos_location="$2"
#     sed -ie "s%<<kerberoslocation>>%${kerberos_username}%g" config.json
# else
#   echo "Need Kerberos Location argument to continue"
#   exit 1
# fi


# if [ $3 != " " ] ; then
#     kerberos_location="$3"
#     sed -ie "s%<<kerberoslocation>>%${kerberos_password}%g" config.json
# else
#   echo "Need Kerberos Location argument to continue"
#   exit 1
# fi

# echo "$kerberos_location"
# echo "$kerberos_username"
# echo "$kerberos_password"






