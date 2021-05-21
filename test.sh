domain="localhost:5001"
## declare an array variable
declare -a arr=("" "welcome" "register" "dogs" "info")
## now loop through the above array
for i in "${arr[@]}"
do
    url="http://$domain/$i"
    code=$(curl --head $url -o /dev/null -w '%{http_code}\n' -s)
    echo "$url $code"
done