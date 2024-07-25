rrr.py检测文件夹里js和html中的敏感信息  
out.txt

```
Analyzing D:\Downloads\bbb\assets\www\cordova.js...Match found for rule 'Linkfinder': 'cordova/channel'
Analyzing D:\Downloads\bbb\assets\www\cordova.js...Match found for rule 'Linkfinder': 'cordova/platform'
Analyzing D:\Downloads\bbb\assets\www\cordova.js...Match found for rule 'Linkfinder': "cordova/android/nativeapiprovider"
```

link.txt
```
- 'cordova/channel'
- 'cordova/platform'
- cordova/android/nativeapiprovider
- 'cordova/android/promptbasednativeapi'
- 'cordova/android/promptbasednativeapi'
- cordova/android/promptbasednativeapi
- cordova/argscheck
```


npm install -g prettier


formatjs.py格式化js和html文件

```
python3 rrr.py #检测敏感信息
运行rrr.py 会生成两个文件 
out.txt 会把匹配到的敏感信息输出 
link.txt会把规则Linkfinder匹配到的信息输出


python3 formatjs.py #格式化js
```


规则来自hae  
感谢hae还有群友还有gpt  