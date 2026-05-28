from datetime import datetime
import json
import requests

URL = "https://jsonplaceholder.typicode.com/posts"

def main():
    response = requests.get(URL)
    posts = response.json()
    total_posts = len(posts)

    user_counts_dict = {}
    body_lengths = []
    title_lengths = []
    processed_posts = []

    for post in posts:
        u_id = post["userId"]
        title_text = post["title"]
        body_text = post["body"]

        if (u_id in user_counts_dict):
            user_counts_dict[u_id] += 1
        else:
            user_counts_dict[u_id] = 1

        body_lengths.append(len(body_text))
        title_lengths.append(len(title_text))
        total_len = len(title_text) + len(body_text)
        processed_posts.append(
            {
                "id": post["id"],
                "userId": u_id,
                "total_length": total_len,
            }
        )

    posts_per_user = []
    for u_id, count in user_counts_dict.items():
        posts_per_user.append({"userId": u_id, "posts_count": count})

    top_longest_posts = sorted(processed_posts, key=lambda x: x["total_length"], reverse=True)

    total_body_sum = sum(body_lengths)
    avg_body_length = (total_body_sum / total_posts)

    most_active_user_id = None
    max_posts = 0
    for u_id, count in user_counts_dict.items():
        if count > max_posts:
            max_posts = count
            most_active_user_id = u_id

    title_lengths.sort()
    mid_index = total_posts // 2
    if total_posts % 2 == 0:
        median_title_length = (title_lengths[mid_index - 1] + title_lengths[mid_index]) / 2
    else:
        median_title_length = title_lengths[mid_index]

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = {
        "generated_at": current_time,
        "source": URL,
        "summary": {
            "total_posts": total_posts,
            "avg_body_length": round(avg_body_length, 1),
            "most_active_user_id": most_active_user_id,
            "median_title_length": median_title_length,
        },
        "posts_per_user": posts_per_user,
        "top_longest_posts": top_longest_posts,
    }

    with open("report.json", 'w', encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
    print("Файл успешно создан!")

if __name__ == "__main__":
    main()


#https://github.com/kostyazu1985-arch/python_top_2026_1/blob/main/Home_work/DZ.py