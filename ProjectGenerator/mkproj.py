import os
import sys

def check_dir(dir_name):
    sub_dirs = [x[0] for x in os.walk("./")]
    return "./"+dir_name in sub_dirs

def check_lanuage(lang):
    lang_list = ["java","py","c","cpp","cs","js"]

    return lang in lang_list
def write_file(filename,content):
    with open(filename,"w") as f:
        f.write(content)
        f.close()

def get_hello_world(lang):

    if lang == "java":
        return ("class HelloWorld {\n "
                "\tpublic static void main(String[] args) {\n"
                "\t\tSystem.out.println(\"Hello, World!\");\n"
                "\t}\n"
                "}")

    if lang == "py":
        return ("def main():\n"
                "\tprint(\"Hello world!\")\n\n"
                "if __name__ == \"__main__\":\n"
                "\tmain()")

    if lang == "c":
        return ("#include <stdio.h>\n"
                "int main() {\n"
                "\tprintf(\"Hello, World!\");\n"
                "\treturn 0;\n"
                "}")

    if lang == "cpp":
        return ("#include <iostream>\n"
                "int main() {\n"
                "\tstd::cout << \"Hello World!\";\n"
                "\treturn 0;\n"
                "}")

    if lang == "cs":
        return ("namespace Main\n"
                "{\n"
                "\tclass Hello {\n"
                "\t\tstatic void Main(string[] args)\n"
                "\t\t{\n"
                "\t\t\tSystem.Console.WriteLine(\"Hello World!\");\n"
                "\t\t}\n"
                "\t}\n"
            "}")

    if lang == "js":
        return "console.log(\"Hello world!\")"

def create_source_code(lang,path):
    file_name = "Main." + lang
    write_file(path +"/" + file_name,get_hello_world(lang))
def create_proj(name,lang):

    if check_dir(name):
        print("Project already exists ")
        sys.exit()
    parent_dir = "./"
    path = os.path.join(parent_dir, name)
    os.mkdir(path)
    create_source_code(lang, path)
    print(name,"project has been made")

def handle_arguments(arg):
    if len(arg)-1 == 0:
        print("No command line arguments try -help")
        sys.exit()

    if arg[1] == "-help":
        print("mkproj [your project name] [programming language]")
        sys.exit()

    if len(arg)-1 == 1 :
        print("Please select a language")
        sys.exit()
    if arg[1][0] == "-":
        print("Unknown command try -help")
        sys.exit()

    if len(arg) == 3:
        if check_lanuage(arg[2]):
            create_proj(arg[1],arg[2])
        else: print("There is no language named: ",arg[2])
        sys.exit()
    if len(arg) > 3:
        print("To mutch arguments try -help")
        sys.exit()

def main():
    handle_arguments(sys.argv)




if __name__ == "__main__":
    main()