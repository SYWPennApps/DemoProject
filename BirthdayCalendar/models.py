from django.db import models

class User(models.Model):
	syw_id=models.BigIntegerField(unique=True)
	name=models.CharField(max_length=64)
	image_url=models.URLField(null=True)
	created=models.DateTimeField(auto_now_add=True,null=True)
	updated=models.DateTimeField(auto_now=True,null=True)
	
class UserFollowship(models.Model):
	followed_by=models.ForeignKey(User, to_field="syw_id")
	follower_id=models.BigIntegerField()
	follower_name=models.CharField(max_length=64)
	follower_image_url=models.URLField(null=True)
	birth_day=models.IntegerField()
	birth_month=models.IntegerField()
	created=models.DateTimeField(auto_now_add=True,null=True)
	updated=models.DateTimeField(auto_now=True,null=True)
	
	class Meta:
		unique_together = ("followed_by", "follower_id")
	
	

	
	
