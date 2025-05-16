# Day 2 - Regex Software Services Internship

## Overview
On Day 2, I learned more advanced Linux command-line utilities and editing tools. This included file operations using `cp`, `mv`, and navigating directories, as well as an introduction to the `vi` text editor. I was also introduced to file archiving using the `tar` command.

---

## Linux Commands Covered

### `cp` - Copy Files and Directories
```bash
cp source.txt destination.txt
cp file.txt /path/to/directory/
```

### `mv` - Move or Rename Files
```bash
mv oldname.txt newname.txt
mv file.txt /path/to/directory/
```

### `cd -` - Switch to Previous Directory
```bash
cd -
```

---

## vi Editor Basics

### Opening a File in `vi`
```bash
vi demo.txt
```

### Modes in vi
- `i` → Insert mode (start editing)
- `Esc` → Exit insert mode

### vi Commands
- `:wq` → Save and quit
- `:q` → Quit (if no changes)
- `:q!` → Quit without saving
- `yy` → Copy a line
- `p` → Paste the copied line
- `dd` → cut a line

---

## Archiving with `tar`

### `tar -cf` - Create Archive
```bash
tar -cf save.tar file1 file2
```

### `tar -tf` - List Contents of Archive
```bash
tar -tf save.tar
```

### `tar -xf` - Extract Files from Archive
```bash
tar -xf save.tar
tar -xf save.tar file1
```

---

## Summary
Today's session focused on practical file management and editing using the terminal, along with efficient file packaging using the `tar` utility. This knowledge is fundamental for managing data and logs in a Unix-based system.