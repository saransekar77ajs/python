print("🔎 WEBSITE URL CHECKER 🔎")

url = input("Enter the url you want to check: ").lower()

check = url[: url.find(":")]
# print(check)

if check == "https":
    print(f"🔒 This website starts with {check} (secure)")
elif check == "http":
    print(f"😈 This website starts with {check} (NOT secure)")
else:
    print(f"❌ {check}: This doesnt look like a complete URL")
