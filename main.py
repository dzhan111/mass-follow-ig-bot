from instapy import InstaPy

session = InstaPy(username="name", password="pass")
session.login()

session.follow_likers(['fus_gring' , 'taco.with.lalo'], photos_grab_amount = 3, follow_likers_per_photo = 6, randomize=False, interact=False)

session.like_by_tags(["breakingbadirony", "breakingbadmemes"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=10)
session.set_do_comment(True, percentage=10)
session.set_comments(["Sus gus", "Saul goodman", "los pollos hermanos"])


session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
session.set_relationship_bounds(enabled=True, max_followers=8500)

session.end()
