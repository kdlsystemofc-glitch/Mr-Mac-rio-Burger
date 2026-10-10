import sys

def append_css(source_file, target_file='site/style.css'):
    with open(source_file, 'r', encoding='utf-8') as sf:
        addition = sf.read()
    with open(target_file, 'a', encoding='utf-8') as tf:
        tf.write('\n' + addition)
    print(f'Successfully appended {source_file} to {target_file}')

if __name__ == '__main__':
    append_css(sys.argv[1])
