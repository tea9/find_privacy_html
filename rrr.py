import yaml  
import sys  
import re  
import os  
from datetime import datetime  
  
# 函数用于加载YAML文件并解析规则  
def load_rules(yaml_file_path):  
    with open(yaml_file_path, 'r', encoding='utf-8') as file:  
        return yaml.safe_load(file)  
  
# 递归遍历文件夹并收集所有文件路径  
def find_files(directory, extensions=None):  
    files = []  
    for root, dirs, file_names in os.walk(directory):  
        for file_name in file_names:  
            if extensions is None or os.path.splitext(file_name)[1] in extensions:  
                files.append(os.path.join(root, file_name))  
    return files  
  
# 函数用于分析多个文件的内容  
def analyze_files_with_rules(files, rules, output_file_path, output_link_file_path):  
    with open(output_file_path, 'w', encoding='utf-8') as output_file,open(output_link_file_path, 'w', encoding='utf-8') as link_output_file:  
        for file_path in files:  
            try:  
                with open(file_path, 'r', encoding='utf-8') as f:  
                    data = f.read()  
                    print(f"Analyzing {file_path}...")  
                    matches_for_file = []  
                    link_matches = []  # 用于存储 "Linkfinder" 规则的匹配项  
  
                    for rule_group in rules:  
                        for rule in rule_group['rule']:  
                            pattern = re.compile(rule['f_regex'])  
                            for match in pattern.finditer(data):  
                                output_file.write(f"Analyzing {file_path}...Match found for rule '{rule['name']}': {match.group()}\n")  
                                matches_for_file.append((rule['name'], match.group()))  
  
                                # 检查是否为 "Linkfinder" 规则  
                                if rule['name'] == "Linkfinder":  
                                    link_matches.append(match.group())  
                                    # 也可以在这里直接将链接写入链接输出文件，但为了避免重复写入，我们在最后统一写入  
  
                    # 如果没有任何匹配项，则打印无匹配信息  
                    if not matches_for_file:  
                        print(f"  No matches found in {file_path}")  
  
                    # 将 "Linkfinder" 规则的所有匹配链接写入链接输出文件  
                    if link_matches:  
                        link_output_file.write(f"Matches for {file_path} using 'Linkfinder' rule:\n")  
                        for link in link_matches:  
                            link_output_file.write(f"- {link}\n")  
  
            except Exception as e:  
                print(f"Error reading file {file_path}: {e}")  
  
# 示例使用  
# 假设你已经有了一个 files 列表，rules 字典，以及两个输出文件路径  
# analyze_files_with_rules(files, rules, 'output.txt', 'links.txt')
  
# ... 其余代码保持不变 ...
  
# 函数用于分析单个文本的内容  
def analyze_text_with_rules(text, rules):  
    for rule_group in rules:  
        for rule in rule_group['rule']:  
            pattern = re.compile(rule['f_regex'])  
            for match in pattern.finditer(text):  
                print(f"Match found in {file_path} for rule '{rule['name']}': {match.group()}")  
  
# 主逻辑  
if __name__ == "__main__":  
    yaml_file_path = 'Rules.yml'  # YAML文件路径  
    directory_path = r"C:\Users\tea90\Desktop\sss"  # 要分析的文件夹路径  
    #output_file_path = "output.txt"  # 指定输出文件的路径
    output_file_path = f"output_{datetime.now().strftime('%H%M%S')}.txt"
    output_link_file_path = f"link_{datetime.now().strftime('%H%M%S')}.txt"
    extensions = ['.js','.html','.java']  # 只想分析的文件扩展名列表，None表示分析所有文件  
  
    # 加载规则  
    rules_data = load_rules(yaml_file_path)  
    rules = rules_data.get('rules', [])  # 确保从YAML中正确获取规则  
  
    # 查找并分析文件  
   # files = find_files(directory_path, extensions)  
    #analyze_files_with_rules(files, rules)  


    if not rules_data:  # 检查rules_data是否为空或False，但通常yaml.safe_load返回的是字典或None  
        print("Error: Failed to load rules from YAML file.")  
        sys.exit(1)  
  
    try:  
        #with open(directory_path, 'r', encoding='utf-8') as f:  
        #    data = f.read()  

        #analyze_text_with_rules(data, rules_data.get('rules', []), output_file_path) 
        # 查找并分析文件  
        files = find_files(directory_path, extensions)  
        analyze_files_with_rules(files, rules,output_file_path,output_link_file_path) 
    except Exception as e:  
        print(f"An error occurred: {e}")  
        sys.exit(1)
  
    # 注意：在analyze_text_with_rules中，我们需要访问file_path，但它是analyze_files_with_rules的局部变量。  
    # 一种解决方法是将file_path作为参数传递给analyze_text_with_rules，或者如示例中所示，在调用print时直接在analyze_files_with_rules中打印它。
