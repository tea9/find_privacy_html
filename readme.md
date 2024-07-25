rrr.py检测文件夹里js和html中的敏感信息

```
Analyzing D:\Downloads\bbb\assets\www\cordova.js...Match found for rule 'Linkfinder': 'cordova/channel'
Analyzing D:\Downloads\bbb\assets\www\cordova.js...Match found for rule 'Linkfinder': 'cordova/platform'
Analyzing D:\Downloads\bbb\assets\www\cordova.js...Match found for rule 'Linkfinder': "cordova/android/nativeapiprovider"
Analyzing D:\Downloads\bbb\assets\www\cordova.js...Match found for rule 'Linkfinder': 'cordova/android/promptbasednativeapi'
Analyzing D:\Downloads\bbb\assets\www\cordova.js...Match found for rule 'Linkfinder': 'cordova/android/promptbasednativeapi'
Analyzing D:\Downloads\bbb\assets\www\cordova.js...Match found for rule 'Linkfinder': "cordova/android/promptbasednativeapi"
Analyzing D:\Downloads\bbb\assets\www\cordova.js...Match found for rule 'Linkfinder': "cordova/argscheck"
Analyzing D:\Downloads\bbb\assets\www\cordova.js...Match found for rule 'Linkfinder': 'cordova/utils'
Analyzing D:\Downloads\bbb\assets\www\cordova.js...Match found for rule 'Linkfinder': "cordova/base64"
Analyzing D:\Downloads\bbb\assets\www\cordova.js...Match found for rule 'Linkfinder': "cordova/builder"
Analyzing D:\Downloads\bbb\assets\www\cordova.js...Match found for rule 'Linkfinder': 'cordova/utils'
Analyzing D:\Downloads\bbb\assets\www\cordova.js...Match found for rule 'Linkfinder': "cordova/channel"
Analyzing D:\Downloads\bbb\assets\www\cordova.js...Match found for rule 'Linkfinder': 'cordova/utils'
Analyzing D:\Downloads\bbb\assets\www\cordova.js...Match found for rule 'Linkfinder': "cordova/exec"
```


npm install -g prettier


formatjs.py格式化js和html文件

```
python3 rrr.py #检测敏感信息
python3 formatjs.py #格式化js
```


规则来自hae  
感谢群友还有gpt  