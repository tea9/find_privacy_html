import os  
import subprocess  
  
def format_js_files(source_dir, output_dir):  
    # 确保输出目录存在  
    formatted_dir = os.path.join(output_dir, "formatted")  
    if not os.path.exists(formatted_dir):  
        os.makedirs(formatted_dir)  
  
    # 遍历源目录及其子目录  
    for root, dirs, files in os.walk(source_dir):  
        for file in files:  
            if file.endswith('.js') or file.endswith('.html'): 
                # 构造完整的文件路径  
                input_path = os.path.join(root, file)  
                # 构造输出文件的路径  
                output_path = os.path.join(formatted_dir, file)  
  
                # 使用Prettier格式化文件  
                # 注意：这里我们假设Prettier已经全局安装在Node.js环境中  
                command = f"prettier --write {input_path}"  
                try:  
                    # 直接运行Prettier命令，不需要捕获stdout  
                    subprocess.run(command, shell=True, check=True, stderr=subprocess.PIPE, text=True)  
                    print(f"Formatted {input_path} and saved changes in-place")  
                    # 如果需要，也可以复制或移动格式化后的文件到output_path  
                    # 但由于使用了--write，原文件已被修改，这里只是打印信息  
                except subprocess.CalledProcessError as e:  
                    print(f"Error formatting {input_path}: {e.stderr}")  
  
# 使用示例  
source_directory = "D:\\Downloads\\bbb"  
output_directory = "D:\\Downloads\\fff"  
format_js_files(source_directory, output_directory)