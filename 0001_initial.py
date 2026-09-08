from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=40, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(blank=True, max_length=140, unique=True)),
                ('tagline', models.CharField(blank=True, max_length=160)),
                ('synopsis', models.TextField()),
                ('director', models.CharField(blank=True, max_length=100)),
                ('cast', models.JSONField(blank=True, default=list, help_text='List of actor names')),
                ('release_year', models.PositiveSmallIntegerField()),
                ('runtime_minutes', models.PositiveSmallIntegerField()),
                ('content_rating', models.CharField(default='PG-13', max_length=10)),
                ('score', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('poster_theme', models.CharField(choices=[('ember', 'Ember'), ('wine', 'Wine'), ('teal', 'Teal'), ('indigo', 'Indigo'), ('gold', 'Gold'), ('slate', 'Slate')], default='slate', max_length=10)),
                ('poster_path', models.CharField(blank=True, help_text="TMDB poster_path (e.g. /abc123.jpg), filled in by 'manage.py fetch_posters'", max_length=200, null=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_trending', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('genres', models.ManyToManyField(related_name='movies', to='catalog.genre')),
            ],
            options={
                'ordering': ['-score', 'title'],
            },
        ),
    ]
