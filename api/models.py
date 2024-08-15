from django.db import models




class StatusChoices(models.TextChoices):
    DRAFT = 'df','Draft'
    PUBLISH='pb','Publish'
class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    profile_views = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=5, choices=StatusChoices.choices, default=StatusChoices.PUBLISH)

    def df_to_pb(self):
        if self.status == "df":
            self.status = 'pb'
            self.save()

    def pb_to_df(self):
        if self.status == "pb":
            self.status = 'df'
            self.save()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    def __str__(self):
        return self.get_full_name()

class StatusChoices(models.TextChoices):
    DRAFT = 'df','Draft'
    PUBLISH='pb','Publish'
class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    num_of_listens = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=5, choices=StatusChoices.choices, default=StatusChoices.PUBLISH)

    def df_to_pb(self):
        if self.status == "df":
            self.status = 'pb'
            self.save()

    def pb_to_df(self):
        if self.status == "pb":
            self.status = 'df'
            self.save()
    def __str__(self):
        return self.title


class StatusChoices(models.TextChoices):
    DRAFT = 'df','Draft'
    PUBLISH='pb','Publish'

class Song(models.Model):
    title = models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    num_of_listens=models.PositiveIntegerField(default=0)
    status=models.CharField(max_length=5,choices=StatusChoices.choices,default=StatusChoices.PUBLISH)


    def df_to_pb(self):
        if self.status == "df":
            self.status = 'pb'
            self.save()

    def pb_to_df(self):
        if self.status == "pb":
            self.status = 'df'
            self.save()
    def __str__(self):
        return self.title