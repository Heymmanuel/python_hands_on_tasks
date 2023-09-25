def collect_day_reviews(num_days):
  day_review = {}
  for day in range(1, num_days + 1):
    print(f'Day {day}: ')
    review = input("Enter your review or commentary for the day: ")
    day_review[day] = review
  return day_review

num_days = 100
day_review = collect_day_reviews(num_days)

print("\nDay Reviews:")
for day, review in day_review.items():
  print(f'Day {day}: {review}')