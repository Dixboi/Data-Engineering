
import pycodestyle

def style_check():
    style_checker = pycodestyle.StyleGuide()

    result = style_checker.check_files(['..\etl\etl.py', '..\main.py'])

    result.messages

if __name__ == "__main__":
    style_check()