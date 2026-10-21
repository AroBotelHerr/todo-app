filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]

# Print filenames without their extensions
for filename in filenames:
    s = filename.title()[:-4]
    print(s)  # Assumes all extensions are 4 characters long
