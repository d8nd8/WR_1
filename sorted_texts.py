def count_lines(*file_paths):
    lines_count_list =[]
    for file in file_paths:
        count = 0
        with open(file) as f:
            for line in f:
                if line.strip():
                    count += 1
            lines_count_list.append((file, count))
    return lines_count_list

count_lines("1.txt", "2.txt", "3.txt")
def sorted_file(file_list ,output_file):
    lines_count_list = count_lines(*file_list)
    sorted_files = sorted(lines_count_list, key=lambda x: x[1])

    with open(output_file, 'w') as fw:
        for file, line_count in sorted_files:
            fw.write(f"{file}\n")
            fw.write(f"{line_count}\n")
            with open(file) as fr:
                fw.write(fr.read().strip())
                fw.write('\n')
    return sorted_files

file_list = ["1.txt", "2.txt", "3.txt"]
sorted_files_list = sorted_file(file_list, "sorted.txt")