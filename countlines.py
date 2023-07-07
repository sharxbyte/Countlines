import os

def item_line_count(path):
    if os.path.isdir(path):
        return dir_line_count(path)
    elif os.path.isfile(path):
        with open(path, 'r') as f:
            return len(f.readlines())
    else:
        return 0

def dir_line_count(dir):
    lines = 0
    for item in os.listdir(dir):
        item_path = os.path.join(dir, item)
        lines += item_line_count(item_path)
    return lines

def countlines(start, lines=0, header=True, begin_start=None, output_file=None):
    if header:
        output_header = '{:>10} |{:>10} | {:<20}\n'.format('ADDED', 'TOTAL', 'FILE')
        output_header += '{:->11}|{:->11}|{:->20}\n'.format('', '', '')
        if output_file:
            output_file.write(output_header)
        else:
            print(output_header)

    for item in os.listdir(start):
        item_path = os.path.join(start, item)
        if os.path.isfile(item_path) and item.endswith('.py'):
            with open(item_path, 'r') as f:
                newlines = len(f.readlines())
                lines += newlines

                if begin_start is not None:
                    reldir_of_item = '.' + item_path.replace(begin_start, '')
                else:
                    reldir_of_item = '.' + item_path.replace(start, '')

                output_line = '{:>10} |{:>10} | {:<20}\n'.format(newlines, lines, reldir_of_item)
                if output_file:
                    output_file.write(output_line)
                else:
                    print(output_line)

        elif os.path.isdir(item_path):
            lines = countlines(item_path, lines, header=False, begin_start=start, output_file=output_file)

    return lines

output_file = 'python_code_summary.txt'

with open(output_file, 'w') as f:
    countlines(os.getcwd(), output_file=f)
