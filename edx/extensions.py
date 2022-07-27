fn = input("File Name: ")
new_fn = fn.lower()

if ".gif" in new_fn:
    print("image/gif")
    
elif ".jpg" in new_fn:
    print("image/jpeg")
    
elif ".jpeg" in new_fn:
    print("image/jpeg")
    
elif ".png" in new_fn:
    print("image/png")
    
elif ".pdf" in new_fn:
    print("application/pdf")
    
elif ".txt" in new_fn:
    print("text/plain")
    
elif ".zip" in new_fn:
    print("application/zip")
    
else:
    print("application/octet-stream")
