with open(r"C:\Users\Shyam.sagar\OneDrive - Motherson Group\Desktop\RPA Projects\Python Projects\emails.txt", "r") as file:
    emails = file.readlines()

with open("output.txt", "w") as out:
    for email in emails:
        email = email.strip()

        if "b" in email:
            result = f"Sending to: {email} -> Sent"
        else:
            result = f"Sending to: {email} -> Skipped"

        print(result)
        out.write(result + "\n")