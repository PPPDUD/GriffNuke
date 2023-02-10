import scratchattach as scratch3, random
random.randint(20, 100)

while True:
    print()
    try:
        user = scratch3.get_user(input("Please provide the profile to scan: "))

    except Exception as e:
        print(str(e))
        while True:
            pass
    print("Agent #" + str(random.randint(20, 100)), "is on the job.\nLoading comments..")

    print()
    comments = user.comments(limit=40, page=1)
    print("Filtering comments..\n")

    try:
        for target in comments:
            author = target["User"]
            target = target["Content"].lower()
            if "http" in target or "@" in target or "check out" in target or len(target.split()) < 3:
                print()
                # print("ADS DETECTED: ")
                print("AUTHOR:", author)
                print("CONTENTS:", target)

                print()

    except Exception as e:
        print(str(e))
