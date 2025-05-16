
# Day2_Assignment

## Step-by-step Tasks

1. **Create folders**:
   - Create a folder named `abhi`
   - Create a folder named `aman`

2. **Create 3 files inside `abhi`**:
   ```bash
   mkdir abhi aman
   touch abhi/file1.txt abhi/file2.txt abhi/file3.txt
   ```

3. **Copy the first file from `abhi` to `aman`**:
   ```bash
   cp abhi/file1.txt aman/
   ```

4. **Copy the `abhi` folder into `aman` folder**:
   ```bash
   cp -r abhi aman/
   ```

5. **Copy the third file from `abhi` to `aman` with a new name**:
   ```bash
   cp abhi/file3.txt aman/file3_renamed.txt
   ```

6. **Delete the `aman` folder**:
   ```bash
   rm -rf aman
   ```

---

## Final Folder Structure (before deletion)

```
.
├── abhi
│   ├── file1.txt
│   ├── file2.txt
│   └── file3.txt
└── aman
    ├── file1.txt
    ├── file3_renamed.txt
    └── abhi
        ├── file1.txt
        ├── file2.txt
        └── file3.txt
```

## Final Step

- After deletion, only `abhi` folder will remain.

```
rm -rf aman
```
