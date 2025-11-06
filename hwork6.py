# List of blog post views
blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

# Variable to count trending posts
trending_posts = 0

# Loop through each blog view count
for views in blog_views:
    if views > 1000:
        print("Trending")
        trending_posts += 1  # Increment count for trending posts
    elif 500 <= views <= 1000:
        print("Average")
    else:
        print("Low Traffic")

# Calculate total views
total_views = sum(blog_views)

# Print summary
print("Total views:", total_views)
print("Number of trending posts:", trending_posts)
