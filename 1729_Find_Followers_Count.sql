SELECT user_id, count(follower_id) as followers_count
From Followers
GROUP BY user_id
ORDER BY user_id;
