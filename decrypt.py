def read_file(file_path):
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
        grid_index = lines.index("Grid:")
        word_index = lines.index("Words:")
        grid = [line.split() for line in lines[grid_index + 1:word_index]]
        word = [w.strip().upper() for w in lines[word_index + 1:]]
    return grid, word


def search_in_direction(grid, mot, x, y, dx, dy):
    positions = []

    for i in range(len(mot)):
        nx, ny = x + dx * i, y + dy * i

        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
            if grid[ny][nx] != mot[i]:
                return None
            positions.append((ny, nx))
        else:
            return None

    return positions


def find_word(grid, word_list):
    found_words = {}
    for w in word_list:
        w = w.strip().upper()
        if not w:
            continue
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == w[0]:
                    directions = [
                        (-1, -1), (-1, 0), (-1, 1),
                        (0, -1),          (0, 1),
                        (1, -1), (1, 0), (1, 1)
                    ]
                    for dx, dy in directions:
                        for motif in [w, w[::-1]]:
                            pos = search_in_direction(grid, motif, j, i, dx, dy)
                            if pos:
                                found_words[w] = pos
                                break
                        if w in found_words:
                            break
                if w in found_words:
                    break
            if w in found_words:
                break
    return found_words


def flag_words_found(grid, found_words_positions):
    for positions in found_words_positions.values():
        for y, x in positions:
            grid[y][x] = "_"
    return grid


# --- MAIN ---
grid, word_list = read_file("challenge.txt")

print("Original Grid:")
for row in grid:
    print(" ".join(row))

print("\nWords to Find :", word_list)

found_words = find_word(grid, word_list)
found_list = list(found_words.keys())
not_found = [w for w in word_list if w not in found_words]

print("\nFound Words :")
for w in found_list:
    print(w)

print("\nNot Found words :")
for w in not_found:
    print(w)

# Mark the Letter 
grid = flag_words_found(grid, found_words)

print("\nMarked Grid::")
for row in grid:
    print(" ".join(row))

# Extract remaining letters for password
password = "".join(letter for row in grid for letter in row if letter != "_")
print("\nPassword :", password)

# Save results to file
with open("flag.txt", "w") as f:
    f.write("\nFlagged grid:\n")
    for row in grid:
        f.write(" ".join(row) + "\n")
    f.write("\nfound word:\n")
    for w in found_list:
        f.write(f"{w}\n")
    f.write("\nWords not found:\n")
    for w in not_found:
        f.write(f"{w}\n")
    f.write("\nPassword:\n")
    f.write(password + "\n")
