import os

folder_path = r"C:\Users\Kinza Wakeel\OneDrive\Desktop\LostDataRecovery_Project\RecoveredFiles"

print("=" * 50)
print("        RECOVERED FILES ANALYSIS")
print("=" * 50)

total_files = 0
total_size = 0

for file in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):

        size = os.path.getsize(file_path)

        print(f"\nFile Name : {file}")
        print(f"File Size : {size} bytes")
        print("-" * 50)

        total_files += 1
        total_size += size

print("\n========== RECOVERY SUMMARY ==========")
print(f"Total Recovered Files : {total_files}")
print(f"Total Recovery Size   : {total_size} bytes")
print("=" * 50)
