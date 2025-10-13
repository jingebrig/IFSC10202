def load_constitution(filename):
    """Load the constitution text into a list of lines without newlines."""
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    return lines

def find_section_bounds(lines, index):
    """Find the start and end index of the section containing the line at 'index'."""
    # Go backward to find the start (look for blank line)
    start = index
    while start > 0 and lines[start].strip() != '':
        start -= 1
    start += 1  # Move to first non-blank line

    # Go forward to find the end (look for blank line)
    end = index
    while end < len(lines) and lines[end].strip() != '':
        end += 1

    return start, end

def search_constitution(lines, term):
    """Search for term in constitution lines and print matching sections."""
    term_lower = term.lower()
    printed_sections = set()
    i = 0

    while i < len(lines):
        if term_lower in lines[i].lower():
            start, end = find_section_bounds(lines, i)
            section_key = (start, end)
            if section_key not in printed_sections:
                printed_sections.add(section_key)
                print(f"\n--- Match at line {i+1} ---")
                for line in lines[start:end]:
                    print(line)
                print('--- End of Section ---\n')
            i = end  # Skip to end of section
        else:
            i += 1

def main():
    lines = load_constitution("constitution.txt")

    while True:
        term = input("Enter a search term (or blank to quit): ").strip()
        if term == "":
            print("Exiting program.")
            break
        search_constitution(lines, term)

if __name__ == "__main__":
    main()