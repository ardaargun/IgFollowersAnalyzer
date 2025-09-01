import json
import os


DATA_PATH = # === Change this to your extracted folder path ===
OUTPUT_FILE = os.path.join(DATA_PATH, "followers_comparison.txt")

with open(os.path.join(DATA_PATH, "followers_1.json"), encoding="utf-8") as f:
    followers_data = json.load(f)
followers = {entry["string_list_data"][0]["value"] for entry in followers_data}

with open(os.path.join(DATA_PATH, "following.json"), encoding="utf-8") as f:
    following_data = json.load(f)
following = {entry["string_list_data"][0]["value"] for entry in following_data["relationships_following"]}

not_following_back = following - followers
you_dont_follow_back = followers - following

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("✅ People you follow but don’t follow back:\n")
    f.write("\n".join(sorted(not_following_back)))
    f.write("\n\n")
    f.write("✅ People who follow you but you don’t follow back:\n")
    f.write("\n".join(sorted(you_dont_follow_back)))

print(f"✅ Results saved to: {OUTPUT_FILE}")
