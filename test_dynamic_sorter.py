import os
import shutil
import dynamic_sorter

def test_dynamic_sorter():
    sandbox = "sandbox_test"
    if os.path.exists(sandbox):
        shutil.rmtree(sandbox)
    os.makedirs(sandbox)
    
    # Create dummy files
    files = ["test.jpg", "doc.pdf", "script.py", "random.xyz", "no_ext", "app.exe"]
    for f in files:
        with open(os.path.join(sandbox, f), 'w') as fp:
            fp.write("dummy content")
            
    print("Files created:", os.listdir(sandbox))
    
    # Run sorter
    print("Running sorter...")
    dynamic_sorter.sort_files(sandbox)
    
    # Verify
    expected_folders = ["jpg files", "pdf files", "py files", "xyz files"]
    
    items = os.listdir(sandbox)
    print("Items after sort:", items)
    
    for folder in expected_folders:
        if folder not in items:
            print(f"FAIL: Expected folder {folder} not found")
        else:
            print(f"PASS: Folder {folder} exists")
            content = os.listdir(os.path.join(sandbox, folder))
            if not content:
                print(f"FAIL: Folder {folder} is empty")
            else:
                print(f"PASS: Folder {folder} contains {content}")

    # Check excluded files
    if "app.exe" in items:
        print("PASS: app.exe was correctly ignored")
    else:
        print("FAIL: app.exe was moved or deleted")

    if "no_ext" in items:
        print("PASS: no_ext file correctly ignored")
    else:
        print("INFO: no_ext file was moved or deleted?")

    if "exe files" in items:
         print("FAIL: created 'exe files' folder")
    else:
         print("PASS: 'exe files' folder was not created")

    # Cleanup
    # shutil.rmtree(sandbox) 
    print("Test Complete.")

if __name__ == "__main__":
    test_dynamic_sorter()
